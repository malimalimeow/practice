def password_checker():
    while True:
        pw = input("Check your password: ")

        if len(pw) < 8 or not any(c.isupper() for c in pw):
            print("Password is not safe!")
        else:
            print("Nice one!")
            break

password_checker()