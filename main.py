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
print("Total words:" + str(len(words)))

# Count of all letters in the string
stringLower = file_contents.lower()

# Create a List / Set to get unique list of characters
# Set removes duplicates & creates a distinct immutable values that are unordered.
# Create List & Sort
stringList = sorted(list(set(stringLower)))
# print(stringList)

# Occurence of a substring in the main string
for charac in stringList:
    print(charac + ":" + str(stringLower.count(charac)))

