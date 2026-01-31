from bs4 import BeautifulSoup
import requests
import sqlite3
import csv
import json
import os

# ============================
# TASK 1 — WEATHER SCRAPING


def task1_weather():
    print("\n--- TASK 1: WEATHER DATA ---")

    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    rows = soup.find("tbody").find_all("tr")

    weather_data = []

    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text.strip()
        temp = int(cols[1].text.replace("°C", ""))
        condition = cols[2].text.strip()

        weather_data.append({
            "day": day,
            "temp": temp,
            "condition": condition
        })

        print(f"{day} | {temp}°C | {condition}")

    # Highest temperature
    max_temp = max(item["temp"] for item in weather_data)
    hottest_days = [item["day"] for item in weather_data if item["temp"] == max_temp]

    print("\nHottest day(s):", hottest_days)

    # Sunny days
    sunny_days = [item["day"] for item in weather_data if item["condition"] == "Sunny"]
    print("Sunny day(s):", sunny_days)

    # Average temperature
    avg_temp = sum(item["temp"] for item in weather_data) / len(weather_data)
    print("Average temperature:", round(avg_temp, 2), "°C")


# ============================
# TASK 2 — JOB SCRAPING + SQLITE


DB_NAME = "jobs.db"

def create_jobs_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)

    conn.commit()
    conn.close()


def task2_scrape_jobs():
    print("\n--- TASK 2: JOB SCRAPING ---")

    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        link = job.find("a")["href"]

        # Check if exists
        cur.execute("""
            SELECT description, link FROM jobs
            WHERE title=? AND company=? AND location=?
        """, (title, company, location))

        existing = cur.fetchone()

        if existing:
            if existing[0] != description or existing[1] != link:
                cur.execute("""
                    UPDATE jobs
                    SET description=?, link=?
                    WHERE title=? AND company=? AND location=?
                """, (description, link, title, company, location))
                print("Updated:", title)
        else:
            cur.execute("""
                INSERT INTO jobs (title, company, location, description, link)
                VALUES (?, ?, ?, ?, ?)
            """, (title, company, location, description, link))
            print("Inserted:", title)

    conn.commit()
    conn.close()


def export_jobs(filter_value, filter_type="location"):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    if filter_type == "location":
        cur.execute("SELECT * FROM jobs WHERE location=?", (filter_value,))
    else:
        cur.execute("SELECT * FROM jobs WHERE company=?", (filter_value,))

    rows = cur.fetchall()
    conn.close()

    filename = f"jobs_{filter_value}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)

    print(f"Exported to {filename}")


# ============================
# TASK 3 — LAPTOP SCRAPING → JSON


def task3_scrape_laptops():
    print("\n--- TASK 3: LAPTOP SCRAPING ---")

    base_url = "https://www.demoblaze.com/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    laptops = []

    items = soup.find_all("div", class_="card-block")

    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)

    print("Saved laptop data to laptops.json")


# ============================
# MAIN EXECUTION


if __name__ == "__main__":

    # Task 1
    task1_weather()

    # Task 2
    create_jobs_table()
    task2_scrape_jobs()

    # Example export 
    # export_jobs("New York")
    # export_jobs("Payne, Roberts and Davis", filter_type="company")

    # Task 3
    task3_scrape_laptops()
