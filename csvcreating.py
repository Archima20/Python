# Data to be written to the CSV file (**Comma-separated values** (CSV)
# is a text file format that uses commas to separate values. A CSV file stores tabular data (numbers and text) in plain text, where each line of the file typically represents one data record. Each record consists of the same number of fields, and these are separated by commas in the CSV file)
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
