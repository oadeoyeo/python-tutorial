dollar_naira_rate = 1000
dollar_amount = input("Enter amount to be exchanged:\n")

def dollar_to_naira(dollars):
    print(f"The Naira equivalent of ${dollars} is N{dollars * dollar_naira_rate}")


print("Welcome to the Currency Converter!")
print(dollar_amount)
dollar_to_naira(250)
