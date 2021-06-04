progressCount = 0
trailerCount = 0
excludeCount = 0
retrieveCount = 0

def passValidation():
    while True:
        try:
            global creditsAtPass
            creditsAtPass = int(input("Enter your credits at pass: "))

        except ValueError:
            print("Integer required")
            continue
        else:
            if (creditsAtPass in range(0, 140, 20)):
                deferValidation()
                break
            elif creditsAtPass not in range(0, 140, 20):
                print("Out Of Range")


def deferValidation():
    while True:
        try:
            global creditsAtDefer
            creditsAtDefer = int(input("Enter your credits at defer: "))

        except ValueError:
            print("Integer required")
            continue
        else:
            if (creditsAtDefer in range(0, 140, 20)):
                failValidation()
                break
            elif creditsAtDefer not in range(0, 140, 20):
                print("Out of Range")


def failValidation():
    while True:
        try:
            global creditsAtFail
            creditsAtFail = int(input("Enter your credits at fail: "))

        except ValueError:
            print("Integer required")
            continue
        else:
            if (creditsAtFail in range(0, 140, 20)):
                progress_outcome(creditsAtPass, creditsAtDefer, creditsAtFail)
                break
            elif creditsAtFail not in range(0, 140, 20):
                print("Out of Range")
                break


def progress_outcome(creditsAtPass, creditsAtDefer, creditsAtFail):
    global progressCount, trailerCount, retrieveCount, excludeCount

    totalCredits = creditsAtPass + creditsAtDefer + creditsAtFail
    if totalCredits > 120:
        print("Total incorrect")
        passValidation()
    elif creditsAtPass == 120:
        print("Progress")
        progressCount += 1


    elif creditsAtPass == 100:
        print("Progress (module trailer)")
        trailerCount += 1


    elif creditsAtPass == 80:
        print("Do not Progress – module retriever")
        retrieveCount += 1

    elif creditsAtPass == 60:
        print("Do not Progress – module retriever")
        retrieveCount += 1

    elif creditsAtPass == 40:
        print("Do not Progress – module retriever")
        retrieveCount += 1

    elif creditsAtPass == 40 and creditsAtDefer == 80:
        print("Exclude")
        exclude_count += 1

    elif creditsAtPass == 20:
        print("Do not Progress – module retriever")
        retrieveCount += 1

    elif creditsAtPass == 20 and creditsAtDefer == 0 or creditsAtDefer == 20:
        print("Exclude")
        exclude_count += 1

    elif creditsAtPass == 0:
        print("Do not Progress – module retriever")
        retrieveCount += 1


    elif creditsAtPass == 0 and creditsAtDefer == 0 or creditsAtDefer == 20 or creditsAtDefer == 40:
        print("Exclude")
        excludeCount += 1


def enter():  
    global studentCount
    
    print('progress', progressCount, ':', progressCount * '*')
    print('tailer  ', trailerCount, ':', trailerCount * '*')
    print('retailer', retrieveCount, ':', retrieveCount * '*')
    print('exclude ', excludeCount, ':', excludeCount * '*')
    studentCount = progressCount + trailerCount + retrieveCount + excludeCount
    print('student count is ', studentCount, '.')


print('**STAFF VERSION**')
userInput = int(input('Enter 1 to Start The Program \nEnter 0 To Start The Program \n'))  # start the program
if (userInput == 1):
    passValidation()
    userInput2 = 0
    while (userInput2 != 'q'):
        userInput2= (
            input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:"))
        if (userInput2 == 'q'):
            userInput3= (input(' Press s for summary \n press any button for exit\n'))
            if (userInput3 == 's'):
                enter()
            else:
                print('End Of The Program')
        else:
            passValidation()
else:
    print("Error , Start Again ")
