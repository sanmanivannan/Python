 
is_male = False
is_tall = True

if is_male and is_tall:
    print("you are both male and tall")
elif is_male and not (is_tall):
    print("you are male but not tall")
elif not(is_male) and is_tall:
    print("you are not male but tall")
else:
    print("you are neither male or tall")

     