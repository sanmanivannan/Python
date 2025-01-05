numbers = [31,2,43,455,5,76,7,8,91,0]

friends = ["name1","name2","name3","name4","name5","name5","name7","name8","name9","name10"]

print(friends.index('name4'))


# copying the list to another list
friends2 = friends.copy()

# extending next list
friends.extend(numbers)

friends.extend(['Mani'])

friends += ['Ram']

# appending the list
friends.append("name11")

# inserting the list values with the index value
friends.insert(1, "zzzzz")

# removing the value from the list
friends.remove("name1")

###############
friends2.insert(1,"Manivannan")
print(friends2)
##################
friends2[2:2] = ['one','two']
print(friends2)
##################
friends2[2:3] = ['three','four']
print(friends2)



# friends.clear

# kicking out the last value from the list
friends.pop()

# knowing the index value on the list
friends.index("name4")

# counting the "name5" in the list
friends.count("name5")



# sorting the list in the ascending order
# friends.sort()   #not sure if its working as its the string

# numbers.sort()

# sorting the reverse order

# friends.reverse   #not sure if its working as its the string

numbers.reverse()

numbers.sort() 

numbers.sort(reverse=True)

#########################

nums = [3,6,8,687,56,43,2]
print(sorted(nums,reverse=True))
print(sorted(nums))
#######################
numcopy = nums.copy()
# or
mynum = list(nums)

##----------------------------------creating a list using the list constructor

mylist = list([1,2,3,4,5])
print(mylist)

