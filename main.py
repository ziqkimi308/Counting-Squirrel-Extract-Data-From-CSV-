"""
********************************************************************************
* Project Name:  Counting Squirrel
* Description:   This project illustrate how to extract information from a CSV file into a new CSV file
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

# IMPORT
import pandas

# CONSTANT
SQUIRREL_CENSUS_DATA_CSV = "./2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"

# Read csv
data = pandas.read_csv(SQUIRREL_CENSUS_DATA_CSV)

# Specifies data
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# Create dictionary
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_count, red_count, black_count]
}

# Convert dict to dataframe to csv
dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("squirrel_count.csv")
