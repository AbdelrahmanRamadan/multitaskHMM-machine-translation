import nltk
from map_tags import map_tag

def train():
    train_words = [i.strip() for i in open('train.txt', 'r').readlines()]
    train_words.append('')

    train = []
    temp_sent = []
    for i in train_words:
        if not i:
            if temp_sent:
                train.append(temp_sent)
            temp_sent = []
        else:
            temp_word = i.split()
            temp_word = (temp_word[0], map_tag(temp_word[1]) + ' ' + temp_word[2] + ' ' + temp_word[3])
            temp_sent.append(temp_word)

    tags_words = []

    for sent in train:
        tags_words.append(('START', 'START'))
        tags_words.extend([(tag, word) for (word, tag) in sent])
        tags_words.append(('END', 'END'))

    cfd_tagwords = nltk.ConditionalFreqDist(tags_words)
    cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)

    universal_tags = [tag for (tag, word) in tags_words]

    cfd_tags = nltk.ConditionalFreqDist(nltk.bigrams(universal_tags))
    cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)

    distinct_tags = set(universal_tags)

    return (cpd_tagwords, cpd_tags, distinct_tags)