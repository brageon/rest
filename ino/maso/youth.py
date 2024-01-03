import re, nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
youn = {'T A T': 1, 'Z J T': 1, 'T Z J': 1, 'J Z T': 2, 'Z Z T': 2, 'T G G': 2, 'G J T': 3, 'T G J': 3, 'T Z G': 3, 'T Z Z': 4, 'J G T': 4, 'Z G T': 4, 'G G T': 5, 'T G Z': 5, 'T J T': 5}
def count_trigrams(text):
    tokens = nltk.word_tokenize(text)
    trigrams = []
    for i in range(len(tokens) - 2):
        trigram = tokens[i] + ' ' + tokens[i + 1] + ' ' + tokens[i + 2]
        trigrams.append(trigram)
    counts = {}
    for trigram in trigrams:
        if trigram in youn:
            if trigram not in counts:
                counts[trigram] = 0
            counts[trigram] += 1
    return counts
def nut_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().splitlines()
    counts = []
    with open(filename.split('.')[0], 'w') as c_file:
        for line in lines:
            counts.append(count_trigrams(line))
            for trigram, count in counts[-1].items():
                c_file.write(f"{trigram}: {count}\n")
if __name__ == "__main__":
    nut_file('lel.txt')
