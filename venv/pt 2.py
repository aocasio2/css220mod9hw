# Problem 2: Fibonacci number with user input

def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

user_input = int(input("Enter the Fibonacci number you want to compute: "))

result = fibonacci(user_input)
print(f"The {user_input}th Fibonacci number is {result}.")
