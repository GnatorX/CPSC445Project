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

def getStemLoopTrees(sequence):
	StemLoopTrees=[]
	StemLoopTree=[]
	loopTypeP="Interior loop"
	firstLine=True
	previousPosition=(0,0)
	end=False
	for line in sequence:
		line = line.rstrip()
		line=line.split(';')
		item= line[0].split()
		print len(line)
		if len(line)==2:
			item2=line[1].split()
		else:
			end=True
		loopType=item[0]+" " +item[1]
		if loopType == loopTypeP:
			position=item[3].split(',')
			#print position,previousPosition
			if not firstLine:
				if position[0] in previousPosition and position[1] in previousPosition:
					p = item2[1].split(',')
					item2[3]=item2[3].translate(None,':')
					previousPosition=(p[0],p[1],item2[3])
					item[5]=item[5].translate(None,':')
					StemLoopTree.append((position[0],position[1],item[5]))
				else:
					item2[3]=item2[3].translate(None,':')
					StemLoopTree.append((previousPosition[0],previousPosition[1],item2[3]))				
					StemLoopTrees.append(StemLoopTree)
					StemLoopTree=[]
					item[5]=item[5].translate(None,':')				
					StemLoopTree.append((position[0],position[1],item[5]))
					end=False
					firstLine=True
				
				
			else:
				item[5]=item[5].translate(None,':')	
				StemLoopTree.append((position[0],position[1],item[5]))
				p = item2[1].split(',')
				item2[3]=item2[3].translate(None,':')
				previousPosition=(p[0],p[1],item2[3])
				firstLine=False
		if end :
			if len(StemLoopTree)>0:
				StemLoopTree.append(previousPosition)
			else:
				position=item[3].split(',')
				item[5]=item[5].translate(None,':')
				StemLoopTree.append((position[0],position[1],item[5]))
			StemLoopTrees.append(StemLoopTree)
			StemLoopTree=[]	
			end=False
			firstLine=True
	
	return 	StemLoopTrees
#def getKnownSequence(fileData):
	

unknownSequence=[]
unknownSequence,unknownInfo,j=getSequence(sequenceFileData,0)
unknownStemLoopTrees=getStemLoopTrees(unknownSequence)

#print unknownStemLoopTrees
knownSequences=[]
knownInfos=[]

#print unknownSequence
i=0
knownSequenceStemLoopTrees=[]
while i<len(compareFileData):
	knownSequence,knownSequenceInfo,i=getSequence(compareFileData,i)
	knownSequences.append(knownSequence)
	knownInfos.append(knownSequenceInfo)
	k = getStemLoopTrees(knownSequence)
	knownSequenceStemLoopTrees.append(k)

print knownSequenceStemLoopTrees


