# Python Lab 3: Directory Enumeration and File Manipulation
# Please run this lab from the directory that it is stored in. It utilizes files that are in the 
# example/ directory -- please do not edit this.

import os, traceback

# Return a list of the files in the "example" directory given to you.
def list_directory() -> list:
    
    return

# Write a function that checks to see if a directory/file exists. It should return a bool.
def file_exists(directory: str) -> bool:
    
    return

# Write a function that will create a new file, "hello.txt" that says (two lines):
# Hello world
# Hello python
def conversation() -> None:
    
    pass

# Write a function that deletes "hello.txt". Return true if it has been deleted and false if it has not been deleted.
def delete_conversation() -> bool:
    
    return

# Write a function that determines what the OS type (Windows, Linux, etc) is. If the box is a 
# linux box, return the PRETTY_NAME of the distribution/version information. If it is a windows box, return the release (i.e. XP) and version
# using the format {release}-{version}. If it is neither, return "undeterminable".
# Hint: use the platform module
def where_am_i() -> str:
    
    return

# Write a function that writes an example dictionary to disk in json format, called "test.json", and reads it back
# in again. Return a boolean value that checks to see that the original dictionary and 
# the one parsed from the json are equal. 
# Extra - pay attention to the output that is printed when you run this script. Is there any way
# 'pretty' print the json file so that its easier to read?
def write_json() -> bool:
    
    return


""" 
    =================================================================================================================
                                                    DO NOT TOUCH
                                                    DO NOT TOUCH
    =================================================================================================================
"""
if __name__ == "__main__":
    try:
        file_inventory = set(os.listdir()) # taking accountability of files currently in the directory
        if list_directory():
            print("List Directory Function Output:")
            print(list_directory())
            print()

        example_dir = "example"
        example_nonexistent = "asdfjiowjiw"
        if file_exists(example_dir):
            print("File Exists Function:")
            print(f"Input: directory={example_dir}")
            print(f"Output: {file_exists(example_dir)}")

            print(f"Input: directory={example_nonexistent}")
            print(f"Output: {file_exists(example_nonexistent)}")
            print()

        try:
            if conversation() is not None:
                    print("Conversation Function:")
                    conversation()
                    print("Check the output!")
                    print()
        except Exception as e:
            print(e)
            print()
        
        input("Check on hello.txt...press the enter key to continue")
        print()

        try:
            print("Delete Conversation Function:")
            print(f"Output: {delete_conversation()}")
            print()
        except Exception as e:
            print(e)
            print()

        if where_am_i():
            print("Where Am I Function Output:")
            print(where_am_i())
            print()

        print("Write Json Function:")
        write_json_output = write_json()
        if write_json_output:
            print(f"Output: {write_json_output}")
            input("Check on your json output...press the enter key to continue")
        else:
            print("function not yet written")
        
        print("\nCleaning up files...")
        updated_inventory = set(os.listdir())
        updated_inventory -= file_inventory
        for file in updated_inventory:
            print(f"Deleting {file}...")
            os.remove(file)
        
    except FileNotFoundError:
        print("Check to see if you are running this in the correct directory...")
        traceback.print_exc()
        
