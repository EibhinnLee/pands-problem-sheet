# Eibhinn Lee

file = open('moby-dick.txt', 'r')

data = file.read()

words = data.split()

print("number of words in the text file 'Moby Dick is", len(words))

file.close()