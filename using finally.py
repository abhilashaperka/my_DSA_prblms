try:
    file=open("C:\Users\abhi\Desktop\python\exception handling")
    content=file.read()
    print("file content:",content)
except FileNotFoundError:
    print("file not found")
finally:
    file.close() if 'file' in locals() else None
    print("successfully closed the file")

#using else 
"""
else:
    content=file.read()
    print("file content:",content)

"""

