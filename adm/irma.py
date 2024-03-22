'''
Conceptual analysis. First Z=GAI, J=AWM, G=NVI, A=CPI, T=QRI. Noun is general category. Verb is non-verbal. Interjections is cardinals. Adjective is a description of noun and verb. QRI is motors behind vehicles. Pronoun is active category defined by ownership.  
'''
import numpy as np
from nltk import pos_tag
import scipy.stats as stats
import re, math, nltk, string
import matplotlib.pyplot as plt
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'PDT': 'Z', 'WDT': 'Z', 'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A', 'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J', 'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J', 'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G'}
dict_map = {'Z': 0.3, 'J': 0.5, 'G': 0.6, 'A': 0.7, 'T': 0.9}
youn = {'A J T': 1, 'G G Z': 1, 'J A T': 1, 'J J T': 1, 'A Z T': 1, 'Z J Z': 1, 'G Z G': 1, 'G A T': 1, 'Z J G': 2, 'G Z J': 2, 'T G A': 2, 'J Z Z': 3, 'Z Z Z': 3, 'T A G': 4, 'A G T': 4, 'T J Z': 4, 'T A T': 5, 'Z J T': 5, 'T Z J': 5, 'J Z T': 6, 'Z Z T': 6, 'T G G': 6, 'G J T': 7, 'T G J': 7, 'T Z G': 7, 'T Z Z': 8, 'J G T': 8, 'Z G T': 8, 'G G T': 9, 'T G Z': 9, 'T J T': 9, 'G Z T': 10, 'T Z T': 10}
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
  def count_trigrams(self, text):
    tokens = nltk.word_tokenize(text)
    trigrams = [] #gh, cloudinary, colab
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
    ouro = line_sum / (count - special_cases) if count - special_cases > 0 else line_sum / count
    sun = sum([dict_map.get(word, 0) for word in words])
    cof = np.array([dict_map.get(word, 0) for word in words])
    if special_cases > 0:
      varm = (line_sum / special_cases)**2 
      zs = (line_sum / special_cases - ouro) / np.sqrt(varm)
      ps = 1 - stats.norm.cdf(zs)
      sd = round(np.std(cof), 2)
    else:
      varm, zs, sd = 0.0, 0.0, 0.0
    return ouro, sun, varm, zs, sd
  def remove_non(self, text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)
if __name__ == "__main__":    
  bacl = BaCl()
#Excess LSE (liqu) but absent left (raw liqu) below. Two concepts are splitted here.
  input_text = "You undercut reputation for Italy by wanting cash without REIT. For example Italy had a fraction from ETF. Therefore we will see more cash for Italy." 
  hydra = bacl.remove_non(input_text)
  translated = bacl.translate(hydra)
  ouro, sun, varm, zs, sd = bacl.calc(translated)
  mid = bacl.count_trigrams(translated)
  percent_scores = []
  av_percent_score = 0
  gt = round(sun / ouro, 2)
  wc = len(input_text.split())
  for trigram, count in mid.items():
    percent_scores.append((float(count) / wc) * 100)
    if len(percent_scores) > 0:
    # liquidity, left, debt-to-equity, asset-to-debt
      av_percent_score = len(percent_scores) / sum(percent_scores)
    # solidity, debt-to-equity histogram 
      am_percent_score = sum(percent_scores) / len(percent_scores)
  mim = 3 * wc * (round(sum(percent_scores), 2) / 100) 
  safe = (wc - mim) / wc
  if zs == 0.0: # Pareto distribution
    zs = 1.0
  zeta = wc - (gt / zs) 
#debt-to-asset, profit except
  zat = am_percent_score / gt
  ares = (av_percent_score / zeta) - (zeta / am_percent_score)
  epok = (zeta / av_percent_score) - (am_percent_score / zeta)
  sac = (ares + epok) / 2
  def pearson_skewness(data):
    n = len(data)
    mean = sum(data) / n
    m2 = sum((x - mean)**2 for x in data) / n
    m3 = sum((x - mean)**3 for x in data) / n
    return 3 * m3 / (m2**(3/2))
  dat1 = (wc, safe) 
  dat2 = (varm, ouro, sd, zs) 
  dat3 = (av_percent_score, am_percent_score, sac)
  skew1 = round(pearson_skewness(dat1), 2)
  skew2 = round(pearson_skewness(dat2), 2)
  skew3 = round(pearson_skewness(dat3), 2)
  def colors(value, lower, upper):
    return max(min(value, upper), lower)
  def adjust(w, s, m, z):
    crow = round(skew1 + skew2 + skew3, 2)
    p = filter(lambda x: x >= 0, [crow, skew1, skew2, skew3])
    n = filter(lambda x: x <= 0, [crow, skew1, skew2, skew3])
    crow1 = sum(p)
    if crow1 == 0:
      crow1 = sum(n)
    so = round(wc / crow1, 1)
    if zs == 1.0:
      iq = round(sd + (ouro / 2), 2) 
    else:
      iq = round(zs * sd + ouro, 2)
    pb = round(iq * so, 1)  
    adjust = colors(pb, 0, 12)
    while adjust > 12:
      adjust -= 12
    return adjust, crow1, so, iq
  pb, crow1, so, iq = adjust(wc, sd, ouro, zs)
  ba = (wc, sun, ouro, varm, zs, sd, iq)
  bo = (safe, av_percent_score, am_percent_score, sac, zat, crow1, so)
  def tuple_elements(t, precision=2):
    return tuple(round(element, precision) if isinstance(element, (int, float)) else element for element in t)
  rba = tuple_elements(ba, precision=2)
  rbo = tuple_elements(bo, precision=2) 
  pl = "word, sum, mean, varx, z-sco, stad, quot"
  pq = "neut, liqu, solid, evals, left, skew, rate"
  print(pl)
  print(rba)
  print(pq)
  print(rbo)
  print(f'Color piece theory: {pb}.') #0 land, 11 bomb, 12 flag in Stratego.
'''
Histogram to plot word range in x axis. Similar to hemingwayapp.com, answerthepublic.com
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(dat1, bins=10, edgecolor='black')
plt.title('WN (Skewness: {:.2f})'.format(skew1))
plt.subplot(1, 3, 2)
plt.hist(dat2, bins=10, edgecolor='black')
plt.title('VMSZ (Skewness: {:.2f})'.format(skew2))
plt.subplot(1, 3, 3)
plt.hist(dat3, bins=10, edgecolor='black')
plt.title('LSE (Skewness: {:.2f})'.format(skew3))
plt.tight_layout()
plt.show()
range.py work better but use this if you have you want all trigrams
def get_words(text, start_indexes, end_indexes):
  words = []
  for start_index, end_index in zip(start_indexes, end_indexes):
    words.append(text[start_index:end_index])
  return words
star, den, sta, lel, dem = 19, 43, 130, 145, 168
gen, vem, dar, foo, ele = 185, 196, 220, 231, 243
words = get_words(input_text, [star, sta, dem, vem, foo], [den, lel, gen, dar, ele])
print(words)
'''
