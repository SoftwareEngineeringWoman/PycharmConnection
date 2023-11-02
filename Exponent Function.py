# allows to take a number and raise it to a power
#print(2**3)

# to create our own exp func

#create a func def
def raise_to_power(base_num, power_num):
    result=1
    for index in range(power_num):
        result =result*base_num
    return result

print(raise_to_power(3,2))

