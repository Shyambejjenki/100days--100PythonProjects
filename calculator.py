def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Division by zero"

# Recursive functions
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Lambda functions
square = lambda x: x**2
cube = lambda x: x**3
is_even = lambda x: x % 2 == 0

# Menu-driven calculator
while True:
    print("\n--- Python Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    print("5. Factorial\n6. Fibonacci\n7. Square\n8. Cube\n9. Check Even\n0. Exit")

    choice = int(input("Enter choice: "))
    if choice == 0:
        print("Exiting Calculator...")
        break

    if choice in [1, 2, 3, 4]:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 1: print("Result:", add(a, b))
        elif choice == 2: print("Result:", sub(a, b))
        elif choice == 3: print("Result:", mul(a, b))
        elif choice == 4: print("Result:", div(a, b))

    elif choice == 5:
        n = int(input("Enter a number: "))
        print("Factorial:", factorial(n))

    elif choice == 6:
        n = int(input("Enter n: "))
        print("Fibonacci:", fibonacci(n))

    elif choice == 7:
        n = int(input("Enter a number: "))
        print("Square:", square(n))

    elif choice == 8:
        n = int(input("Enter a number: "))
        print("Cube:", cube(n))

    elif choice == 9:
        n = int(input("Enter a number: "))
        print("Even?", is_even(n))

    else:
        print("Invalid choice! Try again.")
