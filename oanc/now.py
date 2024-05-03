import re
def remove_extra_whitespaces(filename):
    with open(filename, 'r') as f:
        original_text = f.read()
    cleaned_text = re.sub(r'\s+', ' ', original_text)
    cleaned_text = re.sub(r'\b\w\b', '', cleaned_text)
    with open(filename, 'w') as f:
        f.write(cleaned_text)
if __name__ == "__main__":
    filename = "ab.txt"
    remove_extra_whitespaces(filename)