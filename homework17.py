
import pandas as pd
import numpy as np
import sqlite3

# ===============================
# MERGING AND JOINING



conn = sqlite3.connect("chinook.db")

customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)


customer_invoices = pd.merge(customers, invoices, on="CustomerId", how="inner")

# Total number of invoices for each customer

invoice_count = customer_invoices.groupby("CustomerId")["InvoiceId"].count().reset_index()
invoice_count.rename(columns={"InvoiceId": "Total_Invoices"}, inplace=True)

print("Invoice count per customer:")
print(invoice_count.head())

conn.close()



movies = pd.read_csv("movie.csv")

df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]


left_join = pd.merge(df1, df2, on="director_name", how="left")
print("\nLeft Join Row Count:", len(left_join))

outer_join = pd.merge(df1, df2, on="director_name", how="outer")
print("Full Outer Join Row Count:", len(outer_join))


# ===============================
# GROUPING AND AGGREGATING


titanic = pd.read_csv("titanic.csv")

titanic_grouped = titanic.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "sum",
    "PassengerId": "count"
}).reset_index()

titanic_grouped.rename(columns={"PassengerId": "Passenger_Count"}, inplace=True)

print("\nTitanic Grouped Data:")
print(titanic_grouped)



movie_grouped = movies.groupby(["color", "director_name"]).agg({
    "num_critic_for_reviews": "sum",
    "duration": "mean"
}).reset_index()

print("\nMovie Multi-level Grouping:")
print(movie_grouped.head())



flights = pd.read_csv("flights.csv")

flights_grouped = flights.groupby(["Year", "Month"]).agg({
    "FlightNum": "count",
    "ArrDelay": "mean",
    "DepDelay": "max"
}).reset_index()

flights_grouped.rename(columns={
    "FlightNum": "Total_Flights",
    "ArrDelay": "Avg_ArrDelay",
    "DepDelay": "Max_DepDelay"
}, inplace=True)

print("\nFlights Nested Grouping:")
print(flights_grouped.head())


# ===============================
# APPLYING FUNCTIONS



def classify_age(age):
    if age < 18:
        return "Child"
    else:
        return "Adult"

titanic["Age_Group"] = titanic["Age"].apply(classify_age)

print("\nTitanic with Age_Group:")
print(titanic[["Age", "Age_Group"]].head())



employees = pd.read_csv("employee.csv")

def normalize_salary(group):
    group["Normalized_Salary"] = (
        (group["Salary"] - group["Salary"].min()) /
        (group["Salary"].max() - group["Salary"].min())
    )
    return group

employees = employees.groupby("Department").apply(normalize_salary)

print("\nEmployees with Normalized Salary:")
print(employees.head())


def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

movies["Duration_Category"] = movies["duration"].apply(classify_duration)

print("\nMovies with Duration Category:")
print(movies[["duration", "Duration_Category"]].head())


# ===============================
# USING PIPE



def filter_survived(df):
    return df[df["Survived"] == 1]

def fill_age(df):
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

def create_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

titanic_pipeline = (
    titanic
    .pipe(filter_survived)
    .pipe(fill_age)
    .pipe(create_fare_per_age)
)

print("\nTitanic Pipeline Result:")
print(titanic_pipeline.head())



def filter_delay(df):
    return df[df["DepDelay"] > 30]

def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / (df["AirTime"] / 60)
    return df

flights_pipeline = (
    flights
    .pipe(filter_delay)
    .pipe(add_delay_per_hour)
)

print("\nFlights Pipeline Result:")
print(flights_pipeline.head())
