#In FOR loop we already define a universe interms of range,strings,list,tuples,sets,dictionary(definite list)

#for letter in "Manivannan Santharam":              #string
#    print(letter)
# 
friends = ["one","Two","Three","Four","Five"]       #list
for x in friends:
    print(x)

#

for x in "Shares":
    print(x)

# 
for index in range(10):
    print(index)
# 
for index in range(3,10):
    print(index)

# 
for index in range(0,101,5):
    print(index)    

#
friends = ["one","Two","Three","Four","Five"]
#print(len(friends))
for index1 in range(len(friends)):
    print(index1)

#nested for loop

letter = ["one","Two","Three","Four","Five"]   
num = ["1","2","3","4","5"]
for x in letter:
    for y in num:
        print(x,y) 
print("end of the nested loop")


#########################

fri = ["one","Two","Three","Four","Five"]       #list
for x in fri:
    if x == "Three":
        break
    print(x)

fri1 = ["one","Two","Three","Four","Five"]       #list
for x in fri1:
    if x == "Three":
        continue
    print(x)