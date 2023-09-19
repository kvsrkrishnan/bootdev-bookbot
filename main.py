print("Read Book")

# Read from File
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# Output Read data
print(file_contents)
print("Finished Reading 'Frankenstein'")

# Get all words in a string
words = file_contents.split()

# Count of all words in the string
print(len(words))

