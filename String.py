#Variable Strings:
phrase = "Guy"
#Put a new line between strings:
print("Brian Gao \n RULES!")
#Put quotation marks inside the string:
print(" \"Why?\" ")
#Print a backslash:
print("/")
#Print the variable called "phrase":
print(phrase)
#Adding another part into a string, or "Concatenation":
print(phrase + " is very chill.")

#Functions:
#Lower the case for the entire string
print(phrase.lower())
#Upper the case for the entire string
print(phrase.upper())
#Detect if the string is entirely lowercase or entirely uppercase
print(phrase.isupper())
print(phrase.islower())
#Turn the case lower or upper and ask if it is uppercase or lowercase
print(phrase.upper().isupper())
print(phrase.lower().islower())
#Find the length of this string
print(len(phrase))
#Pick an individual letter from a string, or specifying the index of a individual character from the string
print(phrase[2]) #0 is the first character of the a string, and so on
#Finding the position of a specific character in the string
print(phrase.index("u"))
#Or you can also find more than one character inside a string and it will tell where it starts
print(phrase.index("uy")) #Don't put letters inside the index function that is not in your string.
#Replace a part of the index with a different character or characters
print(phrase.replace("Gu", "Da"))