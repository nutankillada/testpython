import os

folders = input("Enter the folders with spaces: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Provide a valid folder instead of " + folder)
        continue
    count =str(len(files))
    print("List of files under the folder " + folder + " are " + count)
    for file in files:
        print(file)


    
    