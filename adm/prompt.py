import re, csv, nltk, time, scipy, numpy, socket
import threading, logging, warnings, subprocess
from nlptools.preprocessing.tagging import MLTagger
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'PRP': 'A', 'WP': 'Z', 'WPS': 'Z', 'UH': 'S', 'DT': 'S', 'WDT': 'S', 'IN': 'J', 'CD': 'J', 'FW': 'J',
'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G',
'RP': 'A', 'EX': 'A', 'CC': 'A', 'WRB': 'A', 'MD': 'A', '.': 'n'}
dict_map = {"Z": 0.3, "S": 0.3, "A": 0.7, "G": 0.7, "J": 0.5, "T": 1.5}
logging.basicConfig(filename='res.log', level=logging.INFO, format='%(message)s')
warnings.filterwarnings("ignore", category=DeprecationWarning)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logger = logging.getLogger()
lock = threading.Lock()
server = ('localhost', 1234)
sock.connect(server)
def amrita(words): 
    prev_letter = None 
    line_sum = 0.0 
    count = 0 
    special_cases = 0
    for word in words: 
        if word == "n":
            pass
        if prev_letter == "G" and word == "Z":
            line_sum -= 0.3
            special_cases += 1
        elif prev_letter == "Z" and word == "G":
            line_sum -= 0.7
            special_cases += 1
        elif prev_letter == "T" and word == "J":
            line_sum -= 0.5
            special_cases += 1
        elif prev_letter == "J" and word == "T":
            line_sum -= 0.9
            special_cases += 1
        else:
            line_sum += dict_map[word]
            count += 1
        prev_letter = word 
    line = ','.join(words)
    sums = f"{round(line_sum, 2)}"
    if count - special_cases > 0:
        ouro = f"{round((line_sum) / (count - special_cases), 1)}"
    elif count == 0:
        ouro = f"{round((line_sum) / 1)}"
    else:
        ouro = f"{round((line_sum) / (count), 1)}"  
    return line, sums, ouro
tagger = MLTagger()
inputs = []
while True:
    user1 = input("P1: ")
    user2 = input("P2: ")
    user3 = input("P3: ")
    if user1 == "":
        user1 = "."
    if user2 == "":
        user2 = "."
    if user3 == "":
        user3 = "."
    ui = [user1, user2, user3]
    if user1 == "stop":
        break      
    with lock:
        arr = numpy.array(ui)
        for i, item in enumerate(arr):
            tag_pairs = tagger.tag(item)
            tags = [tag.PoS for tag in tag_pairs]
            convert = [tag_map.get(tag, tag) \
            for tag in tags if tag not in ("", None)]
            words = ([col.strip() for col in convert])
            word = numpy.array(list(words))
            word = word.astype(str) 
            wcs = word.tostring().decode("utf-8")
            let = re.sub("[^a-zA-Z]+", "", wcs)
            new = amrita(let)
            logger.info('%s', new)
    result = subprocess.run(['python', 'km.py'], capture_output=True, text=True)
    res = result.stdout  # netcat -l 1234
    sock.sendall(res.encode())
sock.close()