
# 1. Functions
def calculator():
    number1 = float(input("enter the first number: "))
    number2 = float(input("enter the second number: "))
    print(f"sum: {number1 + number2}")
    print(f"difference: {abs(number1 - number2)}")
    print(f"product: {number1 * number2}")
    if number2 == 0:
        print("division with 0 not possible")
    else:
        print(f"division: {number1 / number2}")
def check_even_odd():
    number = int(input("enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
def grade_checker():
    marks = float(input("enter your marks: "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("FAIL")
def login_system():
    correct_username = "admin"
    correct_password = "1234"
    attempts=0
    while attempts < 3:
        username = input("enter your username: ")
        password = input("enter your password: ")
        if username == correct_username and password == correct_password:
           print("Success")
           break
        else:
           print("Invalid credentials")
           attempts = attempts + 1
    if attempts == 3:
        print("Account Locked")
def show_menu():
    menu = ["Basic Calculator", "Check Odd/Even", "Grade Checker", "Login System", "Exit"]
    ## Display menu options
    for i in range(len(menu)):
        print(i + 1, menu[i])
    option = input("choose an option: ")
    return option
# 2. Main loop
while True:
    option = show_menu()
    if option == "1":
        calculator()
    elif option == "2":
        check_even_odd()
    elif option == "3":
        grade_checker()
    elif option =="4":
        login_system()
    elif option =="5":
        print("Goodbye")
        break
    else:
        print("Invalid option")




