
def tokenize(sentence):

	for sym in ['.', ',', '?', ';', '\'', ':']:
		sentence = sentence.replace(sym, ' ' + sym)
	return sentence.split()

