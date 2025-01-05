"""# Scope - Global variable, local variable both from the function and non-function prespective

name = "mani"  #global variable
#print(name)

def name1(last_name):
    age = 30
    print(name)
    print(age)
    print(last_name)

name1("lastme")

#################################


name = "mani"  #global variable
#print(name)

def name1(name):
    age = 30
    print(name)
    print(age)
    print(name)

name1("lastme") #local variable will override the global variable, as we pass the argument on the function
print(name)  #this line will print the value of the global variable, as this is not on the function
##########################################

name = "mani"  #global variable

def name1(name):
    age = 30
    print(name)
    print(age)
    

name1("lastme") #local variable will override the global variable, as we pass the argument on the function
print(name)  #this line will print the value of the global variable, as this is not on the function



def name2():
    print("")
    name1("second function")  #calling the above function name1 in this new function name2

name2()

##########################################


new = "mani"  #global variable

def name2():   #function within function
    print("")
    def name1(name):   #function within function
        age = 30
        print(name)
        print(age)
        
    name1("schoo")
 
name2()"""

############################################

name="mani"
age =20

def first():
    global age   # picks the value of age from the global variable
    age += 2
    color = 'yellow' 
    def second(name):
        print(name)  #picks the name from the argument from the function and NOT from global variable
        print(age) #picks the age from gloabl variable
        print(color) #picks the color from first function
    second('new name')

first()    

#########################################

name="mani"
age =20

def first():
    global age   # picks the value of age from the global variable
    age += 2
    color = 'yellow' 
    def second(name):
        color = 'red' 
        print(name)  #picks the name from the argument from the function and NOT from global variable
        print(age) #picks the age from this function specific variable and gloabl variable
        print(color) #picks the color from first function
    second('new name')

first() 

#############################################

name="mani"
age =20

def first():
    global age   # picks the value of age from the global variable
    age += 2
    color = 'yellow' 
    def second(name):
        nonlocal color  #nonlocal is used, if you want to reuse/modify the variable value from parent function
        color = 'red' 
        print(name)  #picks the name from the argument from the function and NOT from global variable
        print(age) #picks the age from this function specific variable and gloabl variable
        print(color) #picks the color from first function
    second('vishnu')

first() 

