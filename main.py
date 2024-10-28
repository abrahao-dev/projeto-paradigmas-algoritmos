# main.py

# Open a .txt file and read its contents into a list
with open('./tasks/aleatorio_1k.txt', 'r') as file:  # Replace 'your_file.txt' with your actual file name
    lines = file.readlines()  # Read all lines into a list

# Now 'lines' contains each line of the file as an element in the list
# You can print the list to verify
print(lines)
