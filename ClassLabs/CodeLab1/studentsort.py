import pandas as pd

# Load the data
data = pd.read_excel("D:\\Test Files.xlsx")

# Define custom order for gender
gender_order = {'M': 1, 'F': 2}

# Convert 'Gender' to categorical with the custom order
data['Gender'] = pd.Categorical(data['Gender'], categories=['M', 'F'], ordered=True)

# Sort the DataFrame by 'Gender'
sorted_data = data.sort_values(by='Gender')

# Save the sorted DataFrame to a new Excel file
sorted_data.to_excel("D:\\Test Files_Sorted.xlsx", index=False)

# Print the sorted DataFrame
print(sorted_data.head())
