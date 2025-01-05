letter = ["one","Two","Three","Four","Five"]   

for x in letter:
    print(x)
    if x == "Three":            #break (controlflow just breaks out the code after the condition)
        break
print("end of the loop")


letter1 = ["one","Two","Three","Four","Five"]   

for y in letter1:
    if y == "Three":            #continue (controlflow just skips that element)
        continue        
    print(y)
    
print("end of the loop")