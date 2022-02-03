#turn every item into capitals - 'element' can be called anything e.g. 'item', but just how it's known in the loop.
myList = ['apples', 'oranges', 'chocolate']
for element in myList:
    print(element.upper())

#what happens in for loop isn't performed on the collection but on a copy of it
#so when we print myList again, it stays as it is

print(myList)

#TO OVERRIDE

for position, item in enumerate(myList):
    myList[position] = item+item

print(myList)