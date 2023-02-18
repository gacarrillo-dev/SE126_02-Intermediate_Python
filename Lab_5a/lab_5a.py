# Gabriel Carrillo
# SE 126.02
# 02/17/2023
# Lab 5a
#
# Variables Declared
# 
# ipList                    List of IP addresses
# csvfile                   csv file containing list of ips
# ip_file                   read file 


import csv

ipList = []

#==== FUNCTIONS =====

# define function to print only class B ip addresses
def print_classB(ipList):
    for ip in ipList:
        octets = ip.split('.')
        if 128 <= int(octets[0]) <= 192:
            print(f"{ip}".ljust(15) + "255.255.0.0")
        


#==== MAIN PROGRAM =====

with open(r'C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\Lab_5a\Lab5a.csv') as csvfile:
    ip_file = csv.reader(csvfile)
    # load each row into ipList
    for row in ip_file:
        ipList.append(row[0])


# call function to print Class B ip
print_classB(ipList)
