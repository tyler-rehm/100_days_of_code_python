for number in range(1, 10):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
