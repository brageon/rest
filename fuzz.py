from fuzzywuzzy import fuzz
import re, sys, math, nltk
sys.path.insert(1, '../')
from adm.irma import BaCl
import numpy as np
dict_map = {'Z': 3, 'J': 5, 'G': 6, 'A': 7, 'T': 9}
data = "Emotion is memory allocation. Intuition is sensory translation. Belief is logical terrain navigation. All behaviors originate from this."
bacl = BaCl()
hydra = bacl.remove_non(data)
translated = bacl.translate(hydra)
ouro, sun, varm, zs, sd = bacl.calc(translated)
mid = bacl.count_trigrams(translated)
cardinal_threshold = 80
def get_cardinal_value(token):
    max_ratio = 0
    max_value = None
    for key, value in dict_map.items():
        ratio = fuzz.partial_ratio(key, token)
        if ratio >= cardinal_threshold and ratio > max_ratio:
            max_ratio = ratio
            max_value = value
    return max_value
for trigram, count in mid.items():
    print(trigram, count)
    regex = re.compile(r'\b({})\b'.format('|'.join(map(re.escape, dict_map.keys()))), re.IGNORECASE)
    swap = sorted(translated, key=lambda x: get_cardinal_value(trigram))
    sad = "".join(swap) 
print(len(sad.split()), sad.split(','))