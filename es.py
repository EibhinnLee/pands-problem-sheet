# Eibhinn Lee

file = open('moby-dick.txt', 'r')

data = file.read().replace(" ","")

number_of_characters = len(data)

print(number_of_characters)

file.close()