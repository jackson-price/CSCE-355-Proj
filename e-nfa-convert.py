import sys

language = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

fname = sys.argv[1]
inputF = open(fname, "r")

stateNumString = inputF.readline()
stateNumString = stateNumString.strip()
stateNum = int(stateNumString[18:(len(stateNumString))])

alphaLengthString = inputF.readline()
alphaStrip = alphaLengthString.split(":")
alphaLength = alphaStrip[1].strip()
alphabet = ""
for i in range(int(alphaLength)):
	alphabet = alphabet + language[i] + " "

acceptingString = inputF.readline()
acceptingString = acceptingString.strip()
accepting = acceptingString[18:(len(acceptingString))]
accepting = accepting.split()
for i in range(len(accepting)):
	accepting[i] = int(accepting[i])

#print(stateNum)
#print(alphabet)
#print(accepting)

transMat = [0]*stateNum

for i in range(stateNum):
	line = inputF.readline()
	transMat[i] = line.split()

bracketTrans = transMat

for i in range(stateNum):
	for j in range(1+int(alphaLength)):
		transMat[i][j] = transMat[i][j].replace("{","").replace("}","")

eClosureList = []

def eclose(state, i):
	eClosure = []
	if transMat[state][0] == '':
		eClosure.append(int(state))
		if i == state:
			eClosureList.append(eClosure)
	else:
		if state == 0:
			accepting.append(state)
		eClosure.append(state)
		eTrans = transMat[state][0].split(",")
		for j in eTrans:
			eClosure.append(j)
			eclose(int(j), i)
		eClosureList.append(eClosure)

#find all eclosures
for i in range(stateNum):
	eclose(i, i)

for i in range(stateNum):
	for j in range(len(eClosureList[i])):
		if (int(eClosureList[i][j]) in accepting):
			accepting.append(i)

accepting.sort()
accepting = list(dict.fromkeys(accepting))

newTrans = transMat
incomingE = []
sourceE = []

for i in range(stateNum):
	if transMat[i][0] != '':
		for j in range(1, int(alphaLength)+1):
			if len(str(transMat[i][0])) > 1:
				splitE = transMat[i][0].split(",")
				for k in splitE:
					temp = int(k)
					newTrans[i][j] = newTrans[i][j]+str(transMat[int(temp)][j]+",")
				newTrans[i][j] = newTrans[i][j].rstrip(",")
			else:
				if transMat[i][0] == '':
					transMat[i][0] = 0
				temp = int(transMat[i][0])
				newTrans[i][j] = transMat[temp][j]
			newTrans[i][0] = ''
	else:
		for j in range(1, int(alphaLength)):
			newTrans[i][j] = transMat[i][j]

print("Number of states: " + str(stateNum))
print("Alphabet size: " + alphaLength)
print("Accepting states: " + ' '.join(map(str, accepting)))

for i in range(stateNum):
	for j in range(int(alphaLength)+1):
		print("{" + newTrans[i][j] + "}", end = "	")
	print()














