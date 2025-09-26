# calculator_basic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b
    print(f"Multiplying {a} and {b}")
    return result

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    result = a / b
    return round(result, 1)

if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
