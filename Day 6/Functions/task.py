def my_function(string):
    num_char = len(string)
    print(num_char)

my_function("Hello")

# REEBORGS WORLD MAZE EXERCISE
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()