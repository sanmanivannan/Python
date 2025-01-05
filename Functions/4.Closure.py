# Closure is a function having access to the scope of its parent functions
# after the parent function has returned.

def parent_function(person,coins):
  # coins =3
    
    def play_game():
        nonlocal coins  #using the parent function(scope) variable and modify
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")
        elif coins ==1:
            print("\n" + person + " has " + str(coins) + " coin left. ")
        else:
            print("\n" + person + " has no coin left. ")
        
    return play_game   


tommy = parent_function("Tommy",3)
jonny = parent_function("Jonny",3)

tommy()
tommy()

jonny()

###############################################

def num1(n1):
    def num2(n2):
        return n1 * n2
    return num2

multipleof5 = num1(5)

multipleof3 = num1(3)


print(multipleof3(3))

print(multipleof5(8))

