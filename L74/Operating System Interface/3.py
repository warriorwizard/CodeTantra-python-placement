import os

# print the current working directory
print(os.getcwd())

# lists all the files in the current directory
print(os.listdir())

os.makedirs('dir1/sub-dir1')

# lists all the files in the current directory
print(os.listdir())


# deletes  created directory and the required sub directory 
print(os.removedirs('dir1/sub-dir1'))
print(os.listdir())