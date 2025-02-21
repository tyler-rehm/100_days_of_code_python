#
# F Strings
#

height = float(input("Enter your height (in): "))
weight = int(input("Enter your weight (lbs): "))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height ** 2)) * 703

print(f"Your BMI: {bmi}")

print(6 + 4 / 2 - (1 * 2))
print(type(int("5") / int(2.7)))