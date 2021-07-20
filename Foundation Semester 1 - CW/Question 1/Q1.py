


while True:
    value= int(input("Please Enter the Amount: "))

    print("\n(To convert to word representation enter ‘W’, to convert to USD currency enter ‘C’)\n")
    option = input("Please Enter your Option: ")

    if option == 'w' or 'W':
        one = ["", "one ", "two ", "three ", "four ",
               "five ", "six ", "seven ", "eight ",
               "nine ", "ten ", "eleven ", "twelve ",
               "thirteen ", "fourteen ", "fifteen ",
               "sixteen ", "seventeen ", "eighteen ",
               "nineteen "]

        ten = ["", "", "twenty ", "thirty ", "forty ",
               "fifty ", "sixty ", "seventy ", "eighty ",
               "ninety "]

        tens_power = ["hundred", "thousand"]



        out1 = value % 10
        out = value // 10
        out2 = value // 100
        out3 = (value % 100) // 10
        out4 = (value % 100) % 10
        out5 = (value // 1000) // 10
        out6 = (value // 1000) % 10
        out7 = (value % 1000) // 100
        out8 = ((value % 1000) % 100) // 10
        out9 = ((value % 1000) % 100) % 10

        if value <= 19:
            print(one[value])
        elif 20 <= value <= 99:
            print(ten[out], "", one[out1])
        elif 100 <= value <= 999:
            print(one[out2], "", tens_power[0], "", ten[out3], "", one[out4])
        elif 1000 <= value <= 99999:
            res = [int(x) for x in str(value)]
            if res[2] != 0:
                print(ten[out5], '', one[out6], '', tens_power[1], '', one[out7], '', tens_power[0], "and", ten[out8],
                      "",
                      one[out9])
            else:
                print(ten[out5], '', one[out6], '', tens_power[1], "", ten[out8], "", one[out9])
    elif option != "w" or "W":
        amountInUSD = value / 200.00
        print("Result: ", "USD ", round(amountInUSD))


    c = input("Want to Exit Press y : ")
    if c == 'y':
        break