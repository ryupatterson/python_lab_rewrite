"""
This program will ask for user input on which byte to analyze, determine what character that byte is a part of,
then display the decimal code for the UTF-8 character and the character itself.
"""


# Write a function that allows the user to pick their starting byte and return a value 0-9
# Hint: The built-in "input()" function allows you to do this
def getByte():


# Write a function that takes in two arguments: The user's choice and the starting byte string
# Convert the integer to a string, then to a binary value
# Return that binary value
def byteToBin():



# Write a function that takes in the binary number returned from byteToBin
# and determines if the chosen byte is the starting byte
# This function should return a 1,2,3, or 4.
def check():
    # Hint: Use your debugger to see how the binary value looks to get the index
    # Hint: An if/elif would be great here!
    # Hint: Splitting is also helpful!

    #Check to see if the byte starts with 0, or has no additional bytes


        #one byte character

    #Check to see if the byte starts with a 110

        #two byte character

    #Check to see if the byte starts with a 1110

        #three byte character

    #Check to see if the byte starts with a 11110

        #four byte character

    #If its not one of those options, you can return -1 to indicate you are not at a starting byte!

        #Chosen byte is not the start of the character, decrease index by one



# Write a function for a one byte character that takes in the chosen byte and the given string,
# converts the one byte character into decimal format and then returns the ASCII character
def oneByte():
    #Use the byte to bin function on the choice and the given string, store it in a variable

    #Check to see if the beginning of the byte starts with a 0, if so slice without the 0

    #If it does not start with a 0, it must only use 7 bits, so slice including the first bit!


    #Print the integer (decimal) version of the sliced value

    #print the UTF-8 Character associated with it


# Write a function that that takes in the choice and the given string
# Convert, slice, and print accordingly
def twoByte():
    #Use the byte to bin function on the choice and the given string, store it in a variable

    #Slice the binary number to get rid of the leading bits, i.e, the flag bits!

    #Move up one in your string, to find the starting bit. Increment your choice!

    #Re-run the byteToBin function with the new choice and given string!

    #Slice the new binary number to get rid of the leading bits!

    #Combine the two binary numbers and convert them to an integer

    #Print the decimal value

    #Print the UTF-8 character


# Write a function that takes in the choice and the given string
# Convert, Slice, and display the decimal value and UTF-8 character
def threeByte():
    #Use the byte to bin function on the choice and the given string, store it in a variable

    #Slice the binary number to get rid of the leading bits

    #Increment your choice to move forward in the given string

    #Re-run the byteToBin with the new choice and the given byte string

    #Slice the binary number to get rid of the leading bits

    #Increment your choice one last time to get the starting byte, re-run the byteToBin function, slice the binary



    #Combine and convert the three sliced binaries into one integer

    #Print the decimal number and then print the UTF-8 character



# Write a function to handle the 4-byte character case!
# The pattern is similar and I believe you can handle this one on your own! :)
def fourByte():


if __name__ == "__main__":
    main()

