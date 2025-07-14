import os
f = open("Sample.txt","w")             # To Open a File in write mode
data = f.write("This is the Sample file")   # To Write(Overwrite) a File.
print(data)

f = open("Sample.txt","r")    # To Open a File in read mode.
data = f.read()               # To read the File.
print(data)

f = open("Sample.txt", "a")    # To Open a File in append mode.
data = f.write("\nI am learning python")
print(data)

# r+ = read + overwrite file
f = open("Sample.txt", "r+")   
data = f.write("I am learning python")
print(data)

# w+ = read + overwrite file
f = open("Sample.txt", "w+")  
data = f.write("I am learning python")
print(data)

# a+ = read + append file
f = open("Sample.txt", "a+")   
data = f.write("\nI am learning python")
print(data)

# with Syntax
with open("Sample.txt","r") as f:
    data = f.read()
    print(data)

with open("Sample.txt","a") as f:
    data = f.write("\nHello")
    print(data)    

# os.remove("Sample.txt")    # To delete the file