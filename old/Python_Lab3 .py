'''
Python Lab #3: Modules
'''

'''
1. The goal of this lab is to familiarize yourself with importing modules and to give you a better understanding of how
 python stores UTF-8 characters in memory. 

 Below, a main function is defined. This is where you will add your code. Below that, you have the __name__ check,
 the global variable 's1', and finally a call to the main function. 

 The global variable, s1, is a byte string comprised of 10 bytes. These 10 bytes represent four different UTF-8 
 characters of different byte lengths, 4 bytes, 3 bytes, 2 bytes, and 1 byte. Your job is to create a program that will
 take user input on what byte they want to analyze, determine what character that byte is a part of, and display the 
 character and it's UTF-8 decimal code.  

 You will not create any other functions in this python file. All functions will be created on a separate python file 
 and imported. 
 
 Create a new python file within your current folder named 'decoder'. 
'''

import decoder

def main():
    choice = decoder.getByte()
    notAtStart = True
    while notAtStart:
        #This loops parses through the s1 string until the first starting byte is found based on the users input
        binary = decoder.byteToBin(choice, s1)
        beginningCheck = decoder.check(binary)
        if beginningCheck != -1:
            notAtStart = False
        else:
            choice -= 1

    if beginningCheck == 1:
        decoder.oneByte(choice, s1)
    elif beginningCheck == 2:
        decoder.twoByte(choice, s1)
    elif beginningCheck == 3:
        decoder.threeByte(choice, s1)
    elif beginningCheck == 4:
        decoder.fourByte(choice, s1)

if __name__ == "__main__":
    # Byte string is currently formatted as /2-byte-char/4-byte-char/1-byte-char/3-byte-char
    #Global Variables
    s1 = b'\xd0\x96\xf0\x9f\x8d\x97\x7E\xe1\x83\xac'

    main()