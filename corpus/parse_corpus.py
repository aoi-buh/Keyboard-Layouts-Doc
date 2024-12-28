import json

CORPUS = "corpus/mr"
OUTPUT = "corpus/parsed.json"
NGRAM_MAX_LEN = 4

ngrams = tuple({} for _ in range(NGRAM_MAX_LEN))

def window(line, size, r=False):
    if r: return (line[i:i+size] for i in range(len(line)))
    return (line[i:i+size] for i in range(len(line) - size + 1))

# with open(CORPUS, "r") as file:
#     while (line := file.readline().lower()) != "":
#         for ngram in window(line, NGRAM_MAX_LEN):
#             for i, gram in enumerate(ngram[:i+1] for i in range(NGRAM_MAX_LEN)):
#                 ngrams[i][gram] = ngrams[i].get(gram, 0) + 1
#         for ngram in window(line[-NGRAM_MAX_LEN:], NGRAM_MAX_LEN - 1, r=True):
#             for i, gram in enumerate(ngram[:i+1] for i in range(len(ngram))):
#                 ngrams[i][gram] = ngrams[i].get(gram, 0) + 1

with open(CORPUS, "r") as file:
    while (line := file.readline().lower()) != "":
        for ngram in window(line, NGRAM_MAX_LEN, r=True):
            for i, gram in enumerate(ngram[:i+1] for i in range(len(ngram))):
                ngrams[i][gram] = ngrams[i].get(gram, 0) + 1

with open(OUTPUT, "w") as file:
    json.dump(ngrams, file, indent=4)
