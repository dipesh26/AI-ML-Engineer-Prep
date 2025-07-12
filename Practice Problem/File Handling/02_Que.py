# WAF that replace all occurrences of "java" with "python" in practice.txt file.
def replace():
    with open("practice.txt","r") as f:
        data = f.read()
    
    new_data = data.replace("Java", "Pyhton")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)

replace()        