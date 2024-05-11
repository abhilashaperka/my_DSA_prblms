def calculate_sqr_root(num):
    if num<0:
        raise ValueError("input must be a non negative number")
    return num**0.5
try:
    user_input=float(input("enter a number:"))
    result=calculate_sqr_root(user_input)
    print("srt root of a given number:",result)
except ValueError as ve:
    print("error: ve")
except Exception as e:
    print("calculation successful")
finally:
    print("program execution completed")