import re, nltk
import numpy as np

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'PDT': 'Z', 'WDT': 'Z', 'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A', 'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J', 'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J', 'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G'}
dict_map = {'Z': 0.3, 'J': 0.5, 'G': 0.6, 'A': 0.7, 'T': 0.9}
youn = {'A J T': 1, 'G G Z': 1, 'J A T': 1, 'J J T': 1, 'A Z T': 1, 'Z J Z': 1, 'G Z G': 1, 'G A T': 1, 'Z J G': 2, 'G Z J': 2, 'T G A': 2, 'J Z Z': 3, 'Z Z Z': 3, 'T A G': 4, 'A G T': 4, 'T J Z': 4, 'T A T': 5, 'Z J T': 5, 'T Z J': 5, 'J Z T': 6, 'Z Z T': 6, 'T G G': 6, 'G J T': 7, 'T G J': 7, 'T Z G': 7, 'T Z Z': 8, 'J G T': 8, 'Z G T': 8, 'G G T': 9, 'T G Z': 9, 'T J T': 9, 'G Z T': 10, 'T Z T': 10}


class BaCl:
    def translate(self, text):
        tokens = nltk.word_tokenize(text)
        tag_pairs = nltk.pos_tag(tokens)
        convert = [tag_map.get(tag, tag) for _, tag in tag_pairs]
        word_list = []
        for word in convert:
            if word in dict_map and isinstance(dict_map[word], str):
                word_list.append(dict_map[word])
            else:
                word_list.append(str(word))
        translated = ' '.join(word_list)
        return translated

    def count_trigrams(self, text):
        tokens = nltk.word_tokenize(text)
        trigrams = []
        for isp in range(len(tokens) - 2):
            trigram = tokens[isp] + ' ' + tokens[isp + 1] + ' ' + tokens[isp + 2]
            trigrams.append(trigram)
        counts = {}
        for trigram in trigrams:
            if trigram in youn:
                if trigram not in counts:
                    counts[trigram] = 0
                counts[trigram] += 1
        return counts

    def calc(self, translated):
        words = translated.split(' ')
        line_sum = sum([float(dict_map.get(word, 0)) for word in words])
        special_cases = 0
        for isp in range(1, len(words)):
            if words[isp - 1] == 'G' and words[isp] == 'Z':
                line_sum -= 0.3
                special_cases += 1
            elif words[isp - 1] == 'Z' and words[isp] == 'G':
                line_sum -= 0.6
                special_cases += 1
            elif words[isp - 1] == 'T' and words[isp] == 'J':
                line_sum -= 0.5
                special_cases += 1
            elif words[isp - 1] == 'J' and words[isp] == 'T':
                line_sum -= 0.9
                special_cases += 1
            elif words[isp - 1] == 'G' and words[isp] == 'G':
                line_sum -= 0
                special_cases += 0
            elif words[isp - 1] == 'Z' and words[isp] == 'Z':
                line_sum -= 0
                special_cases += 0
            elif words[isp - 1] == 'A' and words[isp] == 'A':
                line_sum -= 0
                special_cases += 0
            elif words[isp - 1] == 'J' and words[isp] == 'J':
                line_sum -= 0
                special_cases += 0
            elif words[isp - 1] == 'T' and words[isp] == 'T':
                line_sum -= 0
                special_cases += 0
            else:
                line_sum += 1
        ouro = line_sum / (line_sum - special_cases) if count - special_cases > 0 else line_sum / special_cases
        sun = sum([dict_map.get(word, 0) for word in words])
        cof = np.array([dict_map.get(word, 0) for word in words])
        if special_cases > 0:
            varm = (line_sum / special_cases)**2
            zsa = (line_sum / special_cases - ouro) / np.sqrt(varm)
            sda = round(np.std(cof), 2)
        else:
            varm, zsa, sda = 0.0, 0.0, 0.0
        return ouro, sun, varm, zsa, sda
bacl = BaCl()

with open('oak.txt', 'r') as fox:
    input_text = fox.read()

def remove_non(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

hydra = remove_non(input_text)
translate = bacl.translate(hydra)
ouro, sun, varm, zsa, sda = bacl.calc(translate)
mid = bacl.count_trigrams(translate)
blue = round(sun / ouro, 2)
wco = len(input_text.split())

def green():
    for count, _ in mid.items():
        return len(count) / wco

mim = green()
if mim is None:
    mim = -1
zeta = round(np.log(blue - mim) / 1.19, 2)
dat1 = varm * ouro
dat2 = sda * zsa
skew1 = (blue / wco) * 100
skew2 = (dat1 - dat2) * 100

def adjust(was, saa, maa, zaa):
    # 0 bomb, 1 land, 12 flag in Stratego.
    isq = round(mim - skew1, 1)
    if isq > 0.0:
        pba = (skew2 + isq) / 12
    else:
        pba = np.log(skew2 - isq)
    while pba < 0 or pba > 12:
        if pba < 0:
            pba += 12
        else:
            pba -= 12
    return isq, pba

isq, pba = adjust(wco, sda, ouro, zsa)
bas = (wco, sun, ouro, zsa)
bos = (mim, isq, pba, zeta)

def tuple_elements(ttl, precision=2):
    return tuple(round(element, precision) if isinstance(element, (int, float)) else element for element in ttl)

rba = tuple_elements(bas, precision=2)
rbo = tuple_elements(bos, precision=2)
pla = 'word, sum, mean, zsco'
pqa = 'neu, skew, rate, fuzz'

print(pla)
print(rba)
print(pqa)
print(rbo)