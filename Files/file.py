import os
# r=Read
# a=Append
# w=Write
# x=Create

#f = open("C:\\Users\\sanma\\Python\\Files\\test.txt")

#print(f.read()) # just read function would read the entire file

#print(f.read(4)) # will read only the 1st 4 character on the file

#print(f.readline()) # will read the entire line

'''
for line in f:
    print(line) 

'''
# f.close()
########################################################
'''
#default Reading the file
try:
    f = open("C:\\Users\\sanma\\Python\\Files\\test.txt")
    print(f.read())
except:
    print("file doesnt exists")
finally:
    f.close()

'''
############################################################
'''
#Appending the file(if exixst) or creates a new file if that doesnt exists
f = open("C:\\Users\\sanma\\Python\\Files\\test1.txt", "a")
f.write("line 4\n")
f.close()
'''
###############################################################
'''
#Write/Overwrite the file
f = open("C:\\Users\\sanma\\Python\\Files\\test.txt", "w")
f.write("deleted the original content as I used write operation \n")
f.close()
'''
###############################################################
'''
#Create the file (Creates a new file if that doesnt exists)
f = open("C:\\Users\\sanma\\Python\\Files\\content.txt", "x")
f.write("new file")
'''
'''
#created the new file if thats not already exists
if not os.path.exists("C:\\Users\\sanma\\Python\\Files\\content1.txt"):
    f = open("C:\\Users\\sanma\\Python\\Files\\content1.txt", "x")
    f.write("new file created after checking the if condition")
   
'''
################################################################

#Deleting the file
'''
if os.path.exists("C:\\Users\\sanma\\Python\\Files\\content1.txt"):
    os.remove("C:\\Users\\sanma\\Python\\Files\\content1.txt")
'''
##############################################################


#with operation, has built-in implicit exception handling close() will be automatically called
'''
#reading from one file and copying to another file
with open("C:\\Users\\sanma\\Python\\Files\\content1.txt") as f:
    content = f.read()

with open("C:\\Users\\sanma\\Python\\Files\\content2.txt", "w") as f:
    f.write(content)

'''    