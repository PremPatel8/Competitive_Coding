"""
1 - clean the data, convert it to a list of words, convert to lowercase, strip punctuations
2 - dict - count the freq of all words, word as key and freq as value, add start pos
3 - des order of freq, or start pos

"""

from collections import defaultdict


def word_count_engine(document):
    word_list = []
    output = []
    # {word : [freq_count, first_index]}
    freqDict = {}

    for word in document.split():
        temp = ""
        for ch in word.lower():
            if ch.isalpha():
                temp += ch

        word_list.append(temp)

    # print("word_list = ", word_list)

    for i, word in enumerate(word_list):
        if word in freqDict:
            freqDict[word][0] += 1
        else:
            freqDict[word] = [1, i]

    # print("freqDict - ", freqDict)

    # Python 3.X saves the insertion order of dict, so we only have to sort by freq
    sorted_words = sorted(
        freqDict.keys(), key=lambda wrd: freqDict[wrd][0], reverse=True)

    # print("sorted_words - ", sorted_words)

    for word in sorted_words:
        wrdFreq = freqDict[word][0]
        output.append([word, str(wrdFreq)])

    return output


# document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
# """ output: [ ["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"], ["get", "1"], ["by", "1"], ["just", "1"] ] """
# print(word_count_engine(document))


document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
""" Expected: [["just","4"],["practice","3"],["perfect","2"],["makes","1"],["youll","1"],["get","1"],["by","1"]] """
print(word_count_engine(document))
