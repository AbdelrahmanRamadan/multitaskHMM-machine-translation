from analysis import analyse
from chunck import chuncker
from utils import tokenize

# look up word meaning from a dictionary containing the arabic translation for each word/analysis
def look_up(word):
	term = '|'.join([str(i) for i in word])
	for line in open('en-ar dictionary.txt', 'r'):
		l = line.split()
		if term == l[0]:
			return ' '.join(l[1:])

	return word[0]



# returns the arabic equivilant sentence of the chunck
def to_arabic_chunck(chunck):
	(tag, words) = chunck

	for i in range(len(words)):
		words[i] = (words[i][0].lower(), words[i][1], words[i][2], words[i][3])

	i = 0
	while i < len(words) - 1:
		if words[i][1] == 'ADJ' and words[i + 1][1] == 'NOUN':
			words[i], words[i + 1] = words[i + 1], words[i]
			
			if i > 0 and words[i - 1][0] == 'the':
				words[i - 1], words[i] = words[i], words[i - 1]
				if words[i - 1][3] == 'O':
					words.insert(i - 1, words[i])
					i += 1
		i += 1

	translated = ''
	for word in words:
		translated += look_up(word)
		if word[0] != 'the' and word[0] != 'a' and word[0] != 'an':
			translated += ' '
		
	return translated


def to_arabic(chuncks):
	#if first chunck is noun and the second is verb then reverse their order 
	#if the first is PRON the order stays the same
	for i in range(1, len(chuncks)):
		if chuncks[i - 1][0] == 'NP' and chuncks[i][0] == 'VP' and chuncks[i - 1][1][0][1] != 'PRON':
			chuncks[i - 1], chuncks[i] = chuncks[i], chuncks[i - 1]

	translated = ''
	for chunck in chuncks:
		translated += to_arabic_chunck(chunck)

	return translated.strip()


def translate(sentence, model, log = None):
	tokens = tokenize(sentence)
	if log:
		print(' tokens = {}\n'.format(tokens), file = log)

	analysis = analyse(tokens, model)

	if log:
		print(' analysis = {}\n'.format(analysis), file = log)
	
	chuncks = chuncker(analysis[0])
	
	if log:
		print(' chuncks = {}\n'.format(chuncks), file = log)
	
	translation = to_arabic(chuncks)
	
	if log:
		print(' translation = {}\n'.format(translation), file = log)
	
	return translation
