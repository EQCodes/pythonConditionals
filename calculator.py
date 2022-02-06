print("Hello! I'm Cal the Calculator.")
# Edit - didn't make begin take a user input, just set as true
#begin = input("Type anything to have a go: ")
begin = True

while begin:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    operator = input("Enter an operator (+, -, * or /): ")
# Q: ^^^ is there a way to ask for a user to input just a sum e.g. 5+5, 6*7
    if operator == "+":
        print("The result is " + str(round(num1+num2, 2)))
    elif operator == "-":
        print("The result is " + str(round(num1-num2, 2)))
    elif operator == "*":
        print("The result is " + str(round(num1*num2, 2)))
    elif operator == "/":
        print("The result is " + str(round(num1/num2, 2)))
    else:
        print("Error. Please input a +, -, / or * sign.")
        continue

    goAgain = input("Wanna try again? Type 'Q' to stop or press Enter to have another go: ")
    if goAgain == 'Q':
         break
    # ^^^ NB: simplified this from a full if else statement with break and continue etc.


