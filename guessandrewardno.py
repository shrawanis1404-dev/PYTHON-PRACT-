import random
number=random.randint(1,10)
guess=int(input("Enter any number from 1 to 10"))
if number==guess:
    print("You won a reware of 100 rs")
else:
    print("Wrong guess...try again")
