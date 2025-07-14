import time
import threading

def task1():
    print("Task 1 Started..")
    time.sleep(3)
    print("Task 1 Ended..")

def task2():
    print("Task 2 Started..")
    time.sleep(3)
    print("Task 2 Ended..")

t1 = threading.Thread(target=task1)    
t2 = threading.Thread(target=task2)    

t1.start()
t2.start()

t1.join()
t2.join()

# --------------------------------------------------------------------------

# File downloading example
def download_file(name):
    print(f"Downloading {name}...")
    time.sleep(2)
    print(f"{name} downloaded...")

files = ["File1","File2","File3"]
thread = []

for file in files:
    t = threading.Thread(target=download_file, args=(file,))
    thread.append(t)
    t.start()

for t in thread:
    t.join()

print(f"\nAll files download completed...")