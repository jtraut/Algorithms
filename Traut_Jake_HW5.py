"""
Assignment Name: Homework 5

Author: Jake Traut 

Description: Reads a wordlist file via command line and finds the longest chain of words. 

Additional Notes: Implemented using a recursive function
	Example chains
	['he', 'the', 'thew', 'thews', 'whites', 'whities', 'whiniest', 'winterish', 'swithering']
	['li', 'lis', 'slit', 'flits', 'filets', 'fetials', 'foliates', 'fellatios', 'fellations'] 
	['sue', 'emus', 'spume', 'septum', 'impetus', 'stumpier', 'septarium', 'subprimate', 'subprimates']

Date: 10-12-15

"""
import sys

filename = sys.argv[-1]

if (filename == "Traut_Jake_HW5.py"): #recieved no command line input
	filename = "wordlist.txt"
	
#Start by making new sorted wordlist
words = []
with open(filename) as wordfile:
	for word in wordfile:
		word = word.rstrip('\n').lower()
		words.append(word)
words.sort(key = lambda s: len(s)) 

maxstring = len(words[len(words)-1]) #length of last string in list
strLength = len(words[0]) #size of source/parent word to search from

longestChainWord = []
maxChainLength = 0
currentChainLength = 0

#print len(words)
#print maxstring

def validChainWord(currentWord,nextWord):
	currentWord = list(currentWord) #for iteration and comparison
	nextWord = list(nextWord)
	for letter in currentWord:
		if (not(letter in nextWord)):
			return False
		else:
			nextWord.remove(letter)
	return True 
	
def longestChain(strLength,currentChainLength,currentWord,counter): 
	global longestChainWord
	global maxChainLength
		
	if (currentChainLength > maxChainLength):
		longestChainWord.append(currentWord)
		maxChainLength = currentChainLength
		#print longestChainWord, maxChainLength
		
	if (strLength == maxstring):
		print longestChainWord, maxChainLength
		return longestChainWord, maxChainLength
	else:
		prevCounter = counter
		findLength = strLength
		while ((findLength < strLength+1)): #find next word with strLength+1	
			findLength = len(words[counter])
			if(findLength > strLength):
				findLength = maxstring+2
			else:
				counter += 1
				
		for i in range (prevCounter, counter+1):
			if validChainWord(currentWord,words[i]):		
				return longestChain(strLength+1,currentChainLength+1,words[i],counter)
		
		print longestChainWord, maxChainLength
		return longestChainWord, maxChainLength
		
#choose source		
strLength = len(words[205])
longestChain(strLength,0,words[205],205)
	
'''
i = 0		
while(strLength <= 3):
	strLength = len(words[i])
	i += 1
	
maxChainLength = 0
longestChainOfWords = []	
strLength = len(words[0])
sourceWord = [None]*(i-1)
count = [None]*(i-1)
chainOfWords = [None]*(i-1)
chainLength = [None]*(i-1)

for j in range(i-1):
	sourceWord[j] = words[j]
	count[j] = j
	(chainOfWords[j],chainLength[j]) = longestChain(strLength,0,sourceWord[j],count[j])
	if (chainLength[j] > maxChainLength):
		maxChainLength = chainLength[j]
		longestChainOfWords = chainOfWords[j]
		print longestChainOfWords, maxChainLength				
'''
		
				
