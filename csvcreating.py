# Data to be written to the CSV file
data = [
    ["Name", "Age", "Location"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 22, "Chicago"]
]

# Specify the file name
file_name = "output.csv"

# Open the file in write mode
with open(file_name, 'w') as csv_file:
    # Loop through each row of data and write it as a comma-separated line
    for row in data:
        csv_file.write(','.join(map(str, row)) + '\n')

print(f"CSV file '{file_name}' has been created.")