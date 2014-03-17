import sys

knownSequences=[]
sequenceFile=sys.argv[1]
compareFile=sys.argv[2]

sequenceFileData=open(sequenceFile,'r')
compareFileData=open(compareFile,'r')


def getSequence(fileData):	
	sequence = []
	structure= []
	s = fileData.readline()
	if s.startswith('>'):
		s=fileData.readline()
	s = s.rstrip()
	for item in s:
		sequence.append(item)
	s = fileData.readline()
	s=s.rstrip()
	for item in s:
		structure.append(item)
	return sequence,structure

unknownSequence=[]
unknownStructure=[]
unknownSequence,unknownStructure=getSequence(sequenceFileData)

knownSequences=[]
knownStructures=[]

#print unknownSequence
for num in range(0,len(compareFileData)):
	kSe,kSt=getSequence(compareFileData)
	knownSequences.append(kSe)
	knownStructures.append(kSt)
print knownSequences

