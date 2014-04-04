import math

deletionScore=insertScore=0.75
relabelScore=0.25
arcCreateScore=arcDestroyScore=0.5
alterScore=completeScore=1

def getIndexingPairs(stemLoop):
	indexingPairs=[]
	for node in stemLoop:
		indexingPairs.append(((node[0],node[1]),(node[0],node[1])))
		if node[5] !=True:
			for leaf in node[3]:
				indexingPairs.append(((leaf,'-'),(node[0],node[1])))
			for leaf in reversed(node[4]):
				indexingPairs.append(((node[0],node[1]),('-',leaf)))
			for leaf in node[3]:
				for rightLeaf in reversed(node[4]):
					indexingPairs.append(((leaf,'-'),('-',rightLeaf)))
		else:
			for leaf in node[3]:
				indexingPairs.append(((leaf,'-'),(node[0],node[1])))
			for leaf in reversed(node[3]):
				indexingPairs.append(((node[0],node[1]),('-',leaf)))
			for num in range(0,len(node[3])):
				for numK in reversed(range(num+1,len(node[3]))):
					indexingPairs.append(((node[3][num],'-'),('-',node[3][numK])))
	
	return indexingPairs
			


def findMin(inputStemLoop,outputStemLoop,inputSequence,outputSequence):
	D=[]
	temp=[0]
	D.append(temp)
	inputIndexingPair=getIndexingPair(inputStemLoop,inputSequence)
	#print inputIndexingPair
	outputIndexingPair=getIndexingPair(outputStemLoop,outputSequence)
	#print outputIndexingPair
	
	



#if outputStemLoop[outputStemLoopLen-1][5]:


#def nextIndexingNode(stemLoop,currentIndexingNode):
	

#def equalInternal(inputInternalNode,outputInternalNode):
