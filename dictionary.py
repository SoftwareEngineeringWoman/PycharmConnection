#stored info in key value pairs
#to access, use key
#unique keys
#get gives a default none if invalid key
# to replace none with other text, use comma and write it
#normal dictionary= word and meaning ... word is key
#below we create a dic to convert month name to shorter name

MonthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
print(MonthConversion["Feb"])

print(MonthConversion.get("Luv"))
# this adds default value
print(MonthConversion.get("Luv", "Not a valid key"))

