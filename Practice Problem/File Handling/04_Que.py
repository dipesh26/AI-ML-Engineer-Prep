# WAF to find in which line of the file does the word "learning"occur first. Print -1 if word not found.
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"Found in line No. {line_no}")
                return
            line_no += 1
    return -1

check_for_line()             