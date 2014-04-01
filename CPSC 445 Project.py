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
	info=' '
	s = fileData[i]
	if s.startswith('>'):
		info=s		
		i=i+2
		s=fileData[i]
		s=s.rstrip()
	while   s.startswith('>')!=True and s:
		sequence.append(s)
		i=i+1
		if i>=len(fileData):
			break
		s=fileData[i]
		s = s.rstrip()
	return sequence,info,i+1

#def getKnownSequence(fileData):
	

unknownSequence=[]

unknownSequence,unknownInfo,j=getSequence(sequenceFileData,0)


knownSequences=[]
knownInfos=[]

#print unknownSequence
i=0
while i<len(compareFileData):
	knownSequence,knownSequenceInfo,i=getSequence(compareFileData,i)
	knownSequences.append(knownSequence)
	knownInfos.append(knownSequenceInfo)
	
#print knownSequences[0]

