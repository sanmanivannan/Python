
#dictionary will always have key and value pair
monthConversion = {
  "Jan": "January",
  "Feb": "Feduary",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "Novermber",
  "Dec": "December"
 }

print(monthConversion["Mar"])

print(monthConversion.get("Dec"))

print(monthConversion.get("Aug","Not a valid entry"))

#creating dictionary using the dict constrcutor function
car = dict({"brand":"Tesla",
             "model":"model_3"})
print(car)
print(type(car))
print(len(car))

#ACCESS THE items from dictionary

print(car["brand"])

print(car.get("brand"))

#list of all keys
print(car.keys())
#list of all value
print(car.values())
#list of all in the form of tuples
print(car.items())

print(type(car.items()))

#verify a key exists

print("brand" in car)

#change values
car["brand"] = "Nio"
car.update()

#adding the new ket and value

car.update({"price" : 10000})
print(car)


#removing items

print(car.pop("price"))
print(car)

car["EV"] = "yes"
print(car)


print(car.popitem())
print(car)

#delete and clear

car.update({"price":"10000"})
print(car)

#print(car.clear())

#copyig the dictonary

car2 = car.copy()
car2["EV"] = "Yes"
print("###############")
print(car2)


car3 = dict(car2)
print("###############")
print(car3)


#Nested Dictionary
mem1 = {
    "name" : "earth",
    "disctance" : 1000
}

mem2 = {
    "name" : "mars",
    "disctance" : 3333
}

newmem = {
    "mem1" : mem1,
    "mem2" : mem2
}

print(newmem)

