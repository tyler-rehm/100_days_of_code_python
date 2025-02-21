#
# Type Error, Checking and Conversion
#

# String
print(type("abc"))

# Integer Type
print(type(123))

# Float
print(type(3.14))

# Bool
print(type(True))

#
# Type Casting
#
print(type(int("123")))
print(type(float("123.123")))
print(type(str(123.123)))
print(type(bool(1)))

#
# Challege
#

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print("Number of letters in your name: " + str(length_of_name))