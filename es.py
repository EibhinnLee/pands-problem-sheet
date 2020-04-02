# Eibhinn Lee
# count the number of lowercase e's within the moby-dick text

# variables
file = "moby-dick.txt"
l=("e")
k = 0

# open file
with open(file, 'r') as f:
   # for each line in text, split into words
    for line in f:
        words = line.split()
        # for each word search through letters in word
        for i in words:
            for letter in i:
                # if e is present, continuously add all the e's in text.
                if(letter==l):
                    k=k+1
print("Lowercase letter 'e' appears in Moby Dick :", k, "times")





