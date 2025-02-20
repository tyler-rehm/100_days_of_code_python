# 100 Days of Code: Day 1 - Band Name Generator Project
# Developer: Tyler Rehm

print("Welcome to the Band Name Generator!")
print("Are you ready? Let's begin!")

# Capitalize each word in the city name
city = input("What city were you born in? ").title()

print("Very well. Now let's see if you can answer my next question.")
pet = input("What kind of pet do you have (e.g. dog, cat)? ").title()

# Simple pluralization rules
if not pet.endswith("s"):  # Avoid adding 's' if already plural
    if pet.endswith(("ch", "sh", "x", "s", "z")):
        pet_plural = pet + "es"  # e.g., fox → foxes, bus → buses
    elif pet.endswith("y") and pet[-2] not in "aeiou":
        pet_plural = pet[:-1] + "ies"  # e.g., puppy → puppies
    else:
        pet_plural = pet + "s"  # e.g., dog → dogs, cat → cats
else:
    pet_plural = pet  # Already plural

print(f"The {city} {pet_plural}!")

print("How do you like your new band name?")
