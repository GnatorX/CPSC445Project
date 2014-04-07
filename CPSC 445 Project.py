import sys
import numpy
from DP import findMin
from DP import getIndexingPairs
from parser import runRNAEval
knownSequences=[]
sequenceFile=sys.argv[1]
compareFile=sys.argv[2]

sequenceFileData=open(sequenceFile,'r')
compareFileData=open(compareFile,'r')
unknownBaseSequence=''
sequenceFileData=sequenceFileData.readlines()
compareFileData=compareFileData.readlines()

def getSequence(fileData,i):
	sequence = []
	info=' '
	sequenceI=''
	structure=''
	s = fileData[i]
	baseSequence=''
	if s.startswith('>'):
		info=s		
		i=i+1
		sequenceI=fileData[i]
		sequenceI=sequenceI.rstrip()
		baseSequence=sequenceI
		i=i+1
		structure=fileData[i]
		structure=structure.rstrip()
	sequenceI=runRNAEval(sequenceI,structure)
	sequence=sequenceI.split('\n')
	return (sequence,info,i+1,baseSequence)

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
			#print item[3]
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
				#	print "sfsfs",str(tree[num][1])
					for numK in range(tree[num][1]+1,curRight):
						tree[num-1][4].append(numK)
				if tree[num][5]:
				#	print "sfdsfs",tree[num]
					for numK in range(tree[num][0]+1,tree[num][1]):
						tree[num][3].append(numK)
					#print tree[num]
				curLeft=tree[num][0]
				curRight=tree[num][1]
	return stemLoopTrees


#def compareStemLoop(unknownStemLoop,knownStemLoop):

unknownSequence=[]
unknownSequence,unknownInfo,j,unknownBaseSequence=getSequence(sequenceFileData,0)
#print unknownSequence
unknownStemLoopTrees=getStemLoopTrees(unknownSequence)
unknownStemLoopTrees=addLeaves(unknownStemLoopTrees)
#print unknownStemLoopTrees

knownSequences=[]
knownInfos=[]
i=0
knownSequenceStemLoopTrees=[]
knowBaseSequences=[]
while i<len(compareFileData):
	knownSequence,knownSequenceInfo,i,knownBaseSequence=getSequence(compareFileData,i)
	knownSequences.append(knownSequence)
	knowBaseSequences.append(knownBaseSequence)
	knownInfos.append(knownSequenceInfo)
	k = getStemLoopTrees(knownSequence)
	knownSequenceStemLoopTrees.append(k)


for num in range(0,len(knownSequenceStemLoopTrees)):
	knownSequenceStemLoopTrees[num]=addLeaves(knownSequenceStemLoopTrees[num])

#print knownSequenceStemLoopTrees[7]
#####################################################################################################
#Initialization
#D=numpy.zeros((
#print unknownStemLoopTrees[1]
#print knownSequenceStemLoopTrees[0][0]
#findMin(unknownStemLoopTrees[1],knownSequenceStemLoopTrees[0][0],unknownSequence,knownSequences[0])
#print knownSequenceStemLoopTrees[7][5]
#indexPairs,pointers= getIndexingPairs(knownSequenceStemLoopTrees[7][5])
findMin(unknownStemLoopTrees[0],knownSequenceStemLoopTrees[7][5],unknownBaseSequence,knowBaseSequences[7])
#print indexPairs,pointers
#print knowBaseSequences[7]


