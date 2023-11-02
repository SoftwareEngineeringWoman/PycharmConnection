# loop over collection of items
#array, letter in string or series of numbers
#variable letter will have different values every time we go through loop / iteration
# after in, we put a collection, in this example it is string "Girrafe..."


#this says, for every letter in Freecode Academy we want to perform something
for letter in "Freecode Academy":
    print(letter)

#Array collection
friends=["Jim","Tom","Sam","Joe","Mat"]
for friend in friends:
    print(friend)

#series of numbes as collection (starts from 0)
for index in range(10):
    print(index)

for indexs in range(3,10):
    print(indexs)

friends = ["Jim", "Tom", "Sam", "Joe", "Mat"]
for index in range(len(friends)):
    print(friends[index])


for index in range(5):
    if index ==0:
        print("1st Iteration")
    else:
        print("Not 1st")