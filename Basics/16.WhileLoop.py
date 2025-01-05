# a while loop is executing the set of statements as long as the condition is true

# while this_condition_true/valid:
#   do this    
'''
i=0
while i <= 10:
    print(i)
    i += 1

print("out of the loop")  '''  


"""i=0
while i <= 10:
  print(i)
  if i == 3:
    break
  i += 1


print("out of the loop2")  """

i=0
while i <= 10:
    i += 1
    if i == 3:
        continue
    print(i)

print("out of the loop3")  