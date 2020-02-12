""" Clean Reviews Data
		-Load input file and Read reviews
		-Tokenize reviews
		-Remove stopwords
		-Perform stemming
		-save the cleaned reviews in output file"""

import numpy as np
import pandas as pd
import sys


# NLTK
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#init
tokenizer = RegexpTokenizer('[\w]+')
sw = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

# data preprocessing - tokenize,remove stopwords,stem
def preprocess_data(text):
	text = text.replace('<br /><br />',' ')
	text = tokenizer.tokenize(text.lower())
	text = [w for w in text if w not in sw]
	text = [stemmer.stem(w) for w in text]

	text = ' '.join(text)
	return text

#read from the input file and write cleaned review to output file
def getCleanedReview(inputfile,outputfile):
	out = open(outputfile,'w')

	with open(inputfile) as f:
		reviews = f.readlines()

	for review in reviews:
		review = preprocess_data(review)
		print(review,file = out)
	out.close()

inputfile = sys.argv[1]
outputfile = sys.argv[2]
getCleanedReview(inputfile,outputfile)
