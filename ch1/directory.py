import os

# Specify the directory you want to list
directory_path = "D:\\game"  # '.' refers to the current working directory

try:
    # List all entries in the directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")