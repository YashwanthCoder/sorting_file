fname = input("Enter file name: ")
fh = open(fname)
words = list()

for line in fh:
    line = line.strip()  # Remove leading and trailing spaces
    word_list = line.split()  # Split the line into words
    for word in word_list:
        if word not in words:
            words.append(word)  # Append the word to the list if it's not already there

words.sort()  # Sort the list of unique words in ascending order

print(words)  # Print the sorted list of unique words as a single list
