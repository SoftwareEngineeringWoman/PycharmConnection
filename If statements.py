is_male= True
if is_male:
    print("You are a male") #if false, won't print anything
else:
    print("You are not a male")



is_male= True
is_tall= False
if is_male and is_tall:  #or operator
    print("You are a male or tall") #if false, won't print anything
elif is_male and not(is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are a short male")
else:
    print("You are not a male nor tall")



#comparison if statements

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2 >=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))


