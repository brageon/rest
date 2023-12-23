import re
def get_trigrams(text):
    words = re.findall(r"\w+", text)
    trigrams = []
    for i in range(len(words) - 2):
        trigram = tuple(words[i:i + 3])
        trigrams.append(trigram)
    return trigrams
if __name__ == "__main__":
    with open("colin2/v10.txt", "r") as f:
        text = f.read()
    trigrams = get_trigrams(text)
    for trigram in trigrams:
        print(trigram)