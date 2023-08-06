'''
Python Lab #1: Numbers, Math Operators, Strings, and Lists
These labs are meant to familiarize yourself with the topics discussed in class.
'''

# 1. Create a variable 'a' and assign the integer 5 to it. Return this variable.
def question_1():
    a = 5
    return a

#2. Slice the list below to only contain '3.2', 'python', and 9.8. Return the list
def question_2():
    example_list = [5, '3.2', 'python', 9.8, 'rocks', 2] # DO NOT CHANGE THIS LINE
    return example_list[1:4]

#3. Using the values contained in the list, return the value of 5 to the second power
def question_3():
    example_list = [5, '3.2', 'python', 9.8, 'rocks', 2] # DO NOT CHANGE THIS LINE
    return example_list[0]**example_list[-1]

#4. Create a string that states 'python rocks' and return it
def question_4():
    string = "python rocks"
    return string

#5. Using the values in the list below, add 2 to 3.2 to get 5.2 and return it
def question_5():
    example_list = [5, '3.2', 'python', 9.8, 'rocks', 2] # DO NOT CHANGE THIS LINE
    return float(example_list[1]) + example_list[-1]

#6 Create and return the string '9.825'
def question_6():
    return '9.825'

#7. Return the data type of the variable below
def question_7():
    example_var = "3.2"  # DO NOT EDIT
    return type(example_var)

# 8. Cast the example variable below to "float" and return it
def question_8():
    example_var = "3.2"  # DO NOT EDIT
    return float(example_var)

# 9. Manipulate the two strings to create one string that prints "The Earth is ROUND" and return it.
def question_9():
    example_string_1 = "       The Earth is flat"
    example_string_2 = 'A sphere is round'
    return example_string_1.strip()[:-4] + example_string_2[-5:].upper()

# 10. Decode the following example byte string (utf-8) and return it.
def question_10():
    example_byte_string = b'\x68\x65\x6C\x6C\x6F'
    return example_byte_string.decode()

# 11. Format a string using the variables below that says "This PC costs $1999.00" and return it. 
# Make sure the price has two decimal places
def question_11():
    device = "PC"
    price = 1999
    return f"This {device} costs ${'%.2f' % price}"

# 12. Assign the list below to a new variable, example_list_2. Change 580 in example_list_2 to 600. Make a copy of 
# example_list_2 and call it example_list_3, ensuring it is not linked to example_list_2. Change the first
# value of example_list_3 back to 580. Return all three lists. 
def question_12():
    example_list = [580, 'laptop', 1999, 'PC', 450, 'console']  # DO NOT EDIT
    example_list_2 = example_list
    example_list_2[0] = 600
    example_list_3 = example_list_2.copy()
    example_list_3[0] = 580
    return example_list, example_list_2, example_list_3

# 13. Calculate the result of an exclusive OR between 10111011 and 00110111. Return the result in both
# binary and then in hex.
def question_13():
    result = 0b10111011 ^ 0b00110111
    return bin(result), hex(result)

# 14. Assign all keys of the dictionary below to a variable called 'keys' and return it.
def question_14():
    example_dict = {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'solaris'}  # DO NOT EDIT
    keys = example_dict.keys()
    return keys

# 15. Add the key, 'network_ips', to the dicitonary below. Its value will be the list ['10.10.10.1', '10.10.10.254']
# Return the dictionary.
def question_15():
    example_dict = {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'solaris'}  # DO NOT EDIT
    example_dict["network_ips"] = ['10.10.10.1', '10.10.10.254']
    return example_dict

# 16. Change the value of the key, 'target', to 'Windows 7'. Return the dictionary.
def question_16():
    example_dict = {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'solaris'}  # DO NOT EDIT
    example_dict['target'] = "Windows 7"
    return example_dict

# 17. Assign the dictionary below to a new variable, example_dict_2. In example_dict, change the value of the key
# 'redirector' to 'freeBSD'. Now, create a copy of example_dict_2 assigned to variable example_dict_3. In 
# example_dict_3, change the value of 'redirector' back to 'centOS'. Return all three dictionaries.
def question_17():
    example_dict = {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'solaris'}  # DO NOT EDIT
    example_dict_2 = example_dict
    example_dict["redirector"] = "freeBSD"
    example_dict_3 = example_dict_2.copy()
    example_dict_3["redirector"] = "centOS"
    return example_dict, example_dict_2, example_dict_3

# 18. Using only the example list, return the value 10.
def question_18():
    example_list = [[1, 2, 3], [4, 5, 6], [7, [8, 9]], [10, [11, [12, 13]]]] # DO NOT EDIT
    return example_list[3][0]

# 19. Using only the example list, return the values 5, 8, and 11
def question_19():    
    example_list = [[1, 2, 3], [4, 5, 6], [7, [8, 9]], [10, [11, [12, 13]]]] # DO NOT EDIT
    return example_list[1][1], example_list[2][1][0], example_list[3][1][0]


# 20. Using only the example list, return the value 13
def question_20():
    example_list = [[1, 2, 3], [4, 5, 6], [7, [8, 9]], [10, [11, [12, 13]]]] # DO NOT EDIT
    return example_list[3][1][1][1]

""" 
    =================================================================================================================
                                                    DO NOT TOUCH
                                                    DO NOT TOUCH
    =================================================================================================================
    Practical Example: Below is a hex dump from a packet capture in the format of a string. By using slicing,
    we can assign bytes to their corresponding variables, which are listed below. An example is provided of 
    how to slice the hex dump and convert the hexadecimal characters into an easy to read format for the source IP.
"""

# Example hexdump
HEXDUMP = '78d2 94a6 75b1 147d da12 34dc 0800 4500 ' \
        '0059 0000 4000 4006 1287 c0a8 010f c0a8 ' \
        '0101 f87c 01bb 5087 e285 2849 991d 8018 ' \
        'ffff fdc3 0000 0101 080a 77cb d864 2c59 ' \
        '6086 1703 0300 20bb 6b4a 14a0 035f 1328 ' \
        'd698 b300 4991 9a48 a150 7aef 3b58 682a ' \
        'f343 fc6b 2fe2 67'

# Example hexdump form of IP
HEXDUMP_IP = 'c0a8 010f'

def example_pcap_parsing(hexdump:str):
    #Ethernet Header
    dest_mac = hexdump[0:14]
    source_Mac = hexdump[15:29]

    #IP Header
    ip_version = hexdump[35:36]
    header_length = hexdump[36:37]
    total_length = hexdump[40:44]
    flags_and_offset = hexdump[50:54]
    ttl = hexdump[55:57]
    ip_protocol = hexdump[57:59]
    checksum = hexdump[60:64]
    source_ip = hexdump[65:74]
    dest_ip = hexdump[75:84]

    #TCP Header
    source_port = hexdump[85:89]
    dest_port = hexdump[90:94]
    data_offset = hexdump[115:119]
    
    return f"The Source IP address is " \
         f"{int(source_ip[0:2], 16)}.{int(source_ip[2:4], 16)}.{int(source_ip[5:7], 16)}.{int(source_ip[7:9], 16)}"

# 21. Use the example_pcap_parsing function above as a model and create a function that takes an IP address, 
# formatted as a hex dump (a pair of 4 hex digits separated by a space, i.e. 'c0a8 010f'), and returns it
# in its decimal form.
def question_21(hexdump_ip:str)->str:
    return f"{int(hexdump_ip[0:2], 16)}.{int(hexdump_ip[2:4], 16)}.{int(hexdump_ip[5:7], 16)}.{int(hexdump_ip[7:9], 16)}"


# 21. Use the example_pcap_parsing function above as a model and create a function that takes a hexdump (formatted
# like the one below in the main method) and returns a dictionary with the following keys:
# src_ip, dst_ip, src_port, dst_port. Make sure to utilize the function you just wrote above.
def question_22(hexdump:str):
    return {
        "src_ip": question_21(hexdump[65:74]),
        "dst_ip": question_21(hexdump[75:84]),
        "src_port": int(hexdump[85:89], 16),
        "dst_port": int(hexdump[90:94], 16)
    }


""" 
    =================================================================================================================
                                                    DO NOT TOUCH
                                                    DO NOT TOUCH
    =================================================================================================================
"""
if __name__ == "__main__":
    if question_1():
        print("Question 1 Output:")
        print(question_1())
        print()
    
    if question_2():
        print("Question 2 Output:")
        print(question_2())
        print()
    
    if question_3():
        print("Question 3 Output:")
        print(question_3())
        print()

    if question_4():
        print("Question 4 Output:")
        print(question_4())
        print()

    if question_5():
        print("Question 5 Output:")
        print(question_5())
        print()

    if question_6():
        print("Question 6 Output:")
        print(question_6())
        print()

    if question_7():
        print("Question 7 Output:")
        print(question_7())
        print()

    if question_8():
        print("Question 8 Output:")
        print(question_8())
        print()

    if question_9():
        print("Question 9 Output:")
        print(question_9())
        print()

    if question_10():
        print("Question 10 Output:")
        print(question_10())
        print()

    if question_11():
        print("Question 11 Output:")
        print(question_11())
        print()

    if question_12():
        print("Question 12 Output:")
        e1, e2, e3 = question_12()
        print(f"Example 1: {e1}")
        print(f"Example 2: {e2}")
        print(f"Example 3: {e3}")
        print()

    if question_13():
        print("Question 13 Output:")
        print(question_13())
        print()

    if question_14():
        print("Question 14 Output:")
        print(question_14())
        print()

    if question_15():
        print("Question 15 Output:")
        print(question_15())
        print()

    if question_16():
        print("Question 16 Output:")
        print(question_16())
        print()

    if question_17():
        print("Question 17 Output:")
        e1, e2, e3 = question_17()
        print(f"Example 1: {e1}")
        print(f"Example 2: {e2}")
        print(f"Example 3: {e3}")
        print()

    if question_18():
        print("Question 18 Output:")
        print(question_18())
        print()

    if question_19():
        print("Question 19 Output:")
        print(question_19())
        print()

    if question_20():
        print("Question 20 Output:")
        print(question_20())
        print()

    
    print("Example PCAP Parser Output:")
    print(example_pcap_parsing(HEXDUMP))
    print()

    if question_21(HEXDUMP_IP):
        print("Question 21:")
        print(f"Input:  {HEXDUMP_IP}")
        print(f"Output: {question_21(HEXDUMP_IP)}")
        print()
    
    if question_22(HEXDUMP):
        print("Question 22 Output:")
        print(question_22(HEXDUMP))