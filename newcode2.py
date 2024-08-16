# This is a program for Dollar to Naira conversion


dollar_to_naira_rate = input("Enter the current dollar to naira rate:\n ")
trans_amt = input("Enter amount to be exchanged:\n ")


def dollar_to_naira(dollar_amount, dollar_naira_rate):
        return f"${dollar_amount} at todays exchange rate is equals to N{dollar_amount * dollar_naira_rate}"


def validate_and_execute():
    if trans_amt.isdigit():
        trans_amt_number = int(trans_amt) # Converts the string input to an integer

        if dollar_to_naira_rate.isdigit():
            dollar_naira_rate = int(dollar_to_naira_rate) # Converts the string input to integer

            if dollar_naira_rate > 0:
                if trans_amt_number > 0:
                    # Call the function to do the conversion
                    result = dollar_to_naira(trans_amt_number, dollar_naira_rate)
                    print(result)
                elif trans_amt_number == 0:
                    print("You have entered no amount. Nothing to convert.")
            elif dollar_naira_rate == 0:
                print("Exchange rate cannot be zero. Valid amount is required for conversion.")
                
        else:
            print("You have provided an invalid input!")

    else:
        print("You have provided an invalid input!")


validate_and_execute()