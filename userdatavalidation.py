import random
import string


users = []


def createPwd(fname, lname):
    letters = string.ascii_letters
    endPart = ''.join(random.choice(letters) for i in range(5))
    return fname[:2] + lname[-2:] + endPart


while True:
    print(f"Welcome to HNG TECH! We are so pleased to have you join our organization. \n Please enter your First Name, Second Name and Email address below. \nA Username shall be generated for you with a strong enough password. These shall be your login details to access the staff portal. \n You are free to change the generated password to a convenient one immediately. \n If you have any problems, please message the admin via whatsapp: 08162339425.\nThanks.\n Press Enter to continue.")
    firstName = input("Please enter your first name => ")
    lastName = input("Please enter your last name => ")
    email = input("Please enter your email address => ")
    username = firstName[:3].lower() + lastName[:3].lower()
    password = createPwd(firstName, lastName)

    prompt = input(
        f"Welcome {firstName}, Your Username is {username}. Password : {password}. Are you satisfied with the Password? [Y]es/[N]o => ").lower()
    if prompt == 'y':
        userDetails = {username: {'firstname': firstName,
                                  'lastname': lastName,  'email': email, 'password': password}}
        users.append(userDetails)
        print(users[-1])
        newUser = input(
            "Would you like to create another user account? [Y]es/[N]o => ").lower()
        if newUser == "y":
            continue
        else:
            print("Account details:")
            for i in users:
                print(i)
            break
    else:
        while True:
            password = input("Please enter a new Password ")
            if len(password) < 7:
                print("Please enter a password of 7 or more characters")
                continue
            else:
                userDetails = {username: {
                    'firstname': firstName, 'lastname': lastName,  'email': email, 'password': password}}
                users.append(userDetails)
                print(users[-1])
                newUser = input(
                    "Do you want to enter another user? [Y]es/[N]o => ").lower()
                if newUser == "y":
                    continue
                else:
                    print("Account details:")
                    for i in users:
                        print(i)
                    break
        break
