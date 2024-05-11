res=0
x=int(input())
try:
    res=10/x
except ZeroDivisionError:
    print("error:division by zero error occured")
print(res)
