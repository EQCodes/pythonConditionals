import math
print("Hello! I'm Florence the Funky Calculator.")
# add that if they input Q at any time they can quit
begin = True

while begin:
    nums = input("Enter as many numbers as you like separated by a space: ")
    operator = input("Enter an operator (+, -, * or /): ")
    numsList = nums.split(' ')
    numsList = [int(x) for x in numsList]
    if operator == "*":
        print("Sweet, the total of your numbers multiplied together is", math.prod(numsList))
    elif operator == "+":
        print("Awesome, the total of your numbers added together is", sum(numsList))
    elif operator == "/":
        print("I haven't figured out how to divide yet, sorry pal.")
        #t ried using a for loop and accessing the next index of the list but got stuck
        # dividedList = []
        # dividedList.append(numsList[0])
        # for number, elem in enumerate(numsList):
        #     if (number+1 < len(numsList)):
        #         num1 = elem
        #         num2 = numsList[number+1]
        #         dividedList.append(num1/num2)
        # print(dividedList)
    elif operator == "-":
        print("I haven't figured out how to takeaway yet, sorry pal.")
    else:
        print("Please only use one of these operators: *, +, -, /")

    goAgain = input("Wanna try again? Type 'Q' to stop or press Enter to have another go: ")
    if goAgain == 'Q':
        begin = False