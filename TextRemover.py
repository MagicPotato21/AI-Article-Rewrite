import os

# File path

file_path = "article.txt"

# Open the file for reading
with open(file_path, "r", encoding="utf-8") as file:
    # Read the entire file
    text = file.read()
    
    # Replace all occurrences of "CNN" with "Test"
    text = text.replace("CNN", "Test")

# Open the file for writing
with open(file_path, "w", encoding="utf-8") as file:
    # Write the modified text back to the file
    file.write(text)
