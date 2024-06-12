# inspect_csv.py
file_path = '/Users/josemarchena/Python/Project1_marchenajose/cleaned_passengers.csv'

# Read the file content as raw text
with open(file_path, 'r') as file:
    content = file.read()

# Display the first few lines to inspect the content
print("\n".join(content.splitlines()[:301]))