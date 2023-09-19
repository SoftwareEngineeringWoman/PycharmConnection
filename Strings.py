phrase= "Good Morning Saira"
print(phrase)
phrase= "Good Morning\nSaira"
print(phrase)
phrase= "Good Morning\nSaira"
print(phrase+" Walia")    #append/concatenate

#function helps us modify string or get info about string

phrase= "Good Morning\nSaira"
print(phrase.lower())

phrase= "Good Morning\nSaira"
print(phrase.isupper())   #the whole string is not upper

phrase= "Good Morning\nSaira"
print(phrase.upper().isupper())

phrase= "Good Morning\nSaira"
print(len(phrase))

phrase= "Good Morning\nSaira"
print(phrase[7])       #index starts from zero

#where charecter is located in a string

phrase= "Good Morning\nSaira"
print(phrase.index("G"))

phrase= "Good Morning\nSaira"
print(phrase.index("od"))    #where it starts


phrase= "Good Morning\nSaira"
print(phrase.replace("Good", "Elephant"))


