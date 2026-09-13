"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and 
an amount. It prints out the result of converting the first currency to 
the second.

Author: Richard Li rl998 Joon LeeJL4875
Date:   Sept 10
"""

import a1

currency1 = input("Enter original currency: ")
currency2 = input("Enter desired currency: ")
amount = input("Enter original amount: ")
a = float(amount)

exchanged_amount = a1.exchange(currency1, currency2, a)
print("You can exchange " + str(amount) + " " + currency1 + " for " + str(exchanged_amount) + " " + currency2)