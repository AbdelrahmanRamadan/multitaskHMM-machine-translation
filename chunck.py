
# takes analysed sentece with (POS, NER, IOB) tags
# returns list of analysed chunks
# chuck = (chuck_tag, [(word, pos_tag, chuck_tag, ner_tag)])

def chuncker(analysis):
	chuncks = []
	temp_chunck = []
	for word in analysis:
		if word[2][0] in ['B', 'O']:
			if temp_chunck:
				chuncks.append(temp_chunck)
				temp_chunck = []
		temp_chunck.append(word)

	if temp_chunck:
		chuncks.append(temp_chunck)

	return [(ch[0][2].replace('B-', ''), ch) for ch in chuncks]


# Testing

# chuncks = chuncker([
# 	('The', 'DET', 'B-NP', 'O'),
# 	('teacher', 'NOUN', 'I-NP', 'O'),
# 	('gave', 'VERB', 'B-VP', 'O'),
# 	('the', 'DET', 'B-NP', 'O'),
# 	('brilliant', 'ADJ', 'I-NP', 'O'),
# 	('student', 'NOUN', 'I-NP', 'O'),
# 	('a', 'DET', 'B-NP', 'O'),
# 	('book','NOUN', 'I-NP', 'O')
# ]);

