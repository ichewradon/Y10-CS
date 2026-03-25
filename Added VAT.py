# subroutines to calculate the tax

def calculate_tax(price): # one parameter
    tax_amount = price * 0.2 # this calculates the tax_amount
    # arithemetic operator
    return tax_amount

# subroutine to calc final price
def final_bill(applied_tax): # two parameters
    total = "{:.2f}".format(applied_tax)
    return ("Total: £ " + str(total))

def calculate_double(price):
    double_amount = price * 2
    return double_amount

def apply_tax(double_amount):
    applied_tax = double_amount * 1.2
    return applied_tax

# main process
itemCost = float(input("Enter your starting amount:"))
double_amount = calculate_double(itemCost)
applied_tax = apply_tax(double_amount)
vat = calculate_tax(itemCost) # passes 50 into the subroutine calculate_tax - return 10
receipt = final_bill(applied_tax) # passes 50 and 10
print (receipt) # prints: total: £60
