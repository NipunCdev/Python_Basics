# Import math library for calculating Square

import math

# Creating Variables

coefficientOfX2 = 0
coefficientOfX = 0
constantValue = 0

# Repatition Part

while True:

    # Input Part - Get Input From User

    coefficientOfX2 = int(input("Enter the Coefficient Of X2\t: "))
    coefficientOfX = int(input("Enter the Coefficient Of X\t: "))
    constantValue = int(input("Enter the constant Value\t: "))


    # Calculate the discriminant part of the quadratic equation

    partOfTheQuadraticEquation = coefficientOfX ** 2 - 4 * coefficientOfX2 * constantValue

    # Calculate and Display Roots only if partOfTheQuadraticEquation is equal to zero.

    if partOfTheQuadraticEquation == 0:

        # Output
        print("The discriminant is zero -> There are two real identical roots")
        # Calculation to get Root
        Root_x = int(((-coefficientOfX) / (2 * coefficientOfX2)))
        # Output
        print("The roots of ", coefficientOfX2, "𝒙𝟐 ", "+ ", coefficientOfX, "𝒙 ", "+ ", constantValue, "= 0 are ",
              Root_x, " and ", Root_x)


    # Calculate and Display Roots only if partOfTheQuadraticEquation is greater than zero

    elif partOfTheQuadraticEquation > 0:

        # Output
        print("The discriminant is grater than zero -> There are two real roots")
        # Calculation to get roots
        Root_x1 = int(((-coefficientOfX) + math.sqrt(partOfTheQuadraticEquation)) / (2 * coefficientOfX2))
        Root_x2 = int(((-coefficientOfX) - math.sqrt(partOfTheQuadraticEquation)) / (2 * coefficientOfX2))
        # Output - if the input coefficient of X is positive
        if coefficientOfX > 0:
            print("The roots of ", coefficientOfX2, "𝒙𝟐 ", "+ ", coefficientOfX, "𝒙 ", "+ ", constantValue,
                  "= 0 are ", Root_x2, " and ", Root_x1)
        # Output - if the input coefficient of X is negative
        else:
            print("The roots of ", coefficientOfX2, "𝒙𝟐", coefficientOfX, "𝒙", "+", constantValue, "= 0 are ",
                  Root_x2, "and", Root_x1)

        # Display the Message if partOfTheQuadraticEquation is less than zero

    else:
        print("The discriminant is less than zero -> There are no real roots")

    # Ask whether continue or Exit

    c = input("Want to Exit Press y : ")
    if c == 'y' or 'Y' :
        break
