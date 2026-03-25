def get_pounds():
    gbp_amount = "{:.2f}".format(float(input("How many GBP do you have?")))
    return gbp_amount

def convert_to_euro(gpb):
    converted_eur = "{:.2f}".format(float(gbp) * 1.15)
    return converted_eur

gbp = get_pounds()

print("€" + str(convert_to_euro(gbp)) + " EUR converted from £" + str(gbp) + " GBP")
