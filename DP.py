import math

deletionScore=insertScore=0.75
relabelScore=0.25
arcCreateScore=arcDestroyScore=0.5
alterScore=completeScore=1


def findMin(inputStemLoop,outputStemLoop):
	D=[]
	temp=[0]
	D.append(temp)
	inputIndexingPair=(0,0)
	inputStemLoopLen=len(inputStemLoop)
	outputStemLoopLen=len(outputStemLoop)
	if inputStemLoop[inputStemLoopLen-1][5]:
		inputIndexingPair=(len(inputStemLoop[inputStemLoopLen-1][3])/2+inputStemLoop[inputStemLoopLen-1][0],len(inputStemLoop[inputStemLoopLen-1][3])/2+inputStemLoop[inputStemLoopLen-1][0]+1)
		
	else:
		inputIndexingPair=(inputStemLoop[inputStemLoopLen-1][0],inputStemLoop[inputStemLoopLen-1][1])

	print inputIndexingPair
	
#if outputStemLoop[outputStemLoopLen-1][5]:


#def nextIndexingNode(stemLoop,currentIndexingNode):
	

#def equalInternal(inputInternalNode,outputInternalNode):
