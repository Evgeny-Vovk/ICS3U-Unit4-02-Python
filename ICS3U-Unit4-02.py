# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit4-02.py File,
# learning do...while statement in python.

 
def main():

    # input and variables
    input_number = input("Input a positive number: ")
    counter = 0
    answer = 1

    # process and output
    print("")
    try:
        input_number_asint = int(input_number)
        if input_number_asint < 0:
            print("This is not a positive number.")
        else:
            while counter < input_number_asint:
                counter += 1
                answer = answer * counter
            print("{0:,}! = {1:,}".format(input_number_asint, answer))
    except ValueError:
        print("Invalid input, Please try again following the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
