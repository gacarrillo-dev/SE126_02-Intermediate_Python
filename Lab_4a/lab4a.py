# SE126.02
# Gabriel Carrillo
# 02/01/2023
# Lab 4a
#
# Variables Declared:
# ===================
# file                      is the file store in the locaiton defined in open
# row                       used to read one row at a time from the file
# typeList = []             list of type computers
# brandList = []            list of brand computers
# cpuList = []              list of cpu computers
# ramList = []              list of computers' ram
# firstDiskList = []        list of computers' first disk
# numHddList = []           list of computers' number of hardrives
# secondDiskList = []       list of computers' second disk
# osList = []               list of computers' operating system
# yearList = []             list of computers' year of manufacturer
# ramComputers = 0          number of computers with ram greater than 8GB




import csv

typeList = []
brandList = []
cpuList = []
ramList = []
firstDiskList = []
numHddList = []
secondDiskList = []
osList = []
yearList = []
ramComputers = 0

#===== FUNCTIONS =======

# function to search list for ram greater than 8GB
def search_ram(ramList):
    ramComputers = 0
    for ram in ramList:
       if ram > 8:
           ramComputers += 1
    return ramComputers

                
#==== MAIN PROGRAM ======

# open csv file and parse the records from the csv file
with open (r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_4a\lab4a.csv") as csvfile:
    file = csv.reader(csvfile)
    # add each row from file to a each list of records
    for row in file:
        typeList.append(row[0])
        brandList.append(row[1])
        cpuList.append(row[2])
        ramList.append(int(row[3]))
        firstDiskList.append(row[4])
        numHddList.append(int(row[5]))
        # if row has 1 disk then add a placeholder for secondDiskList
        if int(row[5]) == 1:
            secondDiskList.append("")
            osList.append(row[6])
            yearList.append(row[7])
        else:
            secondDiskList.append(row[6])
            osList.append(row[7])
            yearList.append(row[8])

# run search ram function and return the results in ramComputers variable
ramComputers = search_ram(ramList)

# print results
print(f"There are {ramComputers} computers with ram greater than 8GB.")