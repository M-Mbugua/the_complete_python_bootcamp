import os

print(os.getcwd()) # Get the current working directory
print(os.listdir('C:\\Users')) # List the directories in the current directory

for folder, sub_folders, files in os.walk('C:\\Users\\user\\Documents\\GitHub\\python'):

    print(f"Currently looking at {folder}\n")
    print("The Sub-folders are: ")
    for sub_fold in sub_folders:
        print(f"Sub-folder: {sub_fold}")

    print("\n")
    print("The files are: ")
    for f in files:
        print(f"File: {f}")
    print("\n")





