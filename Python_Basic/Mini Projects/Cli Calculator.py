print("--- CLI Calculator ---\n")
print("Opeartions -")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide \n")

while True:
    SelectOP = input("Select Operation (+, -, *, /):- ")

    if SelectOP in ('+', '-', '*', '/'):
        num1 = int(input("Enter the 1st No.: "))
        num2 = int(input("Enter the 2nd No.: "))

        if SelectOP == '+':
            ans = num1 + num2

        elif SelectOP == '-':
            ans = num1 - num2

        elif SelectOP == '*':
            ans = num1 * num2

        elif SelectOP == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            ans = num1 / num2
  
        print("Answer: ",ans)
        
        while True:
            next_calcu = input("Want to do Further Calculation? (yes/no):- ")
            if next_calcu == "yes":
                SelectOP = input("Select Operation (+, -, *, /):- ")

                if SelectOP in ('+', '-', '*', '/'):
                    next_num = int(input("Enter the next No.: "))
                    
                    if SelectOP == '+':
                        ans = ans + next_num
                    
                    elif SelectOP == '-':
                        ans = ans - next_num

                    elif SelectOP == '*':    
                        ans = ans * next_num

                    elif SelectOP == '/':
                        if next_num == 0:
                            print("Cannot divide by zero.")
                            continue
                        ans = ans / next_num
                    
                    print("Answer: ",ans)

            elif next_calcu == "no":
                break
            else:
                print("Please type 'yes' or 'no'.")
    else:
        print("Invalid operation. Try again.")




  



  



  



  



  



  



  



  



  



  



  



  



  



  
    
    
