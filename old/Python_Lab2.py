'''
Python Lab #2: Functions
These labs are meant to familiarize yourself with the topics discussed in class.
'''

'''
1. A bank customer wants to withdraw money from her account at an ATM. Create a program for the ATM to check the 
customer's balance and determine if there is enough money in the account. If there’s not enough money in the account, 
print ‘Insufficient funds.’ If the withdraw is the same amount as the balance, print 'This is all your money!'. If the 
withdraw is less than the balance, issue the cash, calculate the new balance, and print the new balance.
'''

def atm(withdrawAmount):
    balance = 1000

atm(600)

'''
2. Create a function that takes two integer arguments. The function will multiplies them together and test's whether the
result is even or odd. If the result is even, the function will print "<arg1> multiplied by <arg2> results in an even 
number!". If the result is odd, the function will print "<arg1> multiplied by <arg2> results in an odd number!"
'''
'''
def evenOrOdd(num1, num2):

evenOrOdd(3, 7)
'''
'''
3. Create a function that takes a list of strings as an argument. The function will iterate through each string, and
determine if the string is an even or odd number of characters in length. If the string is an odd number of characters 
in length, it will add it to a list called oddLength. If the string is an even number of characters long, it will be
added to a list called evenLength. Print the oddLength and evenLength lists at the end of the function. 
'''
'''
stringList = ['cake', 'pie', 'brownie', 'ice-cream', 'cookie']

def lengthTest(list):

lengthTest(stringList)
'''
'''
4. Create a nested loop that creates a multiplication table from numbers 1 to 10.
'''

'''
5. What would be the output of this function?
'''
'''
a = [1, 2, 3, 4]

while a:
    print(a.pop())
'''
'''
6. Create a while loop that iterates through the string variable 'a' and prints out the letters individually, except 
if the letter is a vowel, then it is not printed. 
'''

a = 'Hello World'
