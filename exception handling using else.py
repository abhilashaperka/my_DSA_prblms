res = 0
x = int(input())
try:
    res = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except ValueError:
    print("Invalid input. Please enter a valid integer")
else:
    print("No error occurred")
    print(res)

# Using Exception class
# except Exception as e:
#     print(f"An error occurred: {e}")
#     print(res)


