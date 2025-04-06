import os

# Read the file
file_path = "Demo1.txt"

with open(file_path, "r") as f:
    # Read & print the entire file using read
    contents = f.read()

print(contents)
print('-'* 20)
# file_lsit = list(contents)
# print(file_lsit)
# print('-'* 20)


with open(file_path, "r") as f:
    # Read the first line from the file
    print(f.readline(-1))
    print('-'* 20)
    
with open(file_path, "r") as f:
    # Read the first 6 characters from the file
    print(f.readline(6))
    print('-'* 20)

with open(file_path, "r") as f:
    # read the entire file as a list using the Python .readlines() method:
    print(f.readlines()) 
    print('-'* 20)
    
    
