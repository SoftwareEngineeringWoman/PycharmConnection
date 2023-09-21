def say_hi():
    print("hello user")
print("Top")
say_hi()
print("Bottom")


#give info through parameters

def say_bye(name, age):
    print("bye "+name , " you are" +age)

say_bye("Mike", "40")
say_bye("Hanna", "19")

#return in function
#to perform function, call function by return, to give value/info


def cube(num):
    return num*num*num  #return breaks out of function, so can't write below it
result= cube(4)      #4 is parameter
print(result)