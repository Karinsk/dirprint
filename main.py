"""This script wiil recieve full path input
and will print recursively all the files inside that dir"""

import os

while 1:
    dir = input("Please enter full path: ")
    if (os.path.exists(dir)!= True):
        try_again = input("Dir not found. Try again? answer Y or N ")
        if try_again.upper() == "Y":
            continue
        else:
            break
    for root, dir_names, file_names in os.walk(dir):
        for file in file_names:
            print(file)
    break


