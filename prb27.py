a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
d = float(input("Enter value for d: "))
if c-d == 0:
    print("The value of c - d is zero. Division by zero is not allowed.")
else:
    result = (a + b) / c-d
    print("The result of (a + b) / (c - d) is:",round(result,2))
