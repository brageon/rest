import string
def calculate_letter_frequencies(text):
    letter_frequencies = {}
    for letter in text:
        if letter in letter_frequencies:
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1
    return letter_frequencies
def calculate_probability_score(letter_frequencies):
    total_letters = sum(letter_frequencies.values())
    probability_scores = {}
    for letter, frequency in letter_frequencies.items():
        probability_score = frequency / total_letters
        probability_scores[letter] = probability_score
    return probability_scores
def calculate_probability_score_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    text = ''.join(ch for ch in text if ch not in string.punctuation)
    text = text.lower()
    letter_frequencies = calculate_letter_frequencies(text)
    probability_scores = calculate_probability_score(letter_frequencies)
    return probability_scores
if __name__ == '__main__':
    file_path = 'nu12.txt'
    probability_scores = calculate_probability_score_file(file_path)
    print(probability_scores)
    print("hej")
