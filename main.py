# import funcy
# import math
# import fib
# import infodb
# import swap
# import keypad
# import tree
# import treeanim
# import catanim
# import ship
import src.week2.numbers
import src.week2.findprimes
import src.week2.fish
from src.week2.factors import Factor


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


main_menu = [
    ["Swap", "src/week0/swap.py"],
    ["Matrix", "src/week0/keypad.py"],
    ["Tree", "src/week0/tree.py"],
    ["Factorial", "src/week2/factorial.py"],
    ["Factors", "src/week2/factors.py"],
    ["Numbers", src.week2.numbers.color],
    ["Fish", src.week2.fish.printFish],

]


sub_menu = [
    ["Fibonacci", "src/week1/fib.py"],
    ["InfoDB", "src/week1/infodb.py"]
    # ["Cat", catanim.driver],
    # ["Ship", ship.driver],
    # ["Tree", treeanim.driver],
]

sub_menu1 = [
    ["Factorial", "src/week2/factorial.py"],
    ["Find Primes", src.week2.findprimes.primes],
    ["Find Factors Imperative", src.week2.factors.factors],
    # ["Find Factors OOP", src.week2.factors.OOP]
    
]

sub_menu2 = [
    ["Factorial", "src/week2/factorial.py"],
    ["Factors", "src/week2/factors.py"],
    ["Find Primes", src.week2.findprimes.primes]
]


# Menu banner is typically defined by menu owner


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control

def menu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(banner, options)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def submenu1():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu1)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again

def driver():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 1 Challenges", submenu])
    menu_list.append(["Week 2 Challenges", submenu1])
    menu(title, menu_list)

if __name__ == "__main__":
    driver()
