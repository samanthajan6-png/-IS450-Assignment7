# name: Samantha Kaiser
# Description: Assignment 2 - Cybersecurity Login Challenge

correct_username = "Samantha"
correct_password = "Kaiser123"
chances = 3

while chances > 0:
    enterusername = input("Username: ")
    enterpassword = input("Password: ")

    if enterusername == correct_username:
        print("username accepted")
    else:
        print("username denied")

    if enterpassword == correct_password:
        print("password accepted")
    else:
        print("password denied")

    if enterusername == correct_username and enterpassword == correct_password:
        print("Access granted, welcome Samantha")
        break

    chances -= 1
    if chances > 0:
        print(f"You have {chances} chance(s) remaining")
    else:
        print("Access denied, you have no more chances left")
  