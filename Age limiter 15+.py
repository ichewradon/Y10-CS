valid_input = False

while not valid_input:
    try:
        age = int(input("Please enter your name as a number: "))
        valid_input = True
    except ValueError:
        print("That wasn't a number! Please try again.")

print(f"Thank you, you entered: {age}")
