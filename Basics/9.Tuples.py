
# Tuples will always have the paranthesis and is like x and y coordinates, unlike the list has the square brackets 
# tuples are immutable(not able to change)

coordinates = (4,5)
print(coordinates[0])

# tuples within the list
coordinatelist = [(1,2),(3,4),(5,6)]

#creating a new tuple using the tuple constructor 
mytuple = tuple((1,2,3,4,5))
print(mytuple)

anothertuple = (68,7,8,19,22,122)
print(anothertuple)

tuplelist = list(anothertuple)
tuplelist.sort()
print(tuplelist)
print(type(tuplelist))


convertedbacktotuple = tuple(tuplelist)
print(convertedbacktotuple)
print(type(convertedbacktotuple))
