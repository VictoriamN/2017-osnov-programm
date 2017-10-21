import sys

#read all input lines in our tagged corpus
lines = sys.stdin.readlines()

#variable to store counts for individual tags
tag_count = {}

#variable to store counts of tags give nwords
words = {}

#variable to store counts of individual surface forms/words
counts_of_word = {}
total = 0

for line in lines:
	#skip lines that dont have a tag in
	if '\t' not in line:
		continue

	#split line into lists of cells in the row
	row = line.split('\t')

	#get tag from fourth column and put it in variable
	tag = row[3]
	if tag == '_':
		continue

	if tag not in tag_count:
		tag_count[tag] = 0
	tag_count[tag] = tag_count[tag] + 1 

	#get the surface form from the second column:
	word= row[1]
	if word == '_':
		continue

	#if we havent seen the word before then initialize the word counter from zero
	if word not in counts_of_word:
		counts_of_word[word] = 0
	counts_of_word[word] = counts_of_word[word] + 1

	#if we havent seen the word before then initialise it to an empty dict
	if word not in words: 
		words[word] = {}

	#if we havent seen the tag given the word before, initialize it to zero
	if tag not in words[word]:
		words[word][tag] = 0
	words[word][tag] = words[word][tag] + 1

#	print('T:', tag_count)
#	print('W:', words)
#	print('CW:', counts_of_word)
#	print('X:', total)
	total = total + 1
	#print(tag_count[tag], freq)

for tag in tag_count:
	freq = tag_count[tag]/total
	print('%.2f\t%d\t%s\t_' %( freq, tag_count[tag], tag))

	#fore each of the words in the matrix
for word in words:
	#for each of the tag
	for tag in words[word]:
		freq = words[word][tag]/counts_of_word[word]
		print('%.2f\t%d\t%s\t%s' % (freq, words[word][tag], tag, word))