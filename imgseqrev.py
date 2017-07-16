import os
import shutil

print("=================================")
print("Reverse Image Sequence v1.1 by Simon Huang")
print("=================================\n")
dir_path = os.path.dirname(__file__)

if os.path.isdir(dir_path):
    files = []
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            files.append(f.split('.'))
    files.sort()
    files_count = len(files)

    # print(files)

    print("{:d} files found in {:s}".format(files_count, dir_path))

    # In case of multiple file extension, only reverse the one with the most occurrences

    extension_count = {}
    for f in files:
        extension = f[len(f) - 1]  # in case there were multiple '.' in file name eg: test.dot.jpg.txt
        if extension in extension_count:
            extension_count[extension] += 1
        else:
            extension_count[extension] = 1

    print(extension_count)

    k = list(extension_count.keys())
    v = list(extension_count.values())
    popular_extension_count = max(v)
    popular_extension = k[v.index(popular_extension_count)]

    print("." + popular_extension + " seems to be the most popular file extension in this folder with " +
          str(popular_extension_count) + " occurrences.")

    startReverse = input("Reverse all ." + popular_extension + " image sequence? (y/n)")

    if startReverse.lower() == "y":
        print("Reversing...")

        suffix = "RVS"

        # Can be optimized
        folder_name = "Reversed"
        for f in files:
            if f[len(f) - 1] == popular_extension:
                folder_name = f[0][0:int(len(f[0]) / 2)] + "_" + str(suffix)
                break

        # TODO: Handle existing folder
        reverse_folder_path = os.path.join(os.path.abspath(dir_path), folder_name)
        os.mkdir(reverse_folder_path)

        if os.path.isdir(reverse_folder_path):
            print("Folder created: " + reverse_folder_path)

            for f in files:
                if f[len(f) - 1] == popular_extension:
                    filename_joined = ".".join(f)
                    source_file_path = os.path.join(os.path.abspath(dir_path), filename_joined)

                    shutil.copy(source_file_path, reverse_folder_path)

                    new_file_name = folder_name + "_" + str(popular_extension_count - 1).zfill(
                        5) + "." + popular_extension
                    os.rename(os.path.join(reverse_folder_path, filename_joined),
                              os.path.join(reverse_folder_path, new_file_name))

                    popular_extension_count -= 1

                    print(filename_joined + " -> " + new_file_name)

            print("All done!")

        else:
            print("Error creating reverse folder")

    else:
        print("Process Ended")

else:
    print('Directory error')
