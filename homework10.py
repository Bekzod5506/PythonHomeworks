#Task 1

import requests

API_KEY = "e0ab28c9d96b8a025e9604c21e839633"
CITY = "Tashkent"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Failed to fetch weather data")

#Task2

import requests
import random

API_KEY = "f1489f03b101522f7c98a87ca27579bc"
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

GENRES = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749,
    "sci-fi": 878
}

genre_input = input("Enter a movie genre: ").lower()

if genre_input not in GENRES:
    print("Genre not supported.")
else:
    params = {
        "api_key": API_KEY,
        "with_genres": GENRES[genre_input],
        "language": "en-US"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        movies = response.json()["results"]

        if movies:
            movie = random.choice(movies)
            print("\n🎬 Recommended Movie:")
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Rating: {movie['vote_average']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch movie data.")



