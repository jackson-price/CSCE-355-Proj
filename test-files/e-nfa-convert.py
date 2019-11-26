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

transMat = [0]*stateNum

for i in range(stateNum):
	line = inputF.readline()
	transMat[i] = line.split()

bracketTrans = transMat
eClosureList = []

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
eclose(0, 0)

accepting.sort()
accepting = list(dict.fromkeys(accepting))

newTrans = transMat
incomingE = []
sourceE = []

#assign new transition
def newTransitions(state, character):
	for i in eClosureList:
		if i[0] == state:
			if len(i) > 1:
				return newTransitions(i[1], character)
			else:
				return transMat[state][character]

for i in range(stateNum):
	if len(transMat[i][0]) > 0:
		for j in range(1, int(alphaLength)+1):
			splitE = transMat[i][0].split(",")
			for k in splitE:
				temp = int(k)
				if len(str(transMat[int(k)][0])) == 0:
					newTrans[i][j] = newTrans[i][j] + str(transMat[int(temp)][j]) + ","
				else:
					tmp = newTransitions(i, j)
					newTrans[i][j] = newTrans[i][j] + str(tmp) + ","
			newTrans[i][j] = newTrans[i][j].rstrip(",")
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














