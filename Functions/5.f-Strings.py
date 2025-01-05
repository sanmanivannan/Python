#f Strings

name = "mani"
age = 30

#f-string format
message = f"\n my name is {name} and my age is {age}"
print(message)

#using the operations
message = f"\n my name is {name} and my age is {10*4}"
print(message)

#calling the methods
message = f"\n my name is {name.upper()} and my age is {10*4}"
print(message)

#pass formatting options
#1
num =3
print(f"2.25 times the {num} is : {num*2.25}")

#2
for n in range(1,11):
    print(f"2.25 times the {n} is : {n*2.25}")