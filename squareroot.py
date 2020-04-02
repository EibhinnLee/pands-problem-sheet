# Eibhinn Lee
# Function for squareroot
# sq root of 14.5
# variables
x = 14.5
m = int(input("Enter number of guesses: "))
approx = (1/2)*x

<<<<<<< HEAD
# for loop in range between 0 & no. of guesses
for i in range (0,m):
    # Ist loop : better = (0.5) * (7.25+14.5/7.25)
    better=(1/2) * (approx+x/approx)
    # new value for approx, loop continues until approx = better
    approx = better
    print(approx)


# the more the answer repeats itself after running program = more accurate
=======

def sqrt (v):
    ans= v**(0.5)
    return ans
>>>>>>> 97f94dc6353429790f1e66e3eb8e241162ca20f7


