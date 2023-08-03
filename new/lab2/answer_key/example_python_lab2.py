'''
Python Lab #2: Functions
These labs are meant to familiarize yourself with the topics discussed in class.
'''


# 1. A bank customer wants to withdraw money from her account at an ATM. Create a program for the ATM to check the 
# customer's balance and determine if there is enough money in the account. If there’s not enough money in the account, 
# return ‘Insufficient funds.’ If the withdraw is the same amount as the balance, return 'This is all your money!'. If the 
# withdraw is less than the balance, calculate the new balance, and return the new balance, casted as a string, up to 
# to decimal points.

def withdrawal(balance:float, withdrawal_amount:float)->str:
    if balance > withdrawal_amount:
        return str('%.2f' % (balance - withdrawal_amount))
    elif balance == withdrawal_amount:
        return "This is all your money!"
    else:
        return "Insufficient funds."


# 2. Create a function that takes two integer arguments. The function will multiplies them together and test's whether the
# result is even or odd. If the result is even, the function will return true. If the result is odd, the function will
# return false.

def product_is_even(int1:int, int2:int)->bool:
    return (int1 * int2) % 2 == 0


# 3. Create a function that takes a list of strings as an argument. Reverse the list of strings, as well as each 
# string in the list. You are not allowed to use list.reverse(). Return the resulting list.

def reverse_squared(string_list:list)->list:
    return [string[::-1] for string in string_list[::-1]]


# 4. Create a nested loop that creates a multiplication table that is x (rows) by y (cols). The times table should
# start with 1. You should return a 2 dimensional array.

def times_tables(x:int, y:int)->list[list]:
    output = list()
    for i in range(1, x+1):
        row = list()
        for k in range(1, y+1):
            row.append(i*k)
        output.append(row)
    return output

# 5. Write a function that takes a string parameter, 'string', that returns a string only containing the 
# consonants in 'string'.

def remove_vowels(string:str)->str:
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    output = ""
    for char in string:
        if char not in VOWELS:
            output += char
    return output


if __name__ == "__main__":
    balance = 100.30
    withdrawal_amount = 30.00
    if withdrawal(balance, withdrawal_amount):
        print("withdrawal function:")
        print(f"input: balance={balance}, withdrawal_amount={withdrawal_amount}")
        print(f"output: {withdrawal(balance, withdrawal_amount)}")
        print()
    
    int1 = 4
    int2 = 5
    if product_is_even(int1, int2):
        print("product_is_even function:")
        print(f"input: int1={int1}, int2={int2}")
        print(f"output: {product_is_even(int1, int2)}")
        print()

    example_list = ["hello", "world"]
    if reverse_squared(example_list):
        print("reverse_squared function:")
        print(f"input: string_list={example_list}")
        print(f"output: {reverse_squared(example_list)}")
        print()
    
    x, y = 10, 7
    if times_tables(x, y):
        print("times_tables function:")
        print(f"input: x={x}, y={y}")
        print("output:")
        for row in times_tables(x, y):
            print(row)
        print()

    example_string = "hello world"
    if remove_vowels(example_string):
        print("remove_vowels function:")
        print(f"input: string={example_string}")
        print(f"output: {remove_vowels(example_string)}")
        print()
       
    