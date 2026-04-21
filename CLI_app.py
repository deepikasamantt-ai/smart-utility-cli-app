while True:
    menu = ["Basic Calculator","Check Odd/Even","Grade Checker","Login System","Exit"]
    # Display menu options
    for i in range(len(menu)):
        print(i + 1, menu[i])

    option =input("choose an option: ")

    if option == "1":
          number1 = float(input("enter the first number: "))
          number2 = float(input("enter the second number: "))
          print(f"sum of your numbers is: {number1 + number2}")
          print(f"product of your numbers is: {number1 * number2}")
          print(f"difference of your numbers is: {abs(number1 - number2)}")
          if number2==0:
              print ("division with 0 not possible")
          else:
             print(f"division of your numbers is:{number1 / number2}")

    elif option == "2":
            number = float(input("enter a number: "))
            if number % 2 == 0:
               print(f"{number} is even")
            else:
              print(f"{number} is odd")
    elif option == "3":
            marks = float(input("enter your marks: "))
            if marks > 100 or marks < 0:
               print("Invalid marks")
            elif marks >= 90:
              print("Grade: A")
            elif marks >= 75:
              print("Grade: B")
            elif marks >= 50:
              print("Grade: C")
            else:
              print("FAIL")
    elif option == "4":
                  correct_username="admin"
                  correct_password="1234"
                  username=input("enter your username: ")
                  password=input("enter your password: ")
                  if username == correct_username and password == correct_password:
                     print("Success")
                  else:
                    print("Invalid credentials")
    elif option == "5":
         print("Goodbye")
         break
    else:
         print("Invalid option")




