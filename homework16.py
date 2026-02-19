import pandas as pd
import sqlite3

# ================================
# Part 1: Reading Files


# 1. chinook.db (SQLite)

conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql("SELECT * FROM customers", conn)
conn.close()

print("Customers (first 10 rows):")
print(customers_df.head(10))
print("\n")


# 2. iris.json

iris_df = pd.read_json("iris.json")

print("Iris shape:", iris_df.shape)
print("Iris columns:", iris_df.columns.tolist())
print("\n")


# 3. titanic.xlsx

titanic_df = pd.read_excel("titanic.xlsx")

print("Titanic (first 5 rows):")
print(titanic_df.head())
print("\n")


# 4. Flights parquet file

flights_df = pd.read_parquet("flights.parquet")

print("Flights info:")
print(flights_df.info())
print("\n")


# 5. movie.csv

movie_df = pd.read_csv("movie.csv")

print("Random 10 movies:")
print(movie_df.sample(10))
print("\n")


# ================================
# Part 2: Exploring DataFrames


# 1. iris.json

iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[['sepal_length', 'sepal_width']]

print("Iris selected columns:")
print(iris_selected.head())
print("\n")


# 2. titanic.xlsx

titanic_above_30 = titanic_df[titanic_df['Age'] > 30]

print("Passengers older than 30:")
print(titanic_above_30.head())
print("\n")

print("Gender count:")
print(titanic_df['Sex'].value_counts())
print("\n")


# 3. Flights parquet file

flights_selected = flights_df[['origin', 'dest', 'carrier']]

print("Flights selected columns:")
print(flights_selected.head())
print("\n")

print("Number of unique destinations:")
print(flights_df['dest'].nunique())
print("\n")


# 4. movie.csv

long_movies = movie_df[movie_df['duration'] > 120]
long_movies_sorted = long_movies.sort_values(
    by='director_facebook_likes',
    ascending=False
)

print("Movies longer than 120 minutes (sorted):")
print(long_movies_sorted.head())
print("\n")


# ================================
# Part 3: Challenges & Explorations


# Iris statistics

print("Iris statistics:")
print("Mean:")
print(iris_df.mean(numeric_only=True))
print("\nMedian:")
print(iris_df.median(numeric_only=True))
print("\nStandard Deviation:")
print(iris_df.std(numeric_only=True))
print("\n")


# Titanic age stats

print("Titanic age statistics:")
print("Min age:", titanic_df['Age'].min())
print("Max age:", titanic_df['Age'].max())
print("Sum of ages:", titanic_df['Age'].sum())
print("\n")


# Movie.csv challenges

director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()

print("Director with highest total Facebook likes:")
print(top_director)
print("\n")


longest_movies = movie_df[['movie_title', 'director_name', 'duration']] \
    .sort_values(by='duration', ascending=False) \
    .head(5)

print("5 longest movies and directors:")
print(longest_movies)
print("\n")


# Flights parquet challenges

print("Missing values in Flights dataset:")
print(flights_df.isnull().sum())
print("\n")


if 'air_time' in flights_df.columns:
    flights_df['air_time'] = flights_df['air_time'].fillna(
        flights_df['air_time'].mean()
    )
    print("Missing values in 'air_time' filled with mean.")
