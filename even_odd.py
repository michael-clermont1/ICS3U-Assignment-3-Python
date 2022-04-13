#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is to check if the number is even or odd


def main():
    # this function checks to see if the number is even or odd

    # input
    number_as_string = input("Enter a positive integer: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        mod = number_as_int % 2
        if mod == 0:
            print("The number is even.")
        elif mod == 1:
            print("The number is odd.")
    except Exception:
        print("That is not a integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
