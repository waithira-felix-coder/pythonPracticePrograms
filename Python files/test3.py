class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a,b):
        return a-b
    def divide(self, a, b):
        if b== 0:
            return "*Error: Division by zero!!"
        return a /b
    def multiply(self, a,b):
        return a * b


 #Testing
calc = Calculator()
print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(10, 4))
print("Multiply:", calc.multiply(6, 7))
print("Divide:", calc.divide(6, 0))
      
