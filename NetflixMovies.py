# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
netflix_df = pd.read_csv("netflix_data.csv")

# Step 2: Filter data to remove TV shows
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Step 3: Create netflix_movies DataFrame with selected columns
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Step 4: Filter netflix_movies for movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies["duration"] < 60]

# Step 5: Assign colors to genre groups and create scatter plot
colors = []
for index, row in netflix_movies.iterrows():
    if "Children" in row["genre"]:
        colors.append("blue")
    elif "Documentaries" in row["genre"]:
        colors.append("green")
    elif "Stand-Up" in row["genre"]:
        colors.append("red")
    else:
        colors.append("gray")

fig = plt.figure(figsize=(10, 6))
plt.scatter(netflix_movies["release_year"], netflix_movies["duration"], c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()

# Step 6: Inspect the plot to answer the question
answer = "no"  # Based on the visualization, it's not clear that movies are getting shorter
