import re, nltk

tag_map = ['NNP', 'NNPS', 'NN', 'NNS', 'WP', 'WPS', 'DT', 'PDT', 'WDT', 'PRP', 'PRPS', 'PRP$', 'EX', 'POS', 'TO', 'UH', 'IN', 'CD', 'FW', 'RP', 'CC', 'MD', 'JJ', 'JJR', 'JJS', 'RB', 'WRB', 'RBR', 'RBS', 'VBP', 'VBZ', 'VBD', 'VBG', 'VBN', 'VB']
# 73 J dict vs 38 J list

class NiTi:
    def translate(self, text):
        tokens = nltk.word_tokenize(text)
        tag_pairs = nltk.pos_tag(tokens)
        convert = [tag for tag, _ in tag_pairs]
        return tuple(convert)
    def remove_emails(self, text):
        return re.sub(r'\b\w+@\w+\.\w+\b', '', text)
    def extract_letters(self, text):
        return re.sub(r'[^a-zA-Z\s]', '', text)
    def chunking(self, filename):
        with open(filename, 'r') as film:
            lines = film.readlines()
        for line in lines:
            clean_text = self.remove_emails(line)
            wow = self.extract_letters(clean_text)
            words = self.translate(wow)
            vwo = 1
            for isp in range(0, len(words), 17):
                word_chunk = words[isp:isp+17]
                print(' '.join(word_chunk))
                vwo += 1
niti = NiTi()
film = 'sw.txt'
results = niti.chunking(film)
