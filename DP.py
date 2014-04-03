import math

deletionScore=insertScore=0.75
relabelScore=0.25
arcCreateScore=arcDestroyScore=0.5
alterScore=completeScore=1
def getIndexingPair(stemLoop):
	indexingPair=(0,0)
	stemLoopLen=len(stemLoop)
	if stemLoop[stemLoopLen-1][5]:
		indexingPair=(len(stemLoop[stemLoopLen-1][3])/2+stemLoop[stemLoopLen-1][0],len(stemLoop[stemLoopLen-1][3])/2+stemLoop[stemLoopLen-1][0]+1)
		
	else:
		indexingPair=(stemLoop[stemLoopLen-1][0],stemLoop[stemLoopLen-1][1])

	return indexingPair

def findMin(inputStemLoop,outputStemLoop):
	D=[]
	temp=[0]
	D.append(temp)
	inputIndexingPair=getIndexingPair(inputStemLoop)
	print inputIndexingPair
	outputIndexingPair=getIndexingPair(outputStemLoop)
	print outputIndexingPair
	
	



#if outputStemLoop[outputStemLoopLen-1][5]:


#def nextIndexingNode(stemLoop,currentIndexingNode):
	

#def equalInternal(inputInternalNode,outputInternalNode):
