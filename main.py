import math

choice = input("Dot product: DP, Cross product: CP ") 

coordinateOne = input("coordinate 1: ")
coordinateTwo = input("coordinate 2: ")

ints = ['-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
coorOneNum = []
coorTwoNum = []

for n in coordinateOne:
  if n in ints:
    n = int(n)
    coorOneNum.append(n)

for n in coordinateTwo:
  if n in ints:
    n = int(n)
    coorTwoNum.append(n)

def dotProduct(coorOne, coorTwo):
  return coorOneNum[0]*coorTwoNum[0]  + coorOneNum[1]*coorTwoNum[1] + coorOneNum[2]*coorTwoNum[2]

DP = dotProduct(coorOneNum, coorTwoNum)

#--------#

cpOne = [n for n in coorOneNum]*2
cpTwo = [n for n in coorTwoNum]*2

def crossProduct(cpOne, cpTwo):
  
  x = cpOne[1]*cpTwo[2]-cpOne[2]*cpTwo[1]
  y = cpOne[2]*cpTwo[3]-cpOne[3]*cpTwo[2]
  z = cpOne[3]*cpTwo[4]-cpOne[4]*cpTwo[3]

  return (x, y, z)

CP = crossProduct(cpOne, cpTwo)

if choice == "DP":
  print(DP)
elif choice == "CP":
  print(CP)
else:
  print("Please enter a valid choice")

  

