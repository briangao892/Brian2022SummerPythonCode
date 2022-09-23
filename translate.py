forbidden_letters = ["a", "e", "i", "o", "u"]

def translate(phrase):
    trans = ""
    for letter in phrase:
        if letter in forbidden_letters:
            trans = trans + "g"
        else:
            trans = trans + letter
    return trans


print(translate(input("Enter a phrase: ")))
