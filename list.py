#Creating a list:
foods = ["Pineapple", 5, "Apple", "Banana", "Bread", "Bacon"]
colors = ["red", "blue", "green", "black", "white", "pink", "purple", "yellow"]
#Indexes:     0       1     2
#Accessing an certain item from the list "foods":
print(foods[1])
#Accessing the whole list:
print(foods)
#TIP: Indexes in lists start with 0.
#TIP: Trying to use the list backwards, you should use negative numbers to start from the last value.
#Picking the rest of the list's values, starting by this number:
print(foods[1:])
#Using a range like in for loops You start at this number, and end with this number. In the middle is a colon. It'll grab all the elements except for the last one.
print(foods[0:4])
#Replacing a thing's index position with another thing.
foods[4] = "Eggs"
print(foods[4])

#Functions:
#Extending the list
colors.extend(foods)
print(colors)
#Adding individual elements to a list:
colors.append("maroon")
print(colors)
#Adding and moving that element to a different position
colors.insert(2, "toad")
print(colors)
#Removing an element from a list
colors.remove("yellow")
print(colors)
#Removing every element from a list:
colors.clear()
print(colors)
#Removing the last element from a list:
colors = ["red", "blue", "green", "black", "white", "pink", "purple", "yellow"]
colors.pop()
print(colors)
#Telling the index of a element in a list:
print(colors.index("white"))
#Counting how many times does a element appear in the list:
colors = ["red", "blue", "green", "black", "white", "white", "pink", "purple", "yellow"]
print(colors.count("white"))
#Putting the list in ascending order
colors.sort()
print(colors)
#Reversing the list in opposite order
colors.reverse()
print(colors)
#Creating a new list with all the same elements as the list "colors"
colors2 = colors.copy()
print(colors2)