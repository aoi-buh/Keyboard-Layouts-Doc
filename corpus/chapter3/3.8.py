import json

CORPUS = "corpus/parsed.json"
ALPHA = "abcdefghijklmnopqrstuvwxyz"

alpha_only: tuple

with open(CORPUS, "r") as file:
	alpha_only = tuple(i for i in json.load(file)[1].items() if all(j in ALPHA for j in i[0]))

total = sum(freq for _, freq in alpha_only)
repeats = sorted((i for i in alpha_only if i[0][0] == i[0][1]), key=lambda i: i[1], reverse=True)
repeat_total = sum(freq for _, freq in repeats)

print(
	'\n'.join((
		"| char | freq  | count |",
		"| ---- | ----- | ----- |",
		*(f"| {gram:<4} | {freq / total:>5.2%} | {freq:>5} |" for gram, freq in repeats),
		"",
		f"Double letters amount to about {repeat_total / total:.3%} of bigrams.",
	))
)
