import numpy as np
from nltk import pos_tag
import re, nltk, string, youth
from collections import Counter
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'PDT': 'Z', 'WDT': 'Z', 'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A', 'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J', 'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J', 'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G'}
dict_map = {'Z': 0.3, 'J': 0.5, 'G': 0.6, 'A': 0.7, 'T': 0.9}
class BaCl:
  def __init__(self):
    pass
  def translate(self, text):
    tokens = nltk.word_tokenize(text)
    tag_pairs = nltk.pos_tag(tokens)
    convert = [tag_map.get(tag, tag) for _, tag in tag_pairs]
    word_list = []
    for word in convert:
      if isinstance(word, float):
        continue
      if word in dict_map and isinstance(dict_map[word], str):
        word_list.append(dict_map[word])
      else:
        word_list.append(str(word))
    translated = ' '.join(word_list)
    return translated
  def calc(self, translated):
    words = translated.split(' ')
    line_sum = sum([float(dict_map.get(word, 0)) for word in words])
    count, special_cases = 0, 0
    line = ' '.join(words)
    for i in range(1, len(words)):
      if words[i - 1] == "G" and words[i] == "Z":
        line_sum -= 0.3
        special_cases += 1
      elif words[i - 1] == "Z" and words[i] == "G":
        line_sum -= 0.6
        special_cases += 1
      elif words[i - 1] == "T" and words[i] == "J":
        line_sum -= 0.5
        special_cases += 1
      elif words[i - 1] == "J" and words[i] == "T":
        line_sum -= 0.9
        special_cases += 1
      elif words[i - 1] == "G" and words[i] == "G":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "Z" and words[i] == "Z":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "A" and words[i] == "A":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "J" and words[i] == "J":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "T" and words[i] == "T":
        line_sum -= 0
        special_cases += 0
      else:
        count += 1
    if count - special_cases > 0:
      ouro = (line_sum / (count - special_cases))
    else:
      ouro = dict_map.get(word, 0) if count == 0 else line_sum / count
    sun = sum([dict_map.get(word, 0) for word in words])
    return ouro, sun
input_text = input("Enter text: ")
bacl = BaCl()
translated = bacl.translate(input_text)
ouro, sun = bacl.calc(translated)
mid = youth.count_trigrams(translated)
print("Mean:", round(ouro, 1))
print("Sum:", round(sun, 1))
percent_scores = []
for trigram, count in mid.items():
  percent_scores.append((float(count) / len(input_text.split())) * 100)
average_percent_score = sum(percent_scores) / len(percent_scores)
print("Left:", round(average_percent_score, 1))
for trigram, count in mid.items():
    print(f"{trigram}: {count}")

