#Building a python calculator

operation = input("Enter an operation (+,-,/,*): ")
if operation == "":
    print("You have not entered anything")
    exit()
a_input = input("Enter the value of a: ")
if a_input == "":
    print("You have not entered anything")
    exit()
b_input = input("Enter the value of b: ")
if b_input == "":
    print("You have not entered anything")
    exit()
a = float(a_input)
b = float(b_input)

if operation == "+":
    result = a + b
    print(round(result,2))
elif operation == "-":
    result = a - b
    print(round(result,2))
elif operation == "*":
    result = a*b
    print(round(result,2))
elif operation == "/":
    if b == 0:
       print("Sorry you cannot divide by zero")
       exit()
    else:
        result = a/b
        print(round(result,2))
else:
    print("Sorry you entered an invalid operation")
