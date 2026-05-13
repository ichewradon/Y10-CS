password_attempt = ""
correct_password = "StudyTime2026"
attempts = 0

while attempts < 3 and password_attempt != correct_password:
    password_attempt = input("Enter password: ")
    attempts = attempts + 1

    if password_attempt == correct_password:
        print("Access granted!")
        for i in range(3):
            print("Loading system...")
    else:
        print("Incorrect. Try again.")

if password_attempt != correct_password:
    print("Account locked.")