Conversions = {
    "Jan" : "January",
    "Feb" : "Febuary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
#Ways to get the definition of the abr
#I can set a default value if not in dicitonary with this way:
print(Conversions.get("Dec", "Hello"))
#The Simple Way:
print(Conversions["Dec"])
Conversions.get("Hello")
Conversions.update({"Jan":"June", "Feb" : "Febu"})
del Conversions["Dec"]
print(Conversions)
Age = Conversions.pop("Aug")
print(Age)
print(Conversions.keys())
print(Conversions.values())
print(Conversions.items())
for key, values in Conversions.items():
    print(key, values)