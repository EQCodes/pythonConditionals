print("Hello! I'm Cal the Calculator.")
begin = input("Type anything to have a go: ")

while begin:
    num1 = float(input("Give me your first number: "))
    num2 = float(input("Give me your second number: "))
    operator = input("Give me an operator (+, -, * or /): ")


    if operator == "+":
        print("The result is " + str(round(num1+num2, 2)))
    elif operator == "-":
        print("The result is " + str(round(num1-num2, 2)))
    elif operator == "*":
        print("The result is " + str(round(num1*num2, 2)))
    elif operator == "/":
        print("The result is " + str(round(num1/num2, 2)))
    else:
        print("Please input a +, -, / or * sign.")

    response = input("Wanna try again? Type 'Quit' to stop or anything else to have another go: ")
    if response != 'Quit':
        continue
    else:
        break



