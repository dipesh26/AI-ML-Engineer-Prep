fruits = ['Apple', 'Banana', 'Cherry','Mango']

for i in fruits:
    print(i)

# Looping through String
for i in 'Banana':
    print(i)

# Break Statement
for i in fruits:
    if(i == 'Cherry'):
        break
    print(i)

# Continue Statement
for i in fruits:
    if(i == "Cherry"):
        continue
    print(i)

# range() function
# Start
for i in range(6):
    print(i)
print("\n")
# # Stop
for i in range(2,5):
    print(i)
print("\n")
# # Step
for i in range(2, 18, 3):
    print(i)

# Else in for loop
for i in range(6):
    print(i)
else:
    print("End")

# Nested loop
adj = ['Red','Blue','Green']

for i in adj:
    for j in fruits:
        print(i,"=",j)
    print("\n")

# Pass Satetement
for i in [0,1,2,3]:
    pass