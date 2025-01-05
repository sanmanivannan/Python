#sets
nums = {1,2,3,4,5}
nums2 = set((6,7,8,9,10))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))

#No Duplicate allowed in SETS

num = {1,2,3,4,4}
print(num)

nu = {1,True,2,34, False, 0}
print(nu)

#check values in the set

print(2 in nu)

#You cant refer to an element in the set with an INDEX position or keys

#updting a new element in the set

print(nu.add(999))
print(nu)

#adding elements from one set to another set (not only sets, even the tuple,list,dictionary can be added to a new set)
morenum = {34,565,343}
num.update(morenum)
print(num)

#(not only sets, even the tuple,list,dictionary can be added to a new set) --Eg:

#num.update(tuple)
#print(num)

#num.update(list)
#print(num)

#merging 2 sets
n1 = {1,2,3,4}
n2 = {3,4,5,6,7,8}

newset = n1.union(n2)
print(newset)

#keep only the intersection

intersec = n1.intersection(n2)
print(intersec)


intersec1 = n1.symmetric_difference_update(n2)
print(intersec1)
