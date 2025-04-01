a1=float(input('Enter the first number: '))
b1=float(input('Enter the second number: '))
addition= a1 + b1
subtraction= a1- b1
multiplication= a1 * b1
if b1 != 0:
    division =a1 / b1
else:
    division = "Undefined (division by zero)"

print(f"Addition : {addition}")
print(f"Subtraction : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")

