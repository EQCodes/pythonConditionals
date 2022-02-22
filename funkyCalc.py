import math
from functools import reduce
print("*~* Hello! I'm Florence the Funky Calculator *~*")
print("*~* Using a little bit of magic, I'll take a mathematical operator and apply it cumulatively \n to a list of numbers to give you one final, shiny result *~*")
begin = True
goAgain = ''
#userTracking = open('userFile.txt', mode="a")
#counter = 0

while goAgain != 'Q':
    #counter += 1
    nums = input("Enter as many numbers as you like separated by a space: ")
    operator = input("Enter an operator (+, -, * or /): ")
    numsList = nums.split(' ')
    numsList = [int(x) for x in numsList]
    if operator == "*":
        print("Sweet, lets multiply all of those together! Here's your calcuation:", end=" ")
        print(*numsList, sep="*", end=" ")
        print("=", round(math.prod(numsList), 2))
    elif operator == "+":
        print("Awesome, you chose to get the sum of those numbers! Check it out:", end=" ")
        print(*numsList, sep="+", end=" ")
        print("=", round(sum(numsList), 2))
    elif operator == "/":
        if 0 in numsList:
            print("You cannot divide by 0, give it another go - no 0 this time!")
            continue
        def divideAll(num1, num2):
            result = num1 / num2
            return result
        print("Nice, we divided all of those together and this is what happened:", end=" ")
        print(*numsList, sep="/", end=" ")
        print("=", round(reduce(divideAll, numsList), 2))
    elif operator == "-":
        def subtractAll(a, b):
            result = a - b
            return result
        print("Great, subtracting all of your numbers together looks like this:", end=" ")
        print(*numsList, sep="-", end=" ")
        print("=", round(reduce(subtractAll, numsList), 2))
    else:
        print("Please only use one of these operators: *, +, -, /")

    goAgain = input("Wanna try again? Type 'Q' to stop or press Enter to have another go: ")