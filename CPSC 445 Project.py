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
		#print len(line)
		if len(line)==2:
			item2=line[1].split()
		else:
			end=True
		loopType=item[0]+" " +item[1]
		if loopType == loopTypeP:
			position=[int(x) for x in item[3].split(',')]
			#print position,previousPosition
			if not firstLine:
				if position[0] in previousPosition and position[1] in previousPosition:
					p = [int(x) for x in item2[1].split(',')]
					item2[3]=item2[3].translate(None,':')
					previousPosition=(p[0],p[1],item2[3],list(),list(),False)
					item[5]=item[5].translate(None,':')
					StemLoopTree.append((position[0],position[1],item[5],list(),list(),False))
				else:
					item2[3]=item2[3].translate(None,':')
					StemLoopTree.append((previousPosition[0],previousPosition[1],item2[3],list(),list(),False))				
					StemLoopTrees.append(StemLoopTree)
					StemLoopTree=[]
					item[5]=item[5].translate(None,':')				
					StemLoopTree.append((position[0],position[1],item[5],list(),list(),False))
					end=False
					firstLine=True
				
				
			else:
				item[5]=item[5].translate(None,':')	
				StemLoopTree.append((position[0],position[1],item[5],list(),list(),False))
				p = [int(x) for x in item2[1].split(',')]
				item2[3]=item2[3].translate(None,':')
				previousPosition=(p[0],p[1],item2[3],list(),list(),False)
				firstLine=False
		if end :
			if len(StemLoopTree)>0:
				previousPosition=(previousPosition[0],previousPosition[1],previousPosition[2],previousPosition[3],previousPosition[4],True)
				StemLoopTree.append(previousPosition)
			else:
				position=[int(x) for x in item[3].split(',')]
				item[5]=item[5].translate(None,':')
				StemLoopTree.append((position[0],position[1],item[5],list(),list(),False))
			StemLoopTrees.append(StemLoopTree)
			StemLoopTree=[]	
			end=False
			firstLine=True
	
	return 	StemLoopTrees

def addLeaves(stemLoopTrees):
	for tree in stemLoopTrees:
		curLeft=0
		curRight=0
		first=True
		
		for num in range(0,len(tree)):
			if first:
				curLeft=tree[num][0]
				curRight=tree[num][1]
				first=False
			else:
				if tree[num][0]-1!=curLeft:
				#	print "sdfds"
					for numK in range(curLeft+1,tree[num][0]):
						tree[num-1][3].append(numK)
				if tree[num][1]!=curRight-1:
					print "sfsfs",str(tree[num][1])
					for numK in range(tree[num][1]+1,curRight):
						tree[num-1][4].append(numK)
				curLeft=tree[num][0]
				curRight=tree[num][1]
	return stemLoopTrees


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

unknownStemLoopTrees=addLeaves(unknownStemLoopTrees)
print unknownStemLoopTrees

