import re, math
def compute_tf(term, document):
    term_frequency = document.count(term)
    return term_frequency
def compute_df(term, documents):
    document_frequency = 0
    for document in documents:
        if term in document:
            document_frequency += 1
    return document_frequency
def compute_idf(term, documents):
    document_count = len(documents)
    return math.log(document_count / (1 + compute_df(term, documents)))
def compute_tfidf(term, document, documents):
    term_frequency = compute_tf(term, document)
    inverse_document_frequency = compute_idf(term, documents)
    return term_frequency * inverse_document_frequency
def main():
    document = open("colin2/v10.txt", "r").read()
    tokens = re.split(r"[^\w\s]", document)
    tokens = [token for token in tokens if token]
    tfidf_scores = {}
    for token in tokens:
        tfidf_score = compute_tfidf(token, document, tokens)
        tfidf_scores[token] = tfidf_score
    for term, tfidf in sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{term}: {tfidf}")
if __name__ == "__main__":
    main()
