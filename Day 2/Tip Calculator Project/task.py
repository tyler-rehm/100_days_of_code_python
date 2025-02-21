#
# Tip Calculator
#
from typing import final

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
tip_amount = bill * tip_as_percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
bill_per_person_rounded = round(bill_per_person, 2)

print(f"Each person should pay ${bill_per_person_rounded}")
print(type(bill), type(tip), type(people))