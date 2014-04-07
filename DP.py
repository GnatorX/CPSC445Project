import math

deletionScore=insertScore=0.75
relabelScore=0.25
arcCreateScore=arcDestroyScore=0.5
alterScore=completeScore=1

def getIndexingPairs(stemLoop):
    indexingPairs=[]
    # 4 pointers: current (x, y), (p(x), y), (x, s(y)), (p(x), s(y))
    pointers = [[0,-1,-1,-1]]
    # Previous node
    prevNode = 0
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
                pointers.append([i, -1, rightLeafSucc, -1])
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
            j=0
            first=True
            #Start with left leaves
            for leaf in node[3]:
                indexingPairs.append(((leaf,'-'),(node[0],node[1])))
                i=i+1
                #If first just go one back (didn't use previous node because the i don't understand the behaviour of it
                if first:
                    pointers.append([i, currNode, -1, -1])
                    first=False
                #Else refer to previous indexing node (currNode+j= previous node)
                else:
                    pointers.append([i,currNode+j,-1,-1])
                j=j+1
            first=True
            #Right leaves is the same as left leaves except for the first one where it refers back to the previous internal 
            #node (currNode)
            for leaf in reversed(node[3]):
                indexingPairs.append(((node[0],node[1]),('-',leaf)))
                i=i+1
                if first:
                    pointers.append([i,-1,currNode,-1])
                    first=False
                else:
                     pointers.append([i,-1,currNode+j,-1])
                j=j+1
            #Leaf to leaf for termination loop
            timeRan=0
            notFirstCount=0
            for num in range(0,len(node[3])):
                numOfTerm=len(node[3])
                first=True
                for numK in reversed(range(num+1,len(node[3]))):
                        indexingPairs.append(((node[3][num],'-'),('-',node[3][numK])))
                        i=i+1
                        #Successor is previous indexing pair
                        successor=i-1
                        #Prenode is for getting parent(x) + successor(x) which is just parent(x)-1
                        preNode=i-(numOfTerm-timeRan)-1
                        #First is everytime the left leave changes (special cases)
                        if first:
                            #Is easier to figure out this by looking at the raw output. You want to go back to the indexing pair that had an internal node first right leaf
                            successor=i-(numOfTerm*2+notFirstCount)
                            #For Parent node, is similar but you just go one more back from successor because the way we generate indexing pair is left leaf with progession of right leafs. So parent node = one back from successor node since successor = one right leaf back and one left leaf back = -1 from successor
                            preNode=i-(numOfTerm*2+notFirstCount)-1
                            first=False
                        else:
                            notFirstCount=notFirstCount+1
                        pointers.append([i,i-(numOfTerm-timeRan),successor,preNode])
   
                timeRan=timeRan+1
        prevNode = currNode
    return indexingPairs,pointers
            
def printOutIndexingPairs(indexingPairs,baseSequence):
    for pair in indexingPairs:
        print '(',
    for num in range(0,2):
        p=pair[num]
        for numK in range(0,2):
            if p[numK] is not '-':
                print baseSequence[7][p[numK]-1],
            else:
                print '-',
    print ')'

def findMin(inputStemLoop,outputStemLoop,inputSequence,outputSequence):
    inputIndexingPair=getIndexingPair(inputStemLoop)
    #print inputIndexingPair
    outputIndexingPair=getIndexingPair(outputStemLoop)
    #print outputIndexingPair
    D=numpy.zeros(len(inputIndexingPair),len(outputIndexingPair))
    
    



#if outputStemLoop[outputStemLoopLen-1][5]:


#def nextIndexingNode(stemLoop,currentIndexingNode):
    

#def equalInternal(inputInternalNode,outputInternalNode):
