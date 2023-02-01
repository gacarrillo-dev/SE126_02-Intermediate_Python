names = ["Sally", "Billy", "Gio", "Hank", "Dina", "John"]

length = len(names)
found = "False"

search = input("Enter a name ")

for pos in range(0, length):
    if(search == names[pos]):
        found = "True"
        position = pos
 
if found == "True":
    print(names[position])
else:
    print("Name not on list")

