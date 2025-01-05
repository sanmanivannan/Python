
def rec(num):

    if num >=9:
        return num + 1
    
    total = num+1
    print(total)
         
    return rec(total)


# nu = rec(3)

#return statement - return is used on the python fuctions, 
#                   functions send python values/objects back to the caller
#                   these values/objects are known as the functions return value     

#######################################

def fact(num):
    
    if num ==1:
        return num
    else:
        return num * fact(num-1)



factorialvalue = fact(5)
print(factorialvalue)
