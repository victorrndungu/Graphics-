import pandas as pd
import re

# Load the data
data = pd.read_excel("D:\\Test Files.xlsx")


# Function to clean names and generate email
def generate_email(student_name, existing_emails):
    # Split name into parts
    name_parts = student_name.split()

    # Handle cases with missing names
    first_name = name_parts[1] if len(name_parts) > 0 else ''
    last_name = name_parts[-0] if len(name_parts) > 1 else first_name

    # Clean the names (remove special characters)
    first_name_clean = re.sub(r'\W+', '', first_name)
    last_name_clean = re.sub(r'\W+', '', last_name)

    # Generate initial email
    email_base = f"{first_name_clean[0]}{last_name_clean}".lower()
    email = f"{email_base}@gmail.com"

    # Ensure email is unique
    counter = 1
    original_email = email
    while email in existing_emails:
        email = f"{email_base}{counter}@gmail.com"
        counter += 1

    existing_emails.add(email)
    return email


# Set to keep track of existing emails
existing_emails = set()

# Apply the function to the 'Student Name' column
data['Email Address'] = data['Student Name'].apply(lambda x: generate_email(x, existing_emails))

# Print the first few rows to check the result
print(data.head())
data.to_csv('output.csv', index=False)
data.to_csv('output.tsv', index=False, sep='\t')

data.to_excel("D:\\Test Files_Updated.xlsx", index=False)

