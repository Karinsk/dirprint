"""This script wiil recieve full path input
and will print recursively all the files inside that dir"""

import os
import argparse
import fnmatch

def print_dir():

    running = True
    while running:
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', dest="myPath")
        args = parser.parse_args()
        input_dir = args.myPath
        print(input_dir)
        if os.path.exists(input_dir)!= True:
            try_again = input("Dir not found. Try again? answer Y or N ")
            if try_again.upper() == "Y":
                continue
            elif try_again.upper() == "N":
                running = False
                continue
            else:
                print("Invalid input")
                running = False
                continue
        for _, _, file_names in os.walk(input_dir):
            for file_inst in file_names:
                if fnmatch.fnmatch(file_inst, 'MZ*'):
                    print(file_inst)
                else:
                    continue
        running = False


if __name__ == "__main__":
    print_dir()


