import string
import random
import os

characters = string.ascii_letters + string.digits + string.punctuation
run = True

def generator(otion, password_length):
    options = {
        1: string.ascii_letters,
        2: string.digits,
        3: string.ascii_letters + string.digits,
        4: string.ascii_letters + string.digits + string.punctuation
    }
    characters = options[option]
    password = "".join(random.choice(characters) for i in range(password_length))
    return password

while run:
    try:
        print("""
            Choose option for your password:
            1. Letters
            2. Numbers
            3. Letters and numbers
            4. Letters, numbers and signs\n   
        """)

        option = int(input("#"))
        password_length = int(input("Please enter the password length: #"))

        if option in [1,2,3,4] and password_length > 0:
            password = generator(option, password_length)

            #copied password without pyperclip
            command = f'echo {password.strip()}| clip'
            os.system(command)
            
            print(f"You new password is {password} and it's already copied. (Ctrl+V to paste)")
            run = False
        else:
            print("Please enter correct option")
    except:
        print("Please enter correct option")