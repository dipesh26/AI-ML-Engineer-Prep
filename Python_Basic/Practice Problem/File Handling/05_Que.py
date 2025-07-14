# From a file containing numbers separated by comma, print the count of even numbers.
with open("demo.txt","r") as f:
    data = f.read()
    count = 0
    print(data)
    nums = data.split(",")
    print(nums)
    for i in nums:
        if int(i) % 2 == 0:
            count += 1
    print(count)