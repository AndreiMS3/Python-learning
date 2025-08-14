import pandas as pd


df = pd.read_csv("bestsellers.csv")
"""
print(df.head())

print(df.shape)

print(df.columns)

print(df.describe())"""

df.drop_duplicates(inplace= True) #By setting inplace as True the changes will be made into the original file.

#Renaming some colum names.
df.rename(columns={"Name": "Title", "User Rating": "Rating", "Year": "Publication Year"}, inplace= True)

#Changing the Type of the Price column.
df["Price"] = df["Price"].astype(float)

#Get the author with most sells.
author_counts = df["Author"].value_counts()
print(author_counts)

#Calculating the average rating for each genre in the dataset.
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#Export top selling authors to a csv file.
author_counts.head(10).to_csv("top_authors.csv")

#Export average rating per genre to a csv file.
avg_rating_by_genre.to_csv("average_rating_by_genre.csv")