import random
import re

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read().split()
    dic = {}
    for i in range(len(words)-1):
        if words[i] in dic:
            dic[words[i]].append(words[i+1])
        else:
            dic[words[i]] = [words[i+1]]

# TODO: analyze which words can follow other words
# Your code here
start_regex = re.compile('^((\"|)(?=[A-Z]))')


def checkIfStartWord(word):
    if start_regex.match(word):
        return True
    return False


end_regex = re.compile('.+([.!?](\"|)$)')


def checkIfEndWord(word):
    if end_regex.match(word):
        return True
    return False

def construct_sentence():
# TODO: construct 5 random sentences
# Your code here
    sentence_arr = []
    while len(sentence_arr) < 1:
        word = random.choice(list(dic.keys()))
        if checkIfStartWord(word):
            sentence_arr.append(word)
            break
    while True:
        next_word = random.choice(dic[sentence_arr[-1]])
        if not checkIfStartWord(next_word) and not checkIfEndWord(next_word):
            sentence_arr.append(next_word)
        elif checkIfEndWord(next_word) and not checkIfStartWord(next_word):
            sentence_arr.append(next_word)
            break
    return ' '.join(sentence_arr)


print(construct_sentence())
