#Creating Varibles

value = 0
UserInput =0
i =''

#Repatition Part
while (i !='X'):
    while True:
        try:
            # Input Part - Get Input From User 
            value = int(input("Please Enter the Amount: "))
            #Check the input is Integer or String
        except ValueError:
            print("Integer Required!! Please Enter the Number Again")

        else:
            # Get Input From User


            # Get option as a input from user
            print("\n(To convert to word representation enter ‘W’, to convert to USD currency enter ‘C’)\n")
            UserInput = input("Please Enter your Option: ")

            # If User input the "C" then print the USD Value
            if UserInput == "C":
                amountInUSD = value / 200.00
                print("Result: ", "USD ", round(amountInUSD))
                i = input("Enter 'X' to exit / or press any key to continue the program again ")
                if i == 'X':
                    break
                print("Your input:", i)

            # If user input the "W" then print the word of the  Numbr that is input from user
            elif UserInput == 'W':

                # List 1 - 1 to 19
                one_list = ["", "one ", "two ", "three ", "four ",
                            "five ", "six ", "seven ", "eight ",
                            "nine ", "ten ", "eleven ", "twelve ",
                            "thirteen ", "fourteen ", "fifteen ",
                            "sixteen ", "seventeen ", "eighteen ",
                            "nineteen "]

                # List 2
                ten_list = ["", "", "twenty ", "thirty ", "forty ",
                            "fifty ", "sixty ", "seventy ", "eighty ",
                            "ninety "]

                # List 3
                tens_power_list = ["hundred", "thousand"]

                # Calculation Part to get index

                calculate = value // 10
                calculate_1 = value % 10
                calculate_2 = value // 100
                calculate_3 = (value % 100) // 10
                calculate_4 = (value % 100) % 10
                calculate_5 = (value // 1000)
                calculate_6 = (value % 1000) // 100
                calculate_7 = (value % 100) // 10
                calculate_8 = (value % 100) % 10
                calculate_9 = (value % 100)
                calculate_10 = (value % 1000) % 10
                calculate_11 = (value % 1000)
                calculate_12 = (value // 10000)
                calculate_13 = (value % 10000) // 1000
                calculate_14 = (value % 100)

                # For loop that make the input number as List
                res = [int(x) for x in str(value)]

                # If input number is grater than 100000 then print the Errir message
                if value >= 100000:
                    print("Value Is Invalid")


                elif value <= 19:
                    print(one_list[value])
                elif 20 <= value <= 99:
                    print(ten_list[calculate], "", one_list[calculate_1])
                elif 100 <= value <= 999:
                    if res[1] == 1:
                        print(one_list[calculate_2], tens_power_list[0], one_list[calculate_9])
                    else:
                        print(one_list[calculate_2], tens_power_list[0], "", ten_list[calculate_3], "",
                              one_list[calculate_4])
                elif 1000 <= value <= 9999:

                    if res[1] == 0:
                        if res[2] == 1:
                            print(one_list[calculate_5], tens_power_list[1], one_list[calculate_6],
                                  one_list[calculate_9])
                        else:
                            print(one_list[calculate_5], tens_power_list[1], ten_list[calculate_7],
                                  one_list[calculate_8])
                    else:
                        if res[2] == 1:
                            print(one_list[calculate_5], tens_power_list[1], one_list[calculate_6], tens_power_list[0],
                                  one_list[calculate_9])
                        else:
                            print(one_list[calculate_5], tens_power_list[1], one_list[calculate_6], tens_power_list[0],
                                  ten_list[calculate_7], one_list[calculate_8])
                elif 10000 <= value <= 99999:
                    if res[2] == 0:
                        if res[0] == 1:
                            if res[3] == 1:
                                print(one_list[calculate_5], tens_power_list[1], one_list[calculate_11])
                            else:
                                print(one_list[calculate_5], tens_power_list[1], ten_list[calculate_7],
                                      one_list[calculate_10])
                        else:
                            if res[3] == 1:
                                print(ten_list[calculate_12], one_list[calculate_13], tens_power_list[1],
                                      one_list[calculate_11])
                            else:
                                print(ten_list[calculate_12], one_list[calculate_13], tens_power_list[1],
                                      ten_list[calculate_7], one_list[calculate_10])
                    else:
                        if res[0] == 1:
                            if res[3] == 1:
                                print(one_list[calculate_5], tens_power_list[1], one_list[calculate_6],
                                      tens_power_list[0], one_list[calculate_14])
                            else:
                                print(one_list[calculate_5], tens_power_list[1], one_list[calculate_6],
                                      tens_power_list[0], ten_list[calculate_7], one_list[calculate_10])
                        else:
                            if res[3] == 1:
                                print(ten_list[calculate_12], one_list[calculate_13], tens_power_list[1],
                                      one_list[calculate_6], tens_power_list[0], one_list[calculate_11])
                            else:
                                print(ten_list[calculate_12], one_list[calculate_13], tens_power_list[1],
                                      one_list[calculate_6], tens_power_list[0], ten_list[calculate_7],
                                      one_list[calculate_10])

        i = input("Enter 'X' to exit / or press any key to continue the program again ")
        if i == 'X':
            break
        print("Your input:", i)

print("The Program Is End")
