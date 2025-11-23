import math

def calculator():
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Power (a^b)
    6. Square Root
    7. Sine (degrees)
    8. Cosine (degrees)
    9. Tangent (degrees)
    10. Log10
    11. Natural Log (ln)
    12. Factorial
    """)

    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            result = a + b
        elif choice == 2:
            result = a - b
        elif choice == 3:
            result = a * b
        elif choice == 4:
            result = "Error: Division by zero" if b == 0 else a / b
        elif choice == 5:
            result = a ** b

    elif choice == 6:
        a = float(input("Enter number: "))
        result = math.sqrt(a)

    elif choice in [7, 8, 9]:
        angle = float(input("Enter angle in degrees: "))
        if choice == 7:
            result = math.sin(math.radians(angle))
        elif choice == 8:
            result = math.cos(math.radians(angle))
        elif choice == 9:
            result = math.tan(math.radians(angle))

    elif choice == 10:
        a = float(input("Enter number: "))
        result = math.log10(a)

    elif choice == 11:
        a = float(input("Enter number: "))
        result = math.log(a)

    elif choice == 12:
        a = int(input("Enter integer: "))
        result = math.factorial(a)

    else:
        result = "Invalid choice"

    print("Result:", result)

# Start the calculator
calculator()
