import math
import numpy
numpy.set_printoptions(threshold=numpy.nan)

# Scoring Model
deletionScore=1
insertScore=1
relabelScore=0.25
arcCreateScore=1
arcDestroyScore=1
alterScore=1
completeScore=1.5
pairDeletionScore=1.5
pairInsertionScore=1.5
pairRelabelScore=0.4

INTERNALNODE=0
LEFTLEAF=1
RIGHTLEAF=2
LEAFLEAF=3

def getIndexingPairs(stemLoop):
    indexingPairs=[]
    # 4 pointers: current (x, y), (p(x), y), (x, s(y)), (p(x), s(y))
    pointers = [[0,-1,-1,-1]]
    # Current row number
    i = 0
    
    for node in stemLoop:
        # node - self (e.g. CG, CG)
        indexingPairs.append(((node[0],node[1]),(node[0],node[1]),INTERNALNODE))
        i = i+1
        pointers.append([i, -1, -1, i-1])
        currNode = i
        # NOT terminal
        if node[5] !=True:
            # Left leaf - Node (e.g. A-, CG)
            leftLeafPred = currNode
            for leaf in node[3]:
                indexingPairs.append(((leaf,'-'),(node[0],node[1]),LEFTLEAF))
                i = i+1
                pointers.append([i, leftLeafPred, -1, -1])
                leftLeafPred = i
            # Node - Right leaf (e.g. CG, -U)
            rightLeafSucc = currNode
            for leaf in reversed(node[4]):
                indexingPairs.append(((node[0],node[1]),('-',leaf),RIGHTLEAF))
                i = i+1
                pointers.append([i, -1, rightLeafSucc, -1])
                rightLeafSucc = i
            # Left leaf - Right leaf (e.g. C-, -A)
            # bookmark for first left-leaf
            leafNode = currNode + 1
            # bookmark for first right-leaf
            nodeLeaf = currNode + len(node[3]) + 1
            # predxy: p(x),y    xsuccy: x,s(y)  predxsuccy: p(x),s(y)
            for leftLeaf in node[3]:
                predxy = nodeLeaf
                iter = 0
                for rightLeaf in reversed(node[4]):
                    indexingPairs.append(((leftLeaf,'-'),('-',rightLeaf),LEAFLEAF))
                    i = i+1
                    if iter == 0:
                        xsuccy = leafNode
                        # update right-leaf bookmark
                        nodeLeaf = i
                    else: xsuccy = i-1
                    # For p(x),s(y), look into p(x),y and then its x,s(y)
                    predxsuccy = pointers[xsuccy][1]
                    pointers.append([i, predxy, xsuccy, predxsuccy])
                    predxy = predxy+1
                    iter = iter+1
                # update left-leaf bookmark
                leafNode = leafNode+1
        # Terminal
        else:
            j=0
            first=True
            #Start with left leaves
            for leaf in node[3]:
                indexingPairs.append(((leaf,'-'),(node[0],node[1]),LEFTLEAF))
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
                indexingPairs.append(((node[0],node[1]),('-',leaf),RIGHTLEAF))
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
                        indexingPairs.append(((node[3][num],'-'),('-',node[3][numK]),LEAFLEAF))
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

# INITIALIZATION
def initialization(firstIndexingPair,secondIndexingPair,firstPointer,secondPointer):
   # print len(firstIndexingPair),len(firstPointer)
    D=numpy.zeros((len(firstIndexingPair)+1,len(secondIndexingPair)+1))
    # First Column
    for num in range(1,len(firstIndexingPair)+1 ):
         #  print firstIndexingPair[num-1][2]
        if firstIndexingPair[num-1][2]==INTERNALNODE:
         #   print firstPointer[num][3],num
            D[num,0]=D[firstPointer[num][3],0]+pairDeletionScore
        elif firstIndexingPair[num-1][2]==RIGHTLEAF:
            D[num,0]=D[firstPointer[num][2],0]+deletionScore
        elif firstIndexingPair[num-1][2]==LEFTLEAF:
            D[num,0]=D[firstPointer[num][1],0]+deletionScore
        elif firstIndexingPair[num-1][2]==LEAFLEAF:
            D[num,0]=D[firstPointer[num][3],0]+2*deletionScore
    # First Row
    for num in range(1,len(secondIndexingPair)+1):
        if secondIndexingPair[num-1][2]==INTERNALNODE:
            print num,secondPointer[num][3],D[0,secondPointer[num][3]]
            D[0,num]=D[0,secondPointer[num][3]]+pairDeletionScore
        elif secondIndexingPair[num-1][2]==RIGHTLEAF:
            D[0,num]=D[0,secondPointer[num][2]]+deletionScore
        elif secondIndexingPair[num-1][2]==LEFTLEAF:
           
           D[0,num]=D[0,secondPointer[num][1]]+deletionScore
        elif secondIndexingPair[num-1][2]==LEAFLEAF:
            D[0,num]=D[0,secondPointer[num][3]]+2*deletionScore
    return D

# RECURRENCE
def recurrence(D, pairs1, pairs2, pointers1, pointers2):
    # Row-by-Row
    for xy in range(1, len(pointers1)):
        pointer1 = pointers1[xy]
        # Column-by-Column
        for uv in range(1, len(pointers2)):
            pointer2 = pointers2[uv]
            # CASE 1: Node and Node
            if pairs1[xy-1][2] == INTERNALNODE and pairs2[uv-1][2] == INTERNALNODE:
                # 3 possible events:
                # relabeling, deletion, insertion
                relabeling = D[pointer1[3], pointer2[3]] + pairRelabelScore
                deletion = D[pointer1[3], pointer2[0]] + pairDeletionScore
                insertion = D[pointer1[0], pointer2[3]] + pairInsertionScore
                score = min(relabeling, deletion, insertion)
            # CASE 2: Leaf and Leaf
            elif pairs1[xy-1][2] != INTERNALNODE and pairs2[uv-1][2] != INTERNALNODE:
                scores = []
                # 6 possible events, some may be undefined:
                # 2 deletions, 2 insertions, 2 relabelings
                if pointer1[1] != -1: 
                    deletionx = D[pointer1[1], pointer2[0]] + deletionScore
                    scores.append(deletionx)
                if pointer1[2] != -1:
                    deletiony = D[pointer1[2], pointer2[0]] + deletionScore
                    scores.append(deletiony)
                if pointer2[1] != -1:
                    insertionu = D[pointer1[0], pointer2[1]] + insertScore
                    scores.append(insertionu)
                if pointer2[2] != -1:
                    insertionv = D[pointer1[0], pointer2[2]] + insertScore
                    scores.append(insertionv)
                if pointer1[1] != -1 and pointer2[1] != -1:
                    relabelingxu = D[pointer1[1], pointer2[1]] + relabelScore
                    scores.append(relabelingxu)
                if pointer1[2] != -1 and pointer2[2] != -1:
                    relabelingyv = D[pointer1[2], pointer2[2]] + relabelScore
                    scores.append(relabelingyv)
                score = min(scores)
            # CASE 3: Node and Leaf
            elif pairs1[xy-1][2] == INTERNALNODE and pairs2[uv-1][2] != INTERNALNODE:
                scores = []
                # 6 possible events, some may be undefined:
                # deletion, 2 insertions, 2 alterings, ark-breaking
                if pointer1[3] != -1:
                    deletion = D[pointer1[3], pointer2[0]] + deletionScore
                    scores.append(deletion)
                    if pointer2[1] != -1:
                        alteringu = D[pointer1[3], pointer2[1]] + alterScore
                        scores.append(alteringu)
                    if pointer2[2] != -1:
                        alteringv = D[pointer1[3], pointer2[2]] + alterScore
                        scores.append(alteringv)
                    if pointer2[3] != -1:
                        arcbreak = D[pointer1[3], pointer2[3]] + arcDestroyScore
                        scores.append(arcbreak)
                if pointer2[1] != -1:
                    insertionu = D[pointer1[0], pointer2[1]] + insertScore
                    scores.append(insertionu)
                if pointer2[2] != -1:
                    insertionv = D[pointer1[0], pointer2[2]] + insertScore
                    scores.append(insertionv)
                score = min(scores)
            # CASE 4: Leaf and Node
            elif pairs1[xy-1][2] != INTERNALNODE and pairs2[uv-1][2] == INTERNALNODE:
                scores = []
                # 6 possible events, some may be undefined:
                # insertion, 2 deletions, 2 completion, arc-creation
                if pointer2[3] != -1:
                    insertion = D[pointer1[0], pointer2[3]] + insertScore
                    scores.append(insertion)
                    if pointer1[1] != -1:
                        completex = D[pointer1[1], pointer2[3]] + completeScore
                        scores.append(completex)
                    if pointer1[2] != -1:
                        completey = D[pointer1[2], pointer2[3]] + completeScore
                        scores.append(completey)
                    if pointer1[3] != -1:
                        arccreate = D[pointer1[3], pointer2[3]] + arcCreateScore
                        scores.append(arccreate)
                if pointer1[1] != -1:
                    deletionx = D[pointer1[1], pointer2[0]] + deletionScore
                    scores.append(deletionx)
                if pointer1[2] != -1:
                    deletiony = D[pointer1[2], pointer2[0]] + deletionScore
                    scores.append(deletiony)
                score = min(scores)
            D[xy, uv] = score
    return D



def findMin(inputStemLoop,outputStemLoop,inputSequence,outputSequence):
   
    inputIndexingPair,inPointers=getIndexingPairs(inputStemLoop)
    #print inputIndexingPair
    #print inputIndexingPair
    outputIndexingPair,outPointers=getIndexingPairs(outputStemLoop)
  #  print outputIndexingPair[0][2]
    D= initialization(inputIndexingPair,outputIndexingPair,inPointers,outPointers)
    #print D
    D2 = recurrence(D, resultPairs1,resultPairs2,resultPointers1,resultPointers2)
    print 'DISTANCE MATRIX : '
    print D2
    
    



#if outputStemLoop[outputStemLoopLen-1][5]:


#def nextIndexingNode(stemLoop,currentIndexingNode):
    

#def equalInternal(inputInternalNode,outputInternalNode):
