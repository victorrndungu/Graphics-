import pandas as pd
import re

# Load the data
data = pd.read_excel("D:\\Test Files.xlsx")

# Generate lists of Male and Female students
male_students = data[data['Gender'] == 'M']
female_students = data[data['Gender'] == 'F']

# Convert DataFrames to lists of names
male_names = male_students['Student Name'].tolist()
female_names = female_students['Student Name'].tolist()

# Print the lists (optional)
print("Male Students:")
print(male_names)
print("\nFemale Students:")
print(female_names)
male_students.to_excel("D:\\Male Students.xlxs", index=True)
female_students.to_excel("D:\\Male Students.xlxs", index=True)