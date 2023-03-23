def Calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2 
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    
def Calculate():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator: (+, -, *, /) ")
    result = Calculator(num1, num2, operator)
    print("Result of the operation is: ",round (result, 4))
Calculate()
    
        
        
    