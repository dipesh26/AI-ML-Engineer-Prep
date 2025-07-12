# Search if the word "learning" exists in the practice.txt file or not.
def word_checker():
    word = "learning"
    with open("practice.txt", "r") as f:
        data  = f.read()
        if word in data:
            print("Yes")
        else:
            print("No")

word_checker()            