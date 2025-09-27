history = []

def add_to_history(operation):
    history.append(operation)

def show_history():
    return history

# Example usage
if __name__ == "__main__":
    add_to_history("5 + 3 = 8")
    add_to_history("10 / 2 = 5")
    print(show_history())
