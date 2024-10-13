import re, spacy
class Translator:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
    def remove_non(self, text):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    def get_pos_tags(self, text):
        words = self.remove_non(text).split()
        if words:
            doc = self.nlp(" ".join(words))
            return [(token.text, token.tag_) for token in doc]
        else:
            return []

    def classify_tag(self, tag):
        tag_to_classify = tag[1]
        tag_map = { 'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z',  # Nouns (proper and common)
                    'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'PDT': 'Z', 'WDT': 'Z',  # Pronouns, determiners, wh-determiners
                    'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A',  # Pronouns (personal, possessive)
                    'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J',  # Existential, adpositions, conjunctions, interjections
                    'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J',  # Prepositions, foreign words, particles, modal verbs
                    'JJ': 'T', 'JJR': 'T', 'JJS': 'T',  # Adjectives (positive, comparative, superlative)
                    'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T',  # Adverbs (positive, comparative, superlative)
                    'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G' }
        return tag_map.get(tag_to_classify)

    def hicks_tag(self, word_spans):
        duck = r"G Z | Z G | T J | J T"
        youn = r"A J T | G G Z | J A T | J J T | A Z T | Z J Z | G Z G | G A T | Z J G | G Z J | T G A | J Z Z | Z Z Z | T A G | A G T | T J Z | T A T | Z J T | T Z J | J Z T | Z Z T | T G G | G J T | T G J | T Z G | T Z Z | J G T | Z G T | G G T | T G Z | T J T | G Z T | T Z T"
        matches = re.findall(youn, word_spans)
        return len(duck), len(matches)

    def translate(self):
        with open('oak.txt', 'r') as file:
            lines = file.readlines()
        results = []
        for line_num, line in enumerate(lines, 1):  # Start line numbers from 1
            wco = len(line.split())
            wco = wco * 2
            spacy_output = self.get_pos_tags(line)
            word_spans = " ".join([self.classify_tag(tag) for tag in spacy_output])
            duck, hicks = self.hicks_tag(word_spans)
            results.append((line_num, wco, duck, hicks))
        return results

    def calc(self):
        results = self.translate()
        for line_num, wco, duck, hicks in results:
            dual = round(((duck / wco) * 100), 2)
            hicks = round(((hicks / wco) * 100), 2)
            print(f'Line {line_num}: Wco: {wco} Try: {dual} Lib: {hicks}')

tran = Translator()
tran.calc()
