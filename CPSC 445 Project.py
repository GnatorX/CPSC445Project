import sys

knownSequences=[]
sequenceFile=sys.argv[1]
compareFile=sys.argv[2]

sequenceFileData=open(sequenceFile,'r')
compareFileData=open(compareFile,'r')

sequenceFileData=sequenceFileData.readlines()
compareFileData=compareFileData.readlines()
def getSequence(fileData,i):
	sequence = []
	structure= []
	s = fileData[i]
	if s.startswith('>'):
		i=i+1
		s=fileData[i]
	s = s.rstrip()
	for item in s:
		sequence.append(item)
	i=i+1
	s = fileData[i]
	s=s.rstrip()
	for item in s:
		structure.append(item)
	return sequence,structure

#def getKnownSequence(fileData):
	

unknownSequence=[]
unknownStructure=[]
unknownSequence,unknownStructure=getSequence(sequenceFileData,0)

knownSequences=[]
knownStructures=[]
#print unknownSequence,unknownStructure
#print unknownSequence
for i in range(0,len(compareFileData)-2):
	sequence = []
	structure= []
	s = compareFileData[i]
	if s.startswith('>'):
		i=i+1
		s=compareFileData[i]

	s = s.rstrip()
	for item in s:
		sequence.append(item)
	i=i+1
	s = compareFileData[i]
	s=s.rstrip()
	for item in s:
		structure.append(item)
	knownSequences.append(sequence)
	knownStructures.append(structure)
#print knownSequences[0],knownStructures[0]

########################################################################################################################
#Obtain stem loops






