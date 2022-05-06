#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 5, 2022
# This program has a function called farenheit(). This function lets you
# enter a temperature in degrees Celsius (as a decimal), and converts and
# displays the temperature in Fahrenheit


def fahrenheit():
    # get celsius as a string
    tc_string = input("Enter a temperature in degrees Celsius: ")
    print()

    try:
        # convert the user input to a float
        tc = float(tc_string)

        # calculate the conversion from celsius to fahrenheit
        tf = (9 / 5) * tc + 32

        # display the output
        print("{} degrees celsius is equal to {} degrees fahrenheit!".format(tc, tf))
    except Exception:
        print("Must be a number!")


def main():

    # call fahrenheit
    fahrenheit()


if __name__ == "__main__":
    main()
