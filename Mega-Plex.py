import time

logged_in = False
admin = False
login_attemps = 0

users= [["admin", "admin123", True],
        ["customer", "customer123", False]]

CINEMA_NAME = "Mega-Plex"

while login_attemps < 3:
    login_user = str(input("Enter your username:"))
    time.sleep(1)
    login_pass = str(input("Enter your password:"))

    for user in users:
        if (login_user in user[0]) and (login_pass in user[1]):
            admin = user[2]
            
        else:
            login_attemps += 1
            print(f"Incorrect username or password. {login_attemps}/3 login attemps used.")
