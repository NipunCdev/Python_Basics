number = [0,20,40,60,80,100,120]

def passValidation():
    while True:
        try:
            global creditsAtPass
            creditsAtPass = int(input("Enter your credits at pass: "))

        except ValueError:
            print("Integer required")
            continue
        else:
            if (creditsAtPass in range(0,140,20)):
                deferValidation()
                break
            elif creditsAtPass not in range(0,140,20):
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
            if (creditsAtDefer in range(0,140,20)):
                failValidation()
                break
            elif creditsAtDefer not in range(0,140,20):
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
            if (creditsAtFail in range(0,140,20)):
                progress_outcome(creditsAtPass,creditsAtDefer,creditsAtFail)
                break
            elif creditsAtFail not in range(0,140,20):
                print("Out of Range")
                break

def progress_outcome(creditsAtPass, creditsAtDefer, creditsAtFail):
    totalCredits = creditsAtPass + creditsAtDefer + creditsAtFail
    if totalCredits > 120:
        print("Total incorrect")
        passValidation()
    elif creditsAtPass == 120:
        print("Progress")
    elif creditsAtPass == 100:
        print("Progress (module trailer)")
    elif creditsAtPass == 80:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 60:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 40:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 40 and creditsAtDefer== 80:
        print("Exclude")
    elif creditsAtPass == 20:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 20 and creditsAtDefer == 20 or creditsAtDefer == 0:
        print("Exclude")
    elif creditsAtPass == 0:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 0 and creditsAtDefer == 0 or creditsAtDefer == 20 or creditsAtDefer == 40:
        print("Exclude")

passValidation()

