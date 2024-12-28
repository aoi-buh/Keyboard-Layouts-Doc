import json

CORPUS = "corpus/parsed.json"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
CONS_NO_Y = "bcdfghjklmnpqrstvwxz"

alpha_only: tuple

with open(CORPUS, "r") as file:
	alpha_only = tuple(i for i in json.load(file)[2].items() if all(j in ALPHA for j in i[0]))

total = sum(trigram[1] for trigram in alpha_only)
cons_no_y = (i for i in alpha_only if all(j in CONS_NO_Y for j in i[0]))
trigrams = sorted(cons_no_y, key=lambda i: i[1], reverse=True)
cons_no_y_total = sum(freq for _, freq in trigrams)

print(
	'\n'.join((
		"| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |",
		"| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |",
		*("| " + ' | '.join(f"{trigrams[i+j][0]:<5} | {trigrams[i+j][1] / total:>5.2%}" for j in range(0, 50, 10)) + " |" for i in range(10)),
		"",
		f"Consonant trigrams without `Y` amount to {cons_no_y_total / total:.3%} of trigrams."
	))
)
