# Import libraries like pandas for operating on tables
import pandas as pd

# Read your Excel document as a dataframe (df)
df = pd.read_excel("input.xlsx")

# Define a distance metric
def dist(row):
	# stub for now
    return 1

# Apply a transformation to the data and
# store it in a new column called "distance"
df["distance"] = df.apply(dist, axis=1)

# Preview the dataframe
print(df)