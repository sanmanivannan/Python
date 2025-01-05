'''try:
    number = int(input("Enter the Number: "))
    print(number)

except:
    print("Invalid Entry")
'''
try:
    value = 10/0
    #number = int(input("Enter the Number: "))
    #print(number)
    print(str(value))

except ValueError as err:
    print(err)

except ZeroDivisionError:
     print("ZeroDivisionErr: please dont try to dive a number by 0")

else:           #if there is no error/exception, else block will execte 
    print("no error, so executig the else block")

finally:
    print("Finally block will print with or without error")    

