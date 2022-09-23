name = "Brian"
name = name.lower()
sentence = "Welcome USA"
letters = {
    "A":"a",
    "B":"b",
    "C":"c",
    "D":"d",
    "E":"e",
    "G":"g",
    "H":"h",
    "I":"i",
    "J":"j",
    "K":"k",
    "L":"l",
    "M":"n",
    "O":"o",
    "P":"p",
    "Q":"q",
    "R":"r",
    "S":"s",
    "T":"t",
    "U":"u",
    "V":"v",
    "W":"w",
    "X":"x",
    "Y":"y",
    "Z":"z"
}
vowels = ["a", "e", "i", "o", "u"]
newsent = ""
for i in name:
    if i in vowels:
        name = name.replace(i, "")
print(name)
for i in sentence:
    if i in letters.keys():
        newsent = newsent + letters[i]
    else:
        newsent = newsent + i
print(newsent)