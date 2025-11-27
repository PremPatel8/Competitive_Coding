"""
1 - clean the data, convert it to a list of words, convert to lowercase, strip punctuations
2 - dict - count the freq of all words, word as key and freq as value, add start pos
3 - des order of freq, or start pos

References:
https://www.programiz.com/python-programming/methods/built-in/sorted
https://docs.python.org/3/howto/sorting.html
https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
https://stackoverflow.com/questions/1143671/how-to-sort-objects-by-multiple-keys-in-python
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

    # Python 3.X saves the insertion order of dict, so we only have to sort by freq in descending order
    # For Python 2.X we have to sort twice, once by the word index in ascending order and then by the freq in descending order (sort from least significant key to most significant key)
    # Alternatively we can use tuples with key and use negative values to sort one key by descending and other by ascending
    # Two tuples can be compared by comparing their elements starting from first. If there is a tie (elements are equal), the second element is compared, and so on.

    # we first compare the freq_count in descending order, if freq is same we compare by first_index in default ascending order
    sorted_words = sorted(
        freqDict.keys(), key=lambda wrd: (-freqDict[wrd][0], freqDict[wrd][1]))

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
