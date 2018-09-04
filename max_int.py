

#The user puts in a number
#The user continues to put in numbers until a negative value is entered.
#If a negative value is intered the program prints out the maximum positive intiger from the user.


num_int = 0  # Do not change this line
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line
