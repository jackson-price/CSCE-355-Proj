import sys

filename = sys.argv[1]

n = open(filename, "r")
characters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = ""

stateNumString = n.readline()
alphabetSizeString = n.readline()
acceptingStateString = n.readline()

#strip whitepace and get number of states
stateNumString = stateNumString.strip()
stateNumStripped = stateNumString[18:(len(stateNumString))]
stateNum = int(stateNumStripped)

#strip whitespace and get alphabet size
alphabetSizeString = alphabetSizeString.strip()
alphabetSizeStripped = alphabetSizeString[15:(len(alphabetSizeString))]
alphabetSize = int(alphabetSizeStripped)

#strip whitespace and get accepting states
acceptingStateString = acceptingStateString.strip()
acceptingStateStripped = acceptingStateString[18:(len(acceptingStateString))]
acceptingStates = acceptingStateStripped.split(" ")

#get actual alphabet characters
for x in range(alphabetSize):
	alphabet = alphabet + characters[x*2]

#create matrix of states
matrix = []
for x in range(stateNum):
	matrix.append([])

#populate matrix
for x in range(stateNum):
	transitions = n.readline()
	transitions = transitions.strip()
	tmpMat = transitions.split(" ")
	del tmpMat[0]
	z = 0
	for y in tmpMat:
		y = y.strip("{}")
		y = y.split(",")
		tmpMat[z] = y
		z += 1
	matrix[x] = tmpMat

#open input file
inputF = sys.argv[2]
inputR = open(inputF, "r")

#get input strings
inputStrings = inputR.readlines()

#decide if accepting or not and print
def accepting(state):
	if state in acceptingStates:
		return "accept"
	else:
		return "reject"

def test(inputs, tmpMat, state):
	if inputs == "":
		if(str(state) in acceptingStates):
			return "accept"
		else:
			return "reject"
	curr = inputs[0].strip()
	character = int(alphabet.index(curr))
	outcomes = []
	remaining = tmpMat[state][character]
	if remaining[0] == '':
		return "reject"
	else:
		for i in remaining:
			outcomes.append(test(inputs[1:], tmpMat, int(i)))
			if "accept" in outcomes:
				return "accept"
	if "accept" in outcomes:
		return "accept"
	else:
		return "reject"

for i in inputStrings:
	i = i.strip()
	printText = test(i, matrix, 0)
	print(printText)
