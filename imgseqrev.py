import os
import shutil

print("Reverse Image Sequence")
dir_path = input("Enter the directory path:")
if os.path.isdir(dir_path):
    files = []
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            files.append(f)
    files.sort()
    files_count = len(files)
    print("{:d} files found in {:s}" .format(files_count, dir_path))

    suffix = "reversed"
    extension = ".jpg" #TODO: Allow custom extension
    rev_dir_path = dir_path + "\\reverse"
    os.mkdir(rev_dir_path)
    #TODO: Handle existing folder
    if os.path.isdir(rev_dir_path):
        for f in files:
            shutil.copy(os.path.join(dir_path, f), rev_dir_path)
            os.rename(os.path.join(rev_dir_path, f), os.path.join(rev_dir_path, suffix + "_" + str(files_count - 1) + extension)) #-1 on files_count so it ends at 0
            files_count = files_count - 1

