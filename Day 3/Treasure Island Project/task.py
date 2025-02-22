print(r'''
*******************************************************************************
                  ,
               ,  ;:._.-`''.
             ;.;'.;`      _ `.
              ',;`       ( \ ,`-.  
           `:.`,         (_/ ;\  `-.
            ';:              / `.   `-._
          `;.;'              `-,/ .     `-.
          ';;'              _    `^`       `.
         ';;            ,'-' `--._          ;
':      `;;        ,;     `.    ':`,,.__,,_ /
 `;`:;`;:`       ,;  '.    ;,      ';';':';;`
              .,; '    '-._ `':.;    
            .:; `          '._ `';;,
          ;:` `    :'`'       ',__.)
        `;:;:.,...;'`'
      ';. '`'::'`''  .'`'
    ,'   `';;:,..::;`'`'
, .;`      `'::''`
,`;`.
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice
choice1 = input("You are at a crossroad. Do you want to go left or right? ").strip().lower()
if choice1 not in ["left", "l"]:
    print("You fell into a hole. Game Over.")
    exit()

# Second choice
choice2 = input("You've come to a lake. Do you swim or wait? ").strip().lower()
if choice2 not in ["wait", "w"]:
    print("You were attacked by a trout. Game Over.")
    exit()

# Third choice
choice3 = input("You arrive at three doors: Red, Blue, or Yellow. Which one do you choose? ").strip().lower()
if choice3 in ["red", "r"]:
    print("Burned by fire. Game Over.")
elif choice3 in ["blue", "b"]:
    print("Eaten by beasts. Game Over.")
elif choice3 in ["yellow", "y"]:
    print("Congratulations! You found the treasure! You Win!")
else:
    print("Invalid choice. Game Over.")