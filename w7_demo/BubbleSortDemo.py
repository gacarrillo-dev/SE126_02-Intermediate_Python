
def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp

def mySort(list1, list2):
    length = len(list1)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (list1[j] > list1[j + 1]):

                swap(list1, j)
                swap(list2, j)

#===== Main Program =====

names = ["Sam", "Carole", "Adam", "Bill", "Bobby", "Morgan", "Whitney", "Tom"]
ages = [30, 18, 22, 20, 23, 31, 19, 21]

for i in range(0, 8):
    print(names[i], " ", ages[i])
    
mySort(names, ages)

print("\n\nSorted list by names")
for i in range(0, 8):
    print(names[i], "  ", ages[i])

mySort(ages, names)
            
print("\n\nSorted list by ages")
for i in range(0, 8):
    print(names[i], "  ", ages[i])
