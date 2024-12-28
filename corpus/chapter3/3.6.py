import json

CORPUS = "corpus/parsed.json"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
CONS = "bcdfghjklmnpqrstvwxyz"

alpha_only: tuple

with open(CORPUS, "r") as file:
	alpha_only = tuple(i for i in json.load(file)[1].items() if all(j in ALPHA for j in i[0]))

total = sum(freq for _, freq in alpha_only)
cons_only = (i for i in alpha_only if all(j in CONS for j in i[0]))
bigrams = sorted(cons_only, key=lambda i: i[1], reverse=True)
cons_total = sum(freq for _, freq in bigrams)

print(
	'\n'.join((
		"| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |",
		"| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |",
		*("| " + ' | '.join(f"{bigrams[i+j][0]:<5} | {bigrams[i+j][1] / total:>5.2%}" for j in range(0, 50, 10)) + " |" for i in range(10)),
		"",
		f"Consonant bigrams amount to {cons_total / total:.3%} of bigrams."
	))
)
