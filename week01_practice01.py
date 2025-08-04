
num_input = input("Enter a non-negative integer: ")


try:
    num = int(num_input)

    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        n = num
        while n > 1:
            factorial *= n
            n -= 1

        print(f"The factorial of {num} is: {factorial}")

except ValueError:
    print("Invalid input: Please enter an integer.")
