import sys
import os
import random
import math

RNAEVAL_EXEC = "RNAeval"

def runRNAEval(seq,struct):
  tmpFile = "tmp.dat"
  tmpFileIn = "tmpin.dat"
  inFile = open(tmpFileIn,"w")
  inFile.write(seq+"\n"+struct+"\n")
  inFile.close()
  os.system("%s -d2 -v < %s > %s"%(RNAEVAL_EXEC,tmpFileIn,tmpFile))
  output=""
  data=open(tmpFile,"r")
  length=len(data.readlines())
  i=0
  for l in open(tmpFile,"r"):
    if i+3<length and i!=0:
       output=output+l.rstrip()+'\n'
    elif i+2<length and i!=0:
       output=output+l.rstrip()
    i=i+1
  output=output.replace("( ","(")
  output=output.replace("( ","(")
  output=output.replace("(","( ")
  output=output.replace(")"," )")
  output=output.replace(", ",",")
  return output
  os.remove(tmpFile)
  os.remove(tmpFileIn)
