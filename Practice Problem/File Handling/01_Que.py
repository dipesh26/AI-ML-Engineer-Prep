# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O")
    f.write("\nusing Java.\nI like programming in Java.")
    
with open("practice.txt","r") as f:
    data = f.read()
    print(data)