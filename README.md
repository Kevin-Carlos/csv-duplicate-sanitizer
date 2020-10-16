# Delete duplicate values in CSV files

Built to quickly sanitize data within a semi-large dataset based on values, e.g. removing rows that contain a duplicate email address.

Note: Not meant to be a CLI or anything -- just use as needed. However I might go back and create something a little fancier

## How to Use

Assuming you already have a python3 environment setup.

`pip3 install pandas`

Either clone this repository and follow along the comments.

To run the script: `python3 csv-sanitizer.py` within the directory of the script

```
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
```
