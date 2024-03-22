import re
def remove_emails(text):
    return re.sub(r"\b\w+@\w+\.\w+\b", "", text) 
def extract_letters(text):
    return re.sub(r"[^a-zA-Z\s]", "", text)
with open('ab.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        clean_text = remove_emails(line) 
        words = extract_letters(clean_text)
        for i in range(0, len(words), 100):
            print("".join(words[i:i+100]))
