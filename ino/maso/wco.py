import re
word_count = 0
input_text = input("Enter text: ")
filtered_words = re.findall("[a-zA-Z]+", input_text)
for word in filtered_words:
    word_count += 1
print("Total word count:", word_count)
