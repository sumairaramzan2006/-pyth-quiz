rates = {
    "USD": 1,
    "EUR": 0.85,
    "GBP": 0.75,
    "PKR": 285
}

amount = float(input("Enter amount in USD: "))
currency = input("Enter currency (USD, EUR, GBP, PKR): ").upper()

if currency in rates:
    converted = amount * rates[currency]
    print("Converted Amount =", converted, currency)
else:
    print("Invalid Currency")