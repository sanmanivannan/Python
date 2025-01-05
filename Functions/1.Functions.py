#Functions
def name1():
   print("hello world!!")

name1()   

###########################################

def sum1(num1=0, num2=0):
   if (type(num1) is not int or type(num2) is not int):
      return   
   return num1+num2

total = sum1(5,'a')
print(total) 

##############################################

def multiple_num(*args):            #*args stores data a tuple
   print(args)
   print(type(args))

multiple_num("mani","ram", 5)   


############################################

def add1(*num):                    #*args/*num stores data a tuple
   sum = 0
   for x in num:
      sum += x 
   print(sum)


add1(4,6,7,8,9,43)

#################################################

def multi_names_items(**kwargs):      #kwargs is key word arguments will take dictionary
   print(kwargs)
   print(type(kwargs))

multi_names_items(first='Mani', second='Ram')

##############################################

def fun(a,b,*args, option =False, **kwargs):
   print("")
   print(a,b)
   print(args)
   print(option)
   print(kwargs)

fun(1,2,'mani','ram','vish', first = 'mckinney',second ='dallas')   

   