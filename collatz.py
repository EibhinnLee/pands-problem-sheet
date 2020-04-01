# Eibhinn Lee
# postive integer = 10
# output (if even) = divide by 2
# output (if odd) = integer * 3 + 1

x = int(input("Enter a positive integer here:"))

# End program when x =1
while x > 0:
    if x ==1:
        print(x)
        break
# if x is even(no rounding) divide by 2
    if x % 2 == 0:
        print(x)
        x = x / 2
# if x is odd (rounding) multiply by 3 and add 1        
    elif x % 2 != 0:
        print(x)
        x = x*3+1  
    

