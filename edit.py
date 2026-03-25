# Import libraries like pandas for operating on tables
import pandas as pd
from Levenshtein import distance

# Read your Excel document as a dataframe (df)
df = pd.read_excel("taxa.xlsx")

# Sort values to get similar species next to each other
# This is just a trick to make the demo easier, since
# you could (and should) check every taxon against all others
df = df.sort_values(by=["Genus","Species"])
df["Previous Genus"] = df["Genus"].shift(1)
df["Previous Species"] = df["Species"].shift(1)

# Define an edit distance mapping function
def dist(row):
    # Only match on exact genus names
    # Note that this misses spelling mistakes in Genus
    if row["Genus"] == row["Previous Genus"]:
        return distance(row["Species"], row["Previous Species"])
    return 100

# Apply a transformation to the data and
# store it in a new column called "distance"
df["distance"] = df.apply(dist, axis=1)

# Save the dataframe
df = df.sort_values(by=["distance"])
df.to_excel("output_levenshtein.xlsx", index=False)