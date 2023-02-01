# file          is the file stored in the location defined in open     
# row           is used to read one row at a time from file
#
# Notes:
#   row[0] refers to the first piece of data in the row --- id number
#   row[1] refers to the second piece of data in the row -- age
#   row[2] refers to the third piece of data in the row --- registered to vote
#   row[3] refers to the fourth piece of data in the row -- voted
# 
# Variables used:
#   id                      individuals ID number
#   age                     individuals age
#   registered              individual registered to vote
#   voted                   individual voted 
#   notEligibleToVote       individuals not eligible to vote
#   oldEnoughNotReg         individuals who are old enough to vote but did not register
#   eligibleToVoteNoVote    individuals who are eligible to vote but did vote
#   numberVoted             individuals who voted
#   records                 number of records processed
#   row                     represents a row in the csv file
#==========================================================================================

import csv

idList = []
ageList = []
regList = []
votedList = []

numberVoted = 0
notEligibleToVote = 0
oldEnoughNotReg = 0
eligibleToVoteNoVote = 0
numberVoted = 0
numRecords = 0


#===== Readins a CSV file into a list =====
with open(r"C:\Users\gcarr\Desktop\Local Git Repository\SE126_02-Intermediate_Python\w4_demo\DemoVote.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
      idList.append(row[0])
      ageList.append(int(row[1]))
      regList.append(row[2])
      votedList.append(row[3])

lastItem = len(ageList)
print(lastItem)
for col in range(12):
      if (ageList[col] < 18):
        notEligibleToVote = notEligibleToVote + 1

      if (ageList[col] >= 18 and regList[col] == "N"):
          oldEnoughNotReg = oldEnoughNotReg + 1

      if (regList[col] == "Y" and votedList[col] == "N"):
          eligibleToVoteNoVote = eligibleToVoteNoVote + 1
  
      if (votedList[col] == "Y"):
          numberVoted = numberVoted +1
      print(col)

      numRecords = numRecords + 1
        
print("Number of individuals not eligible to vote ", notEligibleToVote )
print("Number of individuals who are old enough to vote but have not registerered", oldEnoughNotReg)
print("Number of individuals who are eligible to vote but did not vote. ", eligibleToVoteNoVote)
print("Number of individuals who voted ", numberVoted)
print("Number of records process ", numRecords)






