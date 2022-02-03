num1 = float(input("Give me number 1: "))
num2 = float(input("Give me number 2: "))
operator = input("Give me an operator: ")

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