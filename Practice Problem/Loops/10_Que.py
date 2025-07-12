# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

max_tries = 5
attempt = 1
wai_time = 1

print("----You have only \"5 attempts\"----")
while attempt <= 5:
    print(f"❗Attempt: {attempt}")
    num = input("Enter the Password: ")

    if wai_time <= 1:
        print(f" ❌ Try after \"{wai_time} second\"\n")
    else:
        print(f" ❌ Try after \"{wai_time} seconds\"\n")

    time.sleep(wai_time)
    wai_time *= 2
    attempt += 1