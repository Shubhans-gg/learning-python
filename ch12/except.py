try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("No errors occurred!")    # runs only if no error
finally:
    print("This always runs!")      # runs no matter what

try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File doesn't exist!")
finally:
    print("Done!")