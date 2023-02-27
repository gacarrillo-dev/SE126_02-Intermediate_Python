
def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp

def mySort(list1, list2, list3):
    length = len(list1)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (list1[j] > list1[j + 1]):

                swap(list1, j)
                swap(list2, j)
                swap(list3, j)

#===== Main Program =====

tempList = []
first = ["Sam", "Carole", "Adam", "Bill", "Bobby", "Morgan", "Whitney", "Tom"]
last = ["Thompson", "Derby", "Jones", "Thompson","Horan", "Derby", "Jones", "Smith"]

length = len(last)

for i in range(0, length):
    tempList.append(last[i] + first[i])


mySort(tempList, last, first)

for i in range(0, length):
    print(tempList[i])

print("\n\n")
for i in range(0, length):
    print(last[i], "  ", first[i])

