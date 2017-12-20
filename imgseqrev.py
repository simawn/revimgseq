#!/usr/bin/env python3
import os
from os.path import splitext
from shutil import copyfile
from time import time
from collections import Counter

dir_path = os.path.dirname(__file__)
all_directory_files = []

current_file_name = []
new_file_name = []


def find_all_directory_files():
    for file in os.listdir(dir_path):
        if os.path.isfile(file):
            all_directory_files.append(file)


def find_common_extension():
    tally = Counter()

    for file in all_directory_files:
        tally[splitext(file)[1]] += 1

    return tally.most_common(1)[0][0]  # Output is [(str, int)]


def prepare_reversal(file_extension):
    for file in all_directory_files:
        if splitext(file)[1] == file_extension:
            current_file_name.append(file)
    current_file_name.sort()

    files_to_process = counter = len(current_file_name)

    for file in current_file_name:
        new_file_name.append(splitext(file)[0] + "-R" + str(counter - 1).zfill(5) + splitext(file)[1])
        counter -= 1

    print("{0} files to be renamed:".format(files_to_process))

    for i in range(0, files_to_process):
        print("{0} -> {1}".format(current_file_name[i], new_file_name[i]))


def rename_files():
    reverse_folder_name = "Reversed-Footage-" + str(int(time()))
    try:
        os.mkdir(reverse_folder_name)
        for i in range(len(current_file_name)):
            copyfile(current_file_name[i], os.path.join(reverse_folder_name, new_file_name[i]))
    except Exception as err:
        print(err)
        exit(1)


if os.path.isdir(dir_path):
    find_all_directory_files()
    prepare_reversal(find_common_extension())
    rename_files()
    print("Done!")
else:
    print("Directory error")
