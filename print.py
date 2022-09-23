print("Hello ", end="")
print("World!")
print("Cat", "Dog", 'Mice', sep= ",")
Age = 0
stuff = 0
def Brian_Function():
    global Age
    if inputs == "brian":
        Age = Age + 1
        print("Brian Count: "+str(Age))
    else:
        print("Not Brian")
def Chloe_Function():
    print(inputs)
    if inputs == "chloe":
        Age = Age + 1
        print("Chloe Count: "+str(Age))
    else:
        print("Not Chloe")

def main():
    print("VOTE BRIAN FOR PRESIDENT! CHLOE SHMOE!!! Actually, I couldn't find any rhymes for Chloe Stinks.")
    print("VOTE CHLOE FOR PRESIDENT! BRIAN IS LYIN!!!! Actually, I couldn't find any rhymes for Brian Stinks.")

    while stuff == 0:
        inputs = input("Print Brian, the handsome knight, or Chloe, the dog: ")
        inputs = inputs.lower()
        if inputs == "brian":
            Brian_Function()
        if inputs == "chloe":
            Chloe_Function()

if __name__ == "__main__":
    main()

