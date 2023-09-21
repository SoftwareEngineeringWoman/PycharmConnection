friends=["sam","tom","ian", "polly", "trent"]
lucky_numbers=[3,5,8,45,78,100]
#extend function= append
friends.extend(lucky_numbers)
print(friends)
friends.append("creed")  #add an item end
print(friends)
friends.insert(1, "kelly",)  #add an item middle
print(friends)
friends.remove("polly")
print(friends)
friends.clear()   #empty list
print(friends)

fds=["sam","tom","ian", "polly", "trent"]
fds.pop()   # remove from end
print(fds)
print(fds.index("sam")) # to see if sam is on the lsit

#count number of similar items in the list
people=["sam","tom","ian","ian", "polly", "trent"]
print(people.count("ian"))

#sorting
people=["sam","tom","ian","ian", "polly", "trent"]
people.sort()
print(people)
people.reverse()
print(people)

#copy and create another list
people=["sam","tom","ian","ian", "polly", "trent"]
people2=people.copy()
print(people2)