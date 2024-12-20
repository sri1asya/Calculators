#Currency Conversion Calculator
#Convert the USD into one of these currencies: MXN, EUR, GBP, CHF, JPY, KRW, CNY, or INR.
def usd_to_currency(usd, rate):
    return usd * rate

def currency_converter():
    rates = {"MXN": 20.4, "EUR": 0.94, "GBP": 0.78, "CHF": 0.88, "JPY": 154.03, "KRW": 1401.44, "CNY": 7.23, "INR": 84.4}

    print("USD Currency Converter")
    usd = float(input("Enter amount of USD: "))

    print("Choose a currency:")
    print("1. Mexican Peso (MXN)")
    print("2. Euro (EUR)")
    print("3. British Pound (GBP)")
    print("4. Swiss Franc (CHF)")
    print("5. Japanese Yen (JPY)")
    print("6. Korean Won (KRW)")
    print("7. Chinese Yuan (CNY)")
    print("8. Indian Rupee (INR)")

    choice = int(input("Choice (1-8): "))

    codes = list(rates.keys())

    if 1 <= choice <= 8:
        selection = codes[choice - 1]
        rate = rates[selection]
        converted = usd_to_currency(usd, rate)
        print(f"{usd} USD is equivalent to {converted:.2f} {selection}")
    else:
        print("Please select a number between 1 and 8.")
        currency_converter

currency_converter()
