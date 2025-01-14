import os

def list_files(folders_input):
    folders_list = folders_input.split()
    #print(folders_list)
    for folder in folders_list:
        try:
            print("--------------------- Files in the folder '{}' are: ---------------------".format(folder))
            # fetching the list of files present at the path 'folder'
            files_in_folder_list = os.listdir(folder)
            for file in files_in_folder_list:
                print(file)
            print()
        except FileNotFoundError:
            print("No such folder exists; Kindly provide correct folder with full path.")
        except PermissionError:
            print("Not allowed to open this particular folder: '{}'".format(folder))

folders = input("Enter folders along with pull path, seperated by space: ")
#print(folders)
list_files(folders)