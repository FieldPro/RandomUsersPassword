import random
import string
import os
import sys

#Create a function called create_password
def create_password():
    lettersAndDigits = string.ascii_letters + string.digits
    user_number = int(input("For the length of your password. Enter a number between 6 and 10: "))

    if user_number >= 6 and user_number <= 10:
        return ''.join((random.choice(lettersAndDigits) for i in range(user_number)))
        sys.exit()  # exits prpgram
    else:
        create_password()
print(create_password()) #Calls the function