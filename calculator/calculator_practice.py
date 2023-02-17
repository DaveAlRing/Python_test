class Calculation:
    def __init__(self, x, operation, y):
        self.x = x
        self.y = y
        self.operation = operation
        
    def calculation(x, operation, y):
        if operation == "+":
            return x + y
        elif operation == "-":
            return x - y
        elif operation == "*":
            return x * y
        else:
            return x / y
     
class Input:
    def __init__(self):
        pass
    
    def input():
        input_x = int(input("Please enter number of x: "))
        input_operation = input("Please enter an operation (+,-,*,/): ")
        input_y = int(input("Please enter number of y: "))
        
        return input_x, input_operation, input_y

user_input_x, user_input_operation, user_input_y = Input.input()

output = Calculation.calculation(user_input_x, user_input_operation, user_input_y) 

print(f"{user_input_x} {user_input_operation} {user_input_y} = {output}")
 