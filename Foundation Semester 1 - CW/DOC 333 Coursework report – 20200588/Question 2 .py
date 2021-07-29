# Import math library for calculating Square

import math

# Creating Variables

coefficientOfX2 = 0
coefficientOfX = 0
constantValue = 0
i = ''

# Repatition Part

while (i != 'X'):

    #to get only integer as user input. If you input string then you will get a error msg and program will start again
    while True:
        try:
            # Input Part - Get Input From User
            coefficientOfX2 = int(input("Enter the Coefficient Of X2\t: "))
            coefficientOfX = int(input("Enter the Coefficient Of X\t: "))
            constantValue = int(input("Enter the constant Value\t: "))
        except ValueError:
            print("Integer Required!! Please Enter the Number Again")

        else:
            # Calculate the discriminant part of the quadratic equation

            partOfTheQuadraticEquation = coefficientOfX ** 2 - 4 * coefficientOfX2 * constantValue

            # Calculate and Display Roots only if partOfTheQuadraticEquation is equal to zero.

            if partOfTheQuadraticEquation == 0:

                # Output
                print("")
                print("The discriminant is zero -> There are two real identical roots")
                # Calculation to get Root
                Root_x = int(((-coefficientOfX) / (2 * coefficientOfX2)))
                 # Output - if the input coefficient of X is possitive
                if coefficientOfX > 0:
                    #ourput - if the coefficient of X2 is one
                    if coefficientOfX2 == 1:
                        print("")
                        print("The roots of", "𝒙𝟐", "+", coefficientOfX, "𝒙", "+", constantValue,"= 0 are", Root_x, "and", Root_x)
                    else:
                        print("")
                        print("The roots of", coefficientOfX2, "𝒙𝟐", "+", coefficientOfX, "𝒙", "+", constantValue, "= 0 are", Root_x, "and", Root_x)
                # Output - if the input coefficient of X is negative
                else:
                    if coefficientOfX2 == 1:
                        print("")
                        print("The roots of", "𝒙𝟐", coefficientOfX, "𝒙", "+", constantValue, "= 0 are", Root_x,
                              "and", Root_x)
                    else:
                        print("The roots of", coefficientOfX2, "𝒙𝟐", coefficientOfX, "𝒙", "+", constantValue,"= 0 are", Root_x, "and", Root_x)


            # Calculate and Display Roots only if partOfTheQuadraticEquation is greater than zero

            elif partOfTheQuadraticEquation > 0:

                # Output
                print("")
                print("The discriminant is grater than zero -> There are two real roots")
                # Calculation to get roots
                Root_x1 = int(((-coefficientOfX) + math.sqrt(partOfTheQuadraticEquation)) / (2 * coefficientOfX2))
                Root_x2 = int(((-coefficientOfX) - math.sqrt(partOfTheQuadraticEquation)) / (2 * coefficientOfX2))
                # Output - if the input coefficient of X is positive
                if coefficientOfX > 0:
                    if coefficientOfX2 == 1:
                        print("")
                        print("The roots of", "𝒙𝟐", "+", coefficientOfX, "𝒙", "+", constantValue,"= 0 are", Root_x2, "and", Root_x1)
                    else:
                        print("")
                        print("The roots of",coefficientOfX2, "𝒙𝟐", "+", coefficientOfX, "𝒙", "+", constantValue,"= 0 are", Root_x2, "and", Root_x1)
                # Output - if the input coefficient of X is negative
                else:
                    #ourput - if the coefficient of X2 is one
                    if coefficientOfX2 == 1:
                        print("")
                        print("The roots of", "𝒙𝟐", coefficientOfX, "𝒙", "+", constantValue, "= 0 are",Root_x2, "and", Root_x1)
                    else:
                        print("The roots of", coefficientOfX2,"𝒙𝟐", coefficientOfX, "𝒙", "+", constantValue, "= 0 are", Root_x2, "and", Root_x1)

                # Display the Message if partOfTheQuadraticEquation is less than zero

            else:
                print("")
                print("The discriminant is less than zero -> There are no real roots")

        i = input("Enter 'X' to exit / or press any key to continue the program again ")
        if i == 'X':
            break
        print("Your input:", i)

print("The Program Is End")


