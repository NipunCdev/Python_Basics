def progressOutcome(creditsAtPass, creditsAtDefer):
    if creditsAtPass == 120:
        print("Progress")
    elif creditsAtPass == 100:
        print("Progress (module trailer)")
    elif creditsAtPass == 80:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 60:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 40:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 40 and creditsAtDefer == 80:
        print("Exclude")
    elif creditsAtPass == 20:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 20 and creditsAtDefer == 20 or creditsAtDefer == 0:
        print("Exclude")
    elif creditsAtPass == 0:
        print("Do not Progress – module retriever")
    elif creditsAtPass == 0 and creditsAtDefer == 0 or creditsAtDefer == 20 or creditsAtDefer == 40:
        print("Exclude")


print(" ::WELCOME:: ")
creditsAtPass = int(input("Enter The Pass Credits : "))
creditAtDefer = int(input("Enter The Defer Credits: "))
creditsAtFail = int(input("Enter The Defer Credits: "))
progressOutcome(creditsAtPass, creditAtDefer)
