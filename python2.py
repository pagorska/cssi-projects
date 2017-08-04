from random import randint
randLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
randNums = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']
# def passwordGen():
#     password = ""
#     n = 0
#     while n < 8:
#         x = randint(0, 2)
#         if (x == 0):
#             password += randLetters[randint(0, len(randLetters)-1)]
#         elif (x == 1):
#             password += (randLetters[randint(0, len(randLetters)-1)]).upper()
#         else:
#             password += randNums[randint(0, len(randNums)-1)]
#         n +=1
#     print password
#
def passwordGen():
    password = ""
    for i in range(8):
        x = randint(0, 2)
        if (x == 0):
            password += randLetters[randint(0, len(randLetters)-1)]
        elif (x == 1):
            password += (randLetters[randint(0, len(randLetters)-1)]).upper()
        else:
            password += randNums[randint(0, len(randNums)-1)]
    print password

def groceriesList():
    x = int(raw_input("List how many groceries you need to buy: "))
    groceries = []
    for index in range(x):
        item = raw_input('Enter item #%s: '%(index+1))
        y = int(raw_input("How much do you want? "))
        for i in range(y):
            groceries.append(item)
    item_count = 0
    num_count = 1
    item = ""
    for ix in range(len(groceries)):
        if (ix == 0):
            item = groceries[ix]
            item_count = 1
        elif (groceries[ix] == item):
            item_count +=1
        else:
            print "%s. %s : %s"%(num_count,item,item_count)
            item = groceries[ix]
            item_count = 1
            num_count += 1
    print "%s. %s : %s"%(num_count,item,item_count)

groceriesList()

def numGuesser():
    randNum = randint(0, 100)
    guess = int(raw_input("What is your guess? 0 to 100: "))
    guesses = 1
    while (guess != randNum):
        guesses +=1
        if (guess < randNum):
            guess = int(raw_input("The number is higher than your guess. Guess again: "))
        else:
            guess = int(raw_input("The number is lower than your guess. Guess again: "))
    print "Correct! The number is " + str(randNum)
    print "It took you ",
    if (guesses == 1):
        print "1 guess"
    else:
        print str(guesses) + " guesses"
numGuesser()

def randList(maxL): #missing a number
    randNum = randint(1, maxL)
    listo = []
    for i in range(maxL):
        if ((i+1)!=randNum):
            listo.append(i+1)
    print randNum
    return listo


def missingNum(numList):
    for i in range(len(numList)):
        if ((i+1)!=numList[i]):
            print "The missing number is " + str(i+1)
            break

li = randList(100)
missingNum(li)

#groceriesList()
# # for index in range(len(groceries)):
# #     print '%s. %s' %(index + 1, groceries[index])
#
# listX = groceriesList();
# for index in range(len(listX)):
#     print listX[index]
#
# #passwordGen()
