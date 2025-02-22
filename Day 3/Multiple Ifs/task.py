print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))
bill = 0

if height >= 48:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("You tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken (Y/N)").capitalize()

    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
