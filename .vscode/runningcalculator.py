num1 = float(input("enter the first number: "))
flag = True
while flag == True:
   operations = ["+", "-", "*", "/"]
   for operation in operations:
    print(operation)
    method = input("enter the symbol of operation you want to perform from the abouve symbols: ")
    
    num2 = float(input("enter the second number: "))
    if method == "+":
     result = num1 + num2
    elif method == "-":
     result = num1 - num2
    elif method == "*":
     result = num1 * num2
    elif method == "/":
     result = num1 / num2    
    print("the result is: ", result)
    choice = input("press y to continue with the result , press n to exit : ")
    if choice == "y":
       num1 = result
    else: 
     flag = False