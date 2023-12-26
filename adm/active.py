import spacy
nlp = spacy.load("en_core_web_sm")
def active_to_passive(sentence):
    tokens = nlp(sentence)
    verb = tokens[0]
    subject = tokens[1]
    if verb.pos_ == "AUX":
        return sentence
    else:
        passive_sentence = "The " + subject.text + " was " + verb.lemma_ + " by " + sentence[2:]
        return passive_sentence
def passive_to_active(sentence):
    tokens = nlp(sentence)
    verb = tokens[2]
    subject = tokens[0]
    agent = tokens[4:]
    if agent[0].pos_ == "DET":
        return sentence
    else:
        active_sentence = verb.lemma_ + " " + subject.text + " " + sentence[4:]
        return active_sentence
input_sentence = input("Enter a sentence: ")
active_sentence = active_to_passive(input_sentence)
pass_sentence = passive_to_active(input_sentence)
print("Passive: ", active_sentence)
print("Active: ", pass_sentence)
