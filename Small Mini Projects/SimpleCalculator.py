print("---Simple Calculator---")
num1 = int(input("Enter the 1st No.: "))
print("Operators: +, -, *, /, %, **, //")
op = str(input("Choose the Operator: "))
num2 = int(input("Enter the 2nd No.: "))
print("\n")

if(op == '+'):
    ans = num1 + num2
    print("Answer: ",ans)
elif(op == '-'):
    ans = num1 - num2
    print("Answer: ",ans)
elif(op == '*'):
    ans = num1 * num2
    print("Answer: ",ans)
elif(op == '/'):
    ans = num1 / num2
    print("Answer: ",ans)
elif(op == '%'):
    ans = num1 % num2
    print("Answer: ",ans)
elif(op == '**'):
    ans = num1 ** num2
    print("Answer: ",ans)
elif(op == '//'):
    ans = num1 // num2
    print("Answer: ",ans)
else:
    print("Please Choose the Valid Operator:)")