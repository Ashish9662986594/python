
a = 5
b = 4

try:                             #When you know this print the error but also you tell the system try it then we write it
    print("Open resources")
    print(a/b)
    k = int(input("Enter the number : "))    #When ypu put the string then this is ask the num 14 line
    print(k)

except ZeroDivisionError as e:                                           #e is also representetor its show you the error 
    print("Hey , You can not divide a number by zero", e)         #When you do diffrent type of error then this also ask you

except ValueError as e:
    print("Invalid Input")        

except Exception as e:
    print("Something went wrong...")

finally:
    print("Close resources")

