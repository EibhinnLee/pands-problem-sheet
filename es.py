# Eibhinn Lee

file = "moby-dick.txt"
l=("e")
k = 0

with open(file, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter e in Moby Dick are:", k)


