print("Read Book")

# Works in Bash
# Read from File
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# Works local and in PowerShell.
#with open("D:\\workspace\\github.com\\kvsrkrishnan\\bootdev-bookbot\\books\\frankenstein.txt") as f:
#    file_contents = f.read()

# Output Read data
print(file_contents)
print("Finished Reading 'Frankenstein'")

# Get all words in a string
words = file_contents.split()

# Count of all words in the string
print("Total words:" + str(len(words)))

# Count of all letters in the string
stringLower = file_contents.lower()

# Logic 1 - UNSORTED OUTPUT
print("Total letters:" + str(len(stringLower)))

# Create a set 
alphabets1 = {'a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'} # This is a set
alphabets3 = sorted(alphabets1) # print(alphabets1) # print(alphabets3)
# Create a dictionary
alphaDictionary = dict()
for alphabet in alphabets1:
    alphacount = stringLower.count(alphabet) # Get count
    alphaDictionary[alphabet] = alphacount # Create a new index Add to dictionary
print(alphaDictionary)


# Logic 2 - SORTED OUTPUT
# Need a sorted list? Create a sorted list/sequence out of set and loop through. E.g. below
alphabets2 = sorted(list(alphabets1)) # print(alphabets1) # print(alphabets2)

# Create a dictionary
alphaDictionary2 = dict()
for alphabet2 in alphabets2:
    # alphacount1.add(stringLower.count(alphabet)) # Store all the values in set- alternate logic.
    alphacount2 = stringLower.count(alphabet2) # Get count
    alphaDictionary2[alphabet2] = alphacount2 # Create a new index Add to dictionary

print(alphaDictionary2)


"""
# Set that will store all the values - alternate logic.
alphacount1 = set() 
for alphabet in alphabets2:
    alphacount1.add(stringLower.count(alphabet)) # Store all the values in set- alternate logic.
"""

"""
# Logic 3 - Get count of each alphabet in the String
# Create a List / Set to get unique list of characters
# Set removes duplicates & creates a distinct immutable values that are unordered.
# Create List & Sort
stringList = sorted(list(set(stringLower)))
# print(stringList)

# Occurence of a substring in the main string
for charac in stringList:
    print(charac + ":" + str(stringLower.count(charac)))
"""