import json

CORPUS = "corpus/parsed.json"
ALPHA = "abcdefghijklmnopqrstuvwxyz"

with open(CORPUS, "r") as file:
    iterator = ((letter, int(freq)) for letter, freq in json.load(file)[0].items() if letter in ALPHA)
    letters, freqs = zip(*sorted(iterator, key=lambda i: i[1], reverse=True))
    total = sum(freqs)

    letters = "[" + ', '.join(letters) + "]"
    bar = "[" + ', '.join(str(freq / total * 100) for freq in freqs) + "]"
    print(
f"""
```mermaid
xychart-beta horizontal
	title "English Letter Frequencies"
	y-axis "Frequencies (%)" 0 --> 100
	x-axis "Letters" {letters}
	bar {bar}
```
"""
    )
