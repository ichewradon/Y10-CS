def diffCurrencies(x):
    currencies = ["Baht", "Dollar", "Euro", "Koruna", "Lira", "Rand", "Rupee", "Yen"]
    return currencies[x]

for i in range(7, -1, -1):
    print(diffCurrencies(i))
    
