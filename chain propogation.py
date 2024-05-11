class CustomException(Exception):
    pass

def function_a():
    try:
        res = 10 / 0
        print("result:", res)
    except ZeroDivisionError as e:
        print("Error in function_a:", e)
        raise CustomException("Custom exception raised in function_a") from e

def function_b():
    function_a()

try:
    function_b()
except CustomException as e:
    print("Error in function_b:", e)


