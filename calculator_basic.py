# calculator_basic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    print(f"Main branch multiplying {a} and {b}")
    print(f"Feature branch multiplying {a} and {b}")
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot modulus by zero")
    return a % b


if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
