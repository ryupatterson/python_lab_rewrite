"""
    Lab 3 is File Manipulation. Please run this lab from the directory that it is stored in. It utilizes files that are in the 
    example/ directory please do not edit this.
"""
import os, io
import platform
import glob

# Return a list of the files in the "example" directory given to you.
def list_directory()->list:
    return os.listdir("example/")

# Write a function that checks to see if a directory/file exists. It should return a bool.
def file_exists(directory:str)->bool:
    return os.path.exists(directory)

# Write a function that will create a new file, "hello.txt" that says (two lines):
# Hello world
# Hello python
def conversation()->None:
    with open("hello.txt", 'w') as outfile:
        outfile.write("Hello world\n")
        outfile.write("Hello python\n")

# Write a function that checks to see if "hello.txt" exists in the cwd and deletes it
# if it does. Return true if it has been deleted and false if it has not been deleted.
def delete_conversation()->bool:
    if os.path.exists("hello.txt"):
        try:
            os.remove("hello.txt")
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False

if __name__ == "__main__":
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
    
    input("Check on hello.txt...press any key to continue")

    try:
        print("Delete Conversation Function:")
        print(f"Output: {delete_conversation()}")
        print()
    except Exception as e:
        print(e)
        print()

        


    
