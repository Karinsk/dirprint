"""This script wiil recieve full path input
and will print recursively all the files inside that dir"""

import os
import argparse


PE_HEADER = 'MZ'


def check_if_pe_file(file_path):
    with open(file_path, 'rb') as file_handle:
        header = file_handle.read(2)
    return header == PE_HEADER


def print_if_pe_file(real_path):
    if check_if_pe_file(real_path):
        print(real_path)


def print_pe_files(input_dir):
    if not os.path.exists(input_dir):
        print("input dir doesn't exist")
        return
    for _, _, file_names in os.walk(input_dir):
        for file_inst in file_names:
            real_path = os.path.join(input_dir, file_inst)
            print_if_pe_file(real_path)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', dest="my_path")
    return parser.parse_args()


def main():
    args = get_arguments()
    print_pe_files(args.my_path)


if __name__ == "__main__":
    main()




