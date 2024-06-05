def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def select_operation(no, x, y):
    if no == 1:
        return add(x, y)
    elif no == 2:
        return sub(x, y)
    elif no == 3:
        return mul(x, y)
    elif no == 4:
        return div(x, y)
    elif no == 5:
        return True
    else:
        return False


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 5:
        print("It's a voluntary Exit")
        break
    elif 1 <= choice <= 4:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = select_operation(choice, x, y)
        print(f"The result is: {result}")
    else:
        print("Invalid input. Please enter a number from 1 to 5.")
        print("\n")

