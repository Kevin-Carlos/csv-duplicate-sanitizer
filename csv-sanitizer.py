import pandas

# Provide base path name and file name
base_path = ""
csv_file = ".csv"

df = pandas.read_csv(
  base_path + csv_file,
  index_col="", # Which column is the starting column -- useful when writing the csv
  header=0, 
  names=[]) # Use this and insert to manually set the column headers


# Delete duplicates by providing the column name
df = df.drop_duplicates(subset=[""])

# Write the resulting file
df.to_csv(base_path + "modified_" + csv_file)