import sys

lines = sys.stdin.readlines()

tag_count = {}
words = {}

words_of_word = {}
total = 0
# переменная для хранения русского слова и его формы
words_rus = {}
for line in lines[1:]:
    if '\t' not in line:
        continue

    
    row = line.split('\t')

  
    tag = row[3]
    if tag == '_':
        continue
 
    if tag not in tag_count:
        tag_count[tag] = 0
    tag_count[tag] = tag_count[tag] + 1


    word = row[2]
    if word == '_':
        continue

    if word not in words_of_word:
        words_of_word[word] = 0
    words_of_word[word] = words_of_word[word] + 1

    if word not in words:
        words[word] = {}
   
    if tag not in words[word]:
        words[word][tag] = 0
    words[word][tag] = words[word][tag] + 1
    total = total + 1

    # сохраняем русское слово и форму
    if word not in words_rus:
        words_rus[word] = {'word': row[8], 'tag': row[9]}

# # for each of the words in the matrix
for word in words:
    # for each of the tag
    for tag in words[word]:
      
        if (tag != 'IndicPret' and tag != 'IndicIpfct'):
            continue
        freq = words[word][tag] / words_of_word[word]
        
        print('%s\t%s\t%s\t%s\t%d\t%.2f' % (word, tag, words_rus[word]['word'], words_rus[word]['tag'], words[word][tag], freq))