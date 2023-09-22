#stored info in key value pairs
#to access, use key
#unique keys
#get gives a default none if invalid key
# to replace none with other text, use comma and write it

MonthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
print(MonthConversion.get("Luv"))

print(MonthConversion.get("Luv", "Not a valid key"))
