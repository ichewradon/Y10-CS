def withdraw_cash(balance, amount):
    new_balance = balance - amount
    return new_balance

current_bal = 500

while True:
    # Main logic
    print("")
    request = int(input("How much would you like to withdraw? "))

    try:
        if request > 0 and request < 250 and request < current_bal:
            current_bal = withdraw_cash(current_bal, request)
            
        elif request <= 0 or request > 250:
            print("Enter a valid withdrawal amount in the daily limit (£0-£250)")

    except:
        print(f"Your balance isn't high enough to take out £{request}")

    print(f"New balance: £{current_bal}")
