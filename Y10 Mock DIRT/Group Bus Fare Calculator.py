fare = 2.50
under_16s = 1.50

amount_under_16s = 0
amount_over_16s = 0

age1 = int(input("Age 1: "))
age2 = int(input("Age 2: "))
age3 = int(input("Age 3: "))
age4 = int(input("Age 4: "))

def calculateFareGroup(age1, age2, age3, age4):

    global amount_under_16s
    global amount_over_16s

    if age1 < 16:
        amount_under_16s += 1
    else:
        amount_over_16s += 1

    if age2 < 16:
        amount_under_16s += 1
    else:
        amount_over_16s += 1

    if age3 < 16:
        amount_under_16s += 1
    else:
        amount_over_16s += 1

    if age4 < 16:
        amount_under_16s += 1
    else:
        amount_over_16s += 1

    total_fare = ((amount_under_16s * under_16s) + (amount_over_16s * fare)) * 0.9
    print(f"Total Fare: £{total_fare:.2f}")

calculateFareGroup(age1, age2, age3, age4)