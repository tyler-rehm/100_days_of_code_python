math_score = int(input("What math score did you receive?"))
english_score = int(input("What english score did you receive?"))

if math_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
elif english_score >= 90:
    print("You're good at english")


#
# BMI IF ELSE
#
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")