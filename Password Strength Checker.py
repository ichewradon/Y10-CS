import string
from playsound import playsound

enter = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\enter a password.mp3"'
short = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\too short.mp3"'
missing = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\your missing.mp3"'
strong = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\strong.mp3"'
upper = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\upper.mp3"'
lower = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\lowercase.mp3"'
number = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\numbers.mp3"'
symbols = '"C:\Users\JamesWilkes(WHS-Year\CS Y10\Password Strength Checker\symbols.mp3"'

def check_strength():
    password = input("Enter a password 8-16 characters long: ")
    playsound(enter)

    if not 8 <= len(password) <= 16:
        print("Password should be between 8-16 characters.")
        playsound(short)
        check_strength()

    upper = False
    lower = False
    number = False
    symbol = False

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            number = True
        elif char in string.punctuation:
            symbol = True

    if upper and lower and number and symbol:
        print("You have a strong password.")
        playsound(strong)
        check_strength()
    else:
        print("Password is not strong you're missing: ")
        playsound(missing)
        if not upper:
            print("Uppercase Letters")
            playsound(upper)
        if not lower:
            print("Lowercase Letters")
            playsound(lower)
        if not number:
            print("Numbers")
            playsound(number)
        if not symbol:
            print("Symbols")
            playsound(symbols)
        check_strength()

check_strength()
