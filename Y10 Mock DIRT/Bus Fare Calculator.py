fare = 2.50
under_16s = 1.50

while input("Age or Quit").lower() != "quit":
    age = int(input("Age: "))
    if age < 16:
        print("Fare: £" + str(under_16s))
    else:
        print("Fare: £" + str(fare))

else:
    print("Goodbye")