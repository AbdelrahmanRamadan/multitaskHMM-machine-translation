# Viterbi algorithm to get POS, NER and chuncking analysis for each word

def analyse(sentence, model):
    (cpd_tagwords, cpd_tags, distinct_tags) = model

    sentlen = len(sentence)

    viterbi = []

    backpointer = []

    first_viterbi = {}
    first_backpointer = {}
    for tag in distinct_tags:
        if tag == 'START': continue
        first_viterbi[tag] = cpd_tags['START'].prob(tag) * cpd_tagwords[tag].prob(sentence[0])
        first_backpointer[tag] = 'START'

    viterbi.append(first_viterbi)
    backpointer.append(first_backpointer)

    currbest = max(first_viterbi.keys(), key=lambda tag: first_viterbi[tag])

    for wordindex in range(1, len(sentence)):
        this_viterbi = {}
        this_backpointer = {}
        prev_viterbi = viterbi[-1]

        for tag in distinct_tags:
            if tag == 'START': continue

            best_previous = max(prev_viterbi.keys(),
                                key=lambda prevtag: \
                                    prev_viterbi[prevtag] * cpd_tags[prevtag].prob(tag) * cpd_tagwords[tag].prob(
                                        sentence[wordindex]))

            this_viterbi[tag] = prev_viterbi[best_previous] * \
                                cpd_tags[best_previous].prob(tag) * cpd_tagwords[tag].prob(sentence[wordindex])
            this_backpointer[tag] = best_previous

        currbest = max(this_viterbi.keys(), key=lambda tag: this_viterbi[tag])

        viterbi.append(this_viterbi)
        backpointer.append(this_backpointer)

    prev_viterbi = viterbi[-1]
    best_previous = max(prev_viterbi.keys(),
                        key=lambda prevtag: prev_viterbi[prevtag] * cpd_tags[prevtag].prob('END'))

    prob_tagsequence = prev_viterbi[best_previous] * cpd_tags[best_previous].prob('END')

    best_tagsequence = ['END', best_previous]
    backpointer.reverse()

    current_best_tag = best_previous
    for bp in backpointer:
        best_tagsequence.append(bp[current_best_tag])
        current_best_tag = bp[current_best_tag]

    best_tagsequence.reverse()

    analysis = [(word,) + tuple(tag.split()) for (tag, word) in zip(best_tagsequence[1:-1], sentence)]
    return analysis, prob_tagsequence


# test_sentence = ["Ahmed", "went", "to", "school"]
# test_sentence = ["The", "teacher", "gave", "the", "student", "a", "book"]
# test_sentence = ["are", "you", "there", "?"]
# test_sentence = ["I", "saw", "the", "brilliant", "Alex"]
# print(analyse(test_sentence))


