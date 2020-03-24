#!/usr/bin/python
import string
from nltk.tokenize import RegexpTokenizer

nCorpi = 1;
minPalindromeWordLength = 2;
maxPalindromeWordLength = 7;


def palindrome(s):
	if (len(s)<=1):
		return True
	if (s[0] != s[-1]):
		return False
	else:
		return palindrome(s[1:len(s)-1])

def lower(corpus):
	for word in range(0,len(corpus)):
		lowerWord = ""
		for char in range(0, len(corpus[word])):
			lowerWord += (corpus[word][char].lower())
		corpus[word] = lowerWord
	return corpus

def cleanCorpus(corpus):
	corpus = corpus.replace("'", "")
	corpus = corpus.replace("\xe2", "")
	corpus = corpus.replace("_", "")
	tokenizer = RegexpTokenizer(r'\w+')
	corpus  = tokenizer.tokenize(corpus)
	corpus = lower(corpus);
	return corpus


def findPalindromes(corpus, minPalindromeWordLength, maxPalindromeWordLength, palindromeDict):
	for palindromeWordLength in range(minPalindromeWordLength,maxPalindromeWordLength+1):
		for w in range(0, len(corpus)-palindromeWordLength+1):
		 	pal = []
		 	for ngram in range(0,palindromeWordLength):
		 		pal.append(corpus[w+ngram])
		 	concat = ""
		 	concatWithSpaces = ""
			for word in pal:
				concat = concat + word
				concatWithSpaces = concatWithSpaces + " " + word
			if (len(concat)> 1):
				if palindrome(concat):
					if (concatWithSpaces in palindromeDict):
						palindromeDict[concatWithSpaces] = palindromeDict[concatWithSpaces]+  1;
					else:
						palindromeDict[concatWithSpaces] = 1;

palindromeDict = dict()
for corpusNumber in range(1, nCorpi+1):

	corpusName = "corpus" + str(corpusNumber) + ".txt"
	f = open(corpusName,"r") 
	corpus =  f.read()
	corpus = cleanCorpus(corpus)
	findPalindromes(corpus, minPalindromeWordLength, maxPalindromeWordLength, palindromeDict);
print palindromeDict
