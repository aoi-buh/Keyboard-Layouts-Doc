import json

CORPUS = "corpus/parsed.json"
WHITE_LIST = "abcdefghijklmnopqrstuvwxyz'"
APOSTROPHE = "'"

filtered: tuple

with open(CORPUS, "r") as file:
	filtered = tuple(i for i in json.load(file)[2].items() if all(j in WHITE_LIST for j in i[0]))

total = sum(trigram[1] for trigram in filtered)
apostrophe_containing = (i for i in filtered if APOSTROPHE in i[0])
trigrams = sorted(apostrophe_containing, key=lambda i: i[1], reverse=True)
apostrophe_total = sum(freq for _, freq in trigrams)

print(
	'\n'.join((
		"| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |",
		"| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |",
		*("| " + ' | '.join(f"{trigrams[i+j][0]:<5} | {trigrams[i+j][1] / total:>5.2%}" for j in range(0, 50, 10)) + " |" for i in range(10)),
		"",
		f"Trigrams with apostrophe amount to {apostrophe_total / total:.3%} of trigrams."
	))
)
