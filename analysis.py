import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("movies.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nBasic stats:")
print(df.describe())

print("\nMissing values check:")
print(df.isnull().sum())

# Step 2: Answer some questions

# Q1: Top 5 highest rated movies
top5 = df.sort_values(by="rating", ascending=False).head(5)
print("\nTop 5 Highest Rated Movies:")
print(top5[["title", "rating"]])

# Q2: Average rating by genre
avg_by_genre = df.groupby("genre")["rating"].mean().sort_values(ascending=False)
print("\nAverage Rating by Genre:")
print(avg_by_genre)

# Q3: Which director has the most movies in this list
director_counts = df["director"].value_counts()
print("\nMovies per Director:")
print(director_counts)

# Q4: Average rating by decade
df["decade"] = (df["year"] // 10) * 10
avg_by_decade = df.groupby("decade")["rating"].mean()
print("\nAverage Rating by Decade:")
print(avg_by_decade)

# Step 3: Visualizations

# Chart 1: Bar chart - Average rating by genre
plt.figure(figsize=(8, 5))
avg_by_genre.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Movie Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_rating_by_genre.png")
plt.close()

# Chart 2: Pie chart - Genre distribution (how many movies per genre)
genre_counts = df["genre"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(genre_counts, labels=genre_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Genre Distribution in Dataset")
plt.tight_layout()
plt.savefig("genre_distribution.png")
plt.close()

print("\nCharts saved: avg_rating_by_genre.png, genre_distribution.png")
