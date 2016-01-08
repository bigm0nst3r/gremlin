#!/usr/bin/python

import os, random

__author__ = "Sreejith S"

rootDir = os.path.dirname(os.path.abspath(__file__)) + "/collection"
wordDictionary = {}

def addToDict(pair):
  """
  
  Arguments:
  - `words`:
  """
  if(len(pair)>2):
    key = pair[0].strip()
    values = pair[1].split("-")
    vals = [value.strip() for value in values ]
    wordDictionary[key] = vals

def getCollection(dirName):
  """
  
  Arguments:
  - `dirName`:
  """
  files = os.listdir(dirName)
  return [file for file in files if file.startswith('vocab')]


def process(filename):
  """
  
  Arguments:
  - `filename`:
  """
  fullPath = rootDir + "/" + filename
  with open(fullPath, 'r') as myfile:
    data=myfile.read()
    wordlist = data.split("\n\n")
    for wordInfo in wordlist :
      pair = wordInfo.strip().split("\n")
      addToDict(pair)

  
files = getCollection(rootDir)
[process(filename) for filename in files ]

flag = True

while(flag):
  inp = raw_input("Play(y/n)")
  flag = True if inp == 'y' or inp=="" else False
  randKey = random.choice(wordDictionary.keys())
  randValue = random.choice(wordDictionary[randKey])
  print "Guess : " + randValue
  stroke = raw_input("Show answer ?")
  print " Answer : " + randKey
  
  
  





