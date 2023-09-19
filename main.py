print("Read Book")
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
print(file_contents)
print("Finished Reading 'Frankenstein'")