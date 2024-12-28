import json
from typing import Callable, Iterable

CORPUS = "corpus/parsed.json"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
VOWEL = "aeiou"

alpha_only: Callable
vowel_only: Iterable

with open(CORPUS, "r") as file:
	corpus = json.load(file)[1]
	alpha_only = lambda: (i for i in corpus.items() if all(j in ALPHA for j in i[0]))
	vowel_only = (i for i in alpha_only() if all(j in VOWEL for j in i[0]))

total = sum(freq for _, freq in alpha_only())
bigrams = sorted(vowel_only, key=lambda i: i[1], reverse=True)
vowel_total = sum(freq for _, freq in bigrams)

print(
	'\n'.join((
		"| 1-10  | freq  | 11-20 | freq  |",
		"| ----- | ----- | ----- | ----- |",
		*("| " + ' | '.join(f"{bigrams[i+j][0]:<5} | {bigrams[i+j][1] / total:>5.2%}" for j in range(0, 20, 10)) + " |" for i in range(10)),
		"",
		f"Vowel bigrams amount to {vowel_total / total:.3%} of bigrams."
	))
)
