import math

deletionScore=insertScore=0.75
relabelScore=0.25
arcCreateScore=arcDestroyScore=0.5
alterScore=completeScore=1

def getIndexingPairs(stemLoop):
	indexingPairs=[]
    # 4 pointers: current (x, y), (p(x), y), (x, s(y)), (p(x), s(y))
    pointers = [[0,-1,-1,-1]]
    # Parent node
    parentNode = 0
    # Current row number
    i = 0
    
	for node in stemLoop:
        # node - self (e.g. CG, CG)
		indexingPairs.append(((node[0],node[1]),(node[0],node[1])))
        i = i+1
        pointers.append([i, -1, -1, prevNode])
        currNode = i
        # NOT terminal
		if node[5] !=True:
			# left leaf - node (e.g. A-, CG)
            leftLeafPred = currNode
            for leaf in node[3]:
				indexingPairs.append(((leaf,'-'),(node[0],node[1])))
                i = i+1
                pointers.append([i, leftLeafPred, -1, -1])
                leftLeafPred = i
			# node - right leaf (e.g. CG, -U)
            rightLeafSucc = currNode
            for leaf in reversed(node[4]):
				indexingPairs.append(((node[0],node[1]),('-',leaf)))
                i = i+1
                pointers.append([i, -1, rightLeafPred, -1])
                rightLeafSucc = i
			# left leaf - right leaf (e.g. C-, -A)
            # THIS PART IS MESSY, DON'T LOOK!!!
            leftCounter = 0
            rightCounter = 0
            leafNodeStart = currNode + 1
            nodeLeafStart = currNode + len(node[3]) + 1
            currLeftLeafStart = nodeLeafStart
            
            predxy = nodeLeafStart
            xsuccy = currNode + 1
            predxsuccy = currNode
            for leftLeaf in node[3]:
                predxy = currLeftLeafStart
				for rightLeaf in reversed(node[4]):
					indexingPairs.append(((leftLeaf,'-'),('-',rightLeaf)))
                    i = i+1
                    pointers.append([i, predxy, xsuccy, predxsuccy])
                    predxy = predxy + 1
                    xsuccy = i
                currLeftLeafStart = currLeftLeafStart
                leftCounter = leftCounter+1
        # MESSY PART ENDS
		# Terminal <--- COULD YOU LOOK INTO THIS PART?
        else:
			for leaf in node[3]:
				indexingPairs.append(((leaf,'-'),(node[0],node[1])))
			for leaf in reversed(node[3]):
				indexingPairs.append(((node[0],node[1]),('-',leaf)))
			for num in range(0,len(node[3])):
				for numK in reversed(range(num+1,len(node[3]))):
					indexingPairs.append(((node[3][num],'-'),('-',node[3][numK])))
        prevNode = currNode
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
