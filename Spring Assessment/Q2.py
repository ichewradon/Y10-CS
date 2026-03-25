num = int(input())
if not num > 1 or num > 20:
    print("False")
elif num > 1 and num < 15:
    print("Almost")
elif num % 5 == 0:
    print("True")
else:
    print("Unknown")
