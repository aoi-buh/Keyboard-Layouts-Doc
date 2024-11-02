---
layout: default
title: "Chapter 2"
---

# Chapter 2: English data (5 min)

To understand where the stats for a layout are coming from, first we need to be familiar with the letter, bigram and trigram frequency of the language the layout is for. Most layouts were designed for English, so that is what we will be looking at.

Note: the bigram and trigram tables in the following sections were created using the [Monkeyracer corpus](https://github.com/o-x-e-y/oxeylyzer/blob/main/static/language_data/monkeyracer.json).

## English letter frequency

<div class='mermaid'>
xychart-beta horizontal
    title "English Letter Frequency"
    x-axis [e, t, o, a, i, n, s, r, h, l, d, u, y, m, w, c, g, f, p, b, v, k, j, x, z, q]
    y-axis "Frequency (%)" 0 --> 20
    bar [11.50, 8.68, 7.63, 7.19, 6.61, 6.51, 5.66, 5.15, 5.04, 3.94, 3.47, 3.02, 2.48, 2.46, 2.25, 2.16, 2.00, 1.94, 1.52, 1.45, 1.04, 0.92, 0.15, 0.12, 0.07, 0.07]
</div>

As one would expect, the vowels `E`, `O`, `A`, `I` are very frequent, while the most common consonants are `T`, `N`, `S`, `R`. These 8 would be the most important letters. Afterwards we would have the letter `H`, followed by `L`, `D`, and then the vowel `U`.

Note that the results will vary to some extent when using a different corpus. For example, on popular typing websites like TypeRacer or MonkeyType the letter H has around the same usage as R, while W and Y are on par with C.

## Top 50 bigrams

**Two-letter sequences are known as `bigrams`.** The following is the top 50:

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| th    | 3.51% | ha    | 1.22% | is    | 0.94% | le    | 0.76% | wh    | 0.55% |
| he    | 2.79% | ng    | 1.18% | me    | 0.93% | ne    | 0.74% | ho    | 0.54% |
| in    | 2.27% | to    | 1.11% | ar    | 0.91% | of    | 0.71% | om    | 0.54% |
| an    | 1.93% | en    | 1.11% | hi    | 0.84% | ti    | 0.70% | ro    | 0.54% |
| ou    | 1.79% | it    | 1.09% | ea    | 0.83% | as    | 0.68% | ow    | 0.54% |
| er    | 1.76% | ve    | 1.05% | se    | 0.80% | li    | 0.67% | de    | 0.54% |
| re    | 1.67% | or    | 1.04% | al    | 0.79% | be    | 0.66% | wa    | 0.53% |
| on    | 1.34% | yo    | 0.98% | ll    | 0.79% | no    | 0.65% | ut    | 0.52% |
| nd    | 1.34% | es    | 0.97% | te    | 0.79% | nt    | 0.62% | el    | 0.51% |
| at    | 1.26% | st    | 0.95% | ed    | 0.76% | ur    | 0.56% | co    | 0.50% |

We can see that **most bigrams involve a consonant + a vowel.** Having said that, there are some consonant-only bigrams that are very common (e.g. `TH`, `ND`, `ST`, `NT`, `NG`, `CH`, `LL`...). Lastly, the most relevant vowel-only bigrams are `OU`, `IO` and `EA`.

## Top 50 trigrams

**Three-letter sequences are known as `trigrams`.** The following is the top 50:

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| the   | 2.86% | all   | 0.47% | ter   | 0.34% | tio   | 0.28% | ers   | 0.24% |
| ing   | 1.33% | for   | 0.46% | rea   | 0.34% | ill   | 0.28% | ive   | 0.24% |
| you   | 1.30% | hin   | 0.46% | not   | 0.34% | but   | 0.28% | hav   | 0.24% |
| and   | 1.28% | eve   | 0.45% | are   | 0.33% | out   | 0.28% | ate   | 0.23% |
| hat   | 0.84% | our   | 0.43% | ght   | 0.30% | igh   | 0.27% | hey   | 0.22% |
| tha   | 0.69% | ome   | 0.38% | ave   | 0.30% | was   | 0.26% | nce   | 0.22% |
| her   | 0.63% | ion   | 0.37% | ith   | 0.30% | whe   | 0.25% | com   | 0.22% |
| thi   | 0.62% | ent   | 0.36% | now   | 0.29% | hen   | 0.25% | ess   | 0.22% |
| ere   | 0.51% | one   | 0.36% | ear   | 0.28% | can   | 0.25% | wor   | 0.22% |
| ver   | 0.49% | his   | 0.36% | wit   | 0.28% | oul   | 0.24% | uld   | 0.22% |

**Most trigrams involve both consonants and vowels.** In fact, vowel only trigrams are extremely rare. Although not seen on the table, some consonant-only trigrams are decently common, though (e.g. `LLY`, `STR`, `NGS`...).

## Extended bigram tables

Over the following pages we look at bigram data in more detail. In order to make the information easier to digest, we will subdivide bigrams into different tables:

- [Vowel + vowel bigrams](#vowel-+-vowel-bigrams)
- [Consonant + consonant bigrams](#consonant-+-consonant-bigrams)
- [Consonant + vowel bigrams](#consonant-+-vowel-bigrams)
- [Double letters](#double-letters)

For a given table, bigrams will be sorted from most to least frequent. The number next to each bigram will indicate its frequency in percent (e.g. `OU` amounts to 0.870% of bigrams).

At the end of this chapter you will also find some additional data:

- [Consonant only trigrams](#consonant-only-trigrams)
- [Consonant only trigrams (excluding Y)](#consonant-only-trigrams-(excluding-Y))
- [Top words with apostrophe](#top-words-with-apostrophe)
- [Top trigrams with apostrophe](#top-trigrams-with-apostrophe)

## Vowel + vowel bigrams

| 1-10  | freq  | 11-20 | freq  |
| ----- | ----- | ----- | ----- |
| ou    | 1.79% | oi    | 0.10% |
| ea    | 0.83% | ia    | 0.10% |
| ee    | 0.48% | ue    | 0.10% |
| io    | 0.33% | ui    | 0.08% |
| oo    | 0.32% | ua    | 0.07% |
| ie    | 0.29% | oe    | 0.06% |
| ai    | 0.28% | oa    | 0.04% |
| ei    | 0.14% | eu    | 0.01% |
| au    | 0.14% | iu    | 0.01% |
| eo    | 0.11% | uo    | 0.01% |

Vowel bigrams amount to 5.267% of bigrams.

## Consonant + consonant bigrams

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| th    | 3.51% | ld    | 0.34% | nc    | 0.23% | rd    | 0.16% | pp    | 0.11% |
| nd    | 1.34% | gh    | 0.33% | ct    | 0.22% | ty    | 0.15% | wn    | 0.11% |
| ng    | 1.18% | ns    | 0.31% | ht    | 0.22% | ds    | 0.14% | br    | 0.11% |
| st    | 0.95% | tr    | 0.31% | pr    | 0.22% | gr    | 0.14% | nk    | 0.11% |
| ll    | 0.79% | sh    | 0.29% | ts    | 0.22% | mp    | 0.14% | rl    | 0.11% |
| nt    | 0.62% | ry    | 0.28% | bl    | 0.19% | sp    | 0.14% | dr    | 0.10% |
| wh    | 0.55% | ss    | 0.27% | tt    | 0.18% | ny    | 0.14% | tl    | 0.10% |
| ch    | 0.40% | rt    | 0.26% | fr    | 0.18% | rn    | 0.13% | ls    | 0.10% |
| ly    | 0.36% | pl    | 0.23% | kn    | 0.18% | cr    | 0.12% | rr    | 0.10% |
| rs    | 0.35% | my    | 0.23% | ck    | 0.17% | ys    | 0.12% | ff    | 0.10% |

Consonant bigrams amount to about 20.824% of bigrams.

## Consonant + vowel bigrams

<table markdown='1'>
	<tr>
		<th>T + vowels</th>
		<th>N + vowels</th>
		<th>S + vowels</th>
		<th>R + vowels</th>
		<th>H + vowels</th>
		<th>L + vowels</th>
		<th>D + vowels</th>
		<th>Y + vowels</th>
		<th>M + vowels</th>
		<th>W + vowels</th>
		<th>C + vowels</th>
		<th>G + vowels</th>
		<th>F + vowels</th>
		<th>P + vowels</th>
		<th>B + vowels</th>
		<th>V + vowels</th>
		<th>K + vowels</th>
		<th>J + vowels</th>
		<th>X + vowels</th>
		<th>Z + vowels</th>
		<th>Q + vowels</th>
	</tr>
<tr><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| at     | 1.26% |
| to     | 1.11% |
| it     | 1.09% |
| te     | 0.79% |
| ti     | 0.70% |
| ut     | 0.52% |
| ot     | 0.47% |
| et     | 0.47% |
| ta     | 0.39% |
| tu     | 0.17% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| in     | 2.27% |
| an     | 1.93% |
| on     | 1.34% |
| en     | 1.11% |
| ne     | 0.74% |
| no     | 0.65% |
| un     | 0.36% |
| ni     | 0.23% |
| na     | 0.19% |
| nu     | 0.04% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| es     | 0.97% |
| is     | 0.94% |
| se     | 0.80% |
| as     | 0.68% |
| us     | 0.48% |
| so     | 0.46% |
| si     | 0.34% |
| os     | 0.24% |
| sa     | 0.22% |
| su     | 0.19% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| er     | 1.76% |
| re     | 1.67% |
| or     | 1.04% |
| ar     | 0.91% |
| ur     | 0.56% |
| ro     | 0.54% |
| ri     | 0.49% |
| ra     | 0.38% |
| ir     | 0.25% |
| ru     | 0.13% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| he     | 2.79% |
| ha     | 1.22% |
| hi     | 0.84% |
| ho     | 0.54% |
| hu     | 0.07% |
| eh     | 0.02% |
| oh     | 0.02% |
| ah     | 0.02% |
| uh     | 0.00% |
| ih     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| al     | 0.79% |
| le     | 0.76% |
| li     | 0.67% |
| el     | 0.51% |
| lo     | 0.44% |
| il     | 0.42% |
| la     | 0.32% |
| ul     | 0.32% |
| ol     | 0.25% |
| lu     | 0.08% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ed     | 0.76% |
| de     | 0.54% |
| do     | 0.39% |
| ad     | 0.31% |
| di     | 0.30% |
| id     | 0.26% |
| od     | 0.18% |
| da     | 0.17% |
| du     | 0.05% |
| ud     | 0.05% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| yo     | 0.98% |
| ay     | 0.37% |
| ey     | 0.23% |
| ye     | 0.11% |
| yi     | 0.05% |
| oy     | 0.04% |
| uy     | 0.02% |
| ya     | 0.01% |
| yu     | 0.00% |
| iy     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| me     | 0.93% |
| om     | 0.54% |
| ma     | 0.49% |
| mo     | 0.31% |
| im     | 0.31% |
| em     | 0.30% |
| am     | 0.25% |
| mi     | 0.24% |
| um     | 0.10% |
| mu     | 0.10% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ow     | 0.54% |
| wa     | 0.53% |
| we     | 0.47% |
| wi     | 0.41% |
| wo     | 0.31% |
| ew     | 0.09% |
| aw     | 0.07% |
| wu     | 0.00% |
| iw     | 0.00% |
| uw     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| co     | 0.50% |
| ca     | 0.49% |
| ce     | 0.43% |
| ac     | 0.35% |
| ic     | 0.34% |
| ec     | 0.30% |
| ci     | 0.14% |
| uc     | 0.12% |
| oc     | 0.08% |
| cu     | 0.08% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ge     | 0.34% |
| ig     | 0.27% |
| go     | 0.26% |
| ag     | 0.16% |
| ug     | 0.15% |
| gi     | 0.13% |
| ga     | 0.11% |
| gu     | 0.07% |
| eg     | 0.06% |
| og     | 0.06% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| of     | 0.71% |
| fo     | 0.40% |
| if     | 0.29% |
| fe     | 0.29% |
| fi     | 0.23% |
| fa     | 0.17% |
| ef     | 0.11% |
| fu     | 0.09% |
| af     | 0.05% |
| uf     | 0.02% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| pe     | 0.40% |
| pa     | 0.21% |
| po     | 0.21% |
| op     | 0.20% |
| ap     | 0.15% |
| up     | 0.14% |
| ep     | 0.12% |
| pi     | 0.11% |
| pu     | 0.07% |
| ip     | 0.05% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| be     | 0.66% |
| bu     | 0.26% |
| bo     | 0.23% |
| ab     | 0.19% |
| ba     | 0.15% |
| bi     | 0.09% |
| ob     | 0.07% |
| ib     | 0.06% |
| ub     | 0.04% |
| eb     | 0.02% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ve     | 1.05% |
| ev     | 0.37% |
| av     | 0.26% |
| iv     | 0.22% |
| ov     | 0.18% |
| vi     | 0.16% |
| va     | 0.06% |
| vo     | 0.05% |
| vu     | 0.00% |
| uv     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ke     | 0.39% |
| ak     | 0.19% |
| ki     | 0.16% |
| ik     | 0.13% |
| ok     | 0.11% |
| ek     | 0.02% |
| ka     | 0.02% |
| ku     | 0.00% |
| ko     | 0.00% |
| uk     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ju     | 0.11% |
| jo     | 0.04% |
| je     | 0.02% |
| ja     | 0.01% |
| aj     | 0.01% |
| ej     | 0.00% |
| ji     | 0.00% |
| oj     | 0.00% |
| ij     | 0.00% |
| uj     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ex     | 0.12% |
| xi     | 0.03% |
| ix     | 0.02% |
| xa     | 0.01% |
| ax     | 0.01% |
| xe     | 0.01% |
| ox     | 0.01% |
| ux     | 0.00% |
| xu     | 0.00% |
| xo     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| ze     | 0.04% |
| iz     | 0.04% |
| az     | 0.02% |
| za     | 0.01% |
| zi     | 0.01% |
| zo     | 0.01% |
| ez     | 0.01% |
| oz     | 0.00% |
| uz     | 0.00% |
| zu     | 0.00% |

</td><td markdown='1'>

| bigram | freq  |
| ------ | ----- |
| qu     | 0.08% |
| eq     | 0.02% |
| iq     | 0.00% |
| aq     | 0.00% |
| oq     | 0.00% |
| qi     | 0.00% |
| uq     | 0.00% |
| qa     | 0     |
| qe     | 0     |
| qo     | 0     |

</td></tr>
</table>

Consonant + vowel bigrams amount to about 64.085% of bigrams.

## Double letters

| char | freq  |
| ---- | ----- |
| ll   | 0.79% |
| ee   | 0.48% |
| oo   | 0.32% |
| ss   | 0.27% |
| tt   | 0.18% |
| pp   | 0.11% |
| rr   | 0.10% |
| ff   | 0.10% |
| nn   | 0.09% |
| mm   | 0.05% |
| cc   | 0.04% |
| dd   | 0.03% |
| gg   | 0.02% |
| bb   | 0.01% |
| zz   | 0.01% |
| aa   | 0.00% |
| ii   | 0.00% |
| uu   | 0.00% |
| hh   | 0.00% |
| vv   | 0.00% |
| kk   | 0.00% |
| yy   | 0.00% |
| xx   | 0.00% |

Double letters amount to about 2.603% of bigrams.

## Consonant only trigrams

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| ght   | 0.30% | nst   | 0.06% | ntr   | 0.04% | ldn   | 0.02% | sky   | 0.02% |
| lly   | 0.13% | ttl   | 0.06% | ryt   | 0.04% | bly   | 0.02% | ppy   | 0.02% |
| str   | 0.13% | nts   | 0.06% | lls   | 0.03% | rly   | 0.02% | cts   | 0.02% |
| ngs   | 0.11% | rth   | 0.05% | ngl   | 0.03% | hts   | 0.02% | rch   | 0.02% |
| nly   | 0.10% | mpl   | 0.05% | rry   | 0.03% | rty   | 0.02% | rms   | 0.02% |
| rld   | 0.09% | try   | 0.05% | nyt   | 0.03% | yst   | 0.02% | mpt   | 0.02% |
| thr   | 0.09% | tly   | 0.05% | mys   | 0.03% | nch   | 0.02% | ply   | 0.02% |
| nds   | 0.08% | tch   | 0.05% | ntl   | 0.03% | scr   | 0.02% | dly   | 0.02% |
| rst   | 0.08% | rds   | 0.04% | sts   | 0.03% | sch   | 0.02% | ndr   | 0.02% |
| yth   | 0.07% | why   | 0.04% | rts   | 0.02% | cks   | 0.02% | ppr   | 0.01% |

## Consonant only trigrams (excluding Y)

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| ght   | 0.30% | rth   | 0.05% | ldn   | 0.02% | ndr   | 0.02% | mpr   | 0.01% |
| str   | 0.13% | mpl   | 0.05% | hts   | 0.02% | ppr   | 0.01% | ths   | 0.01% |
| ngs   | 0.11% | tch   | 0.05% | nch   | 0.02% | ctl   | 0.01% | rns   | 0.01% |
| rld   | 0.09% | rds   | 0.04% | scr   | 0.02% | stl   | 0.01% | lds   | 0.01% |
| thr   | 0.09% | ntr   | 0.04% | sch   | 0.02% | nsw   | 0.01% | ngt   | 0.01% |
| nds   | 0.08% | lls   | 0.03% | cks   | 0.02% | nth   | 0.01% | ldr   | 0.01% |
| rst   | 0.08% | ngl   | 0.03% | cts   | 0.02% | mbl   | 0.01% | ckl   | 0.01% |
| nst   | 0.06% | ntl   | 0.03% | rch   | 0.02% | xpl   | 0.01% | spr   | 0.01% |
| ttl   | 0.06% | sts   | 0.03% | rms   | 0.02% | lth   | 0.01% | nct   | 0.01% |
| nts   | 0.06% | rts   | 0.02% | mpt   | 0.02% | ndl   | 0.01% | ncl   | 0.01% |

## Top words with apostrophe

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| it's | 0.35% | didn't | 0.06% | what's | 0.03% | aren't | 0.02% | world's | 0.01% |
| don't | 0.32% | they're | 0.06% | we've | 0.03% | they'll | 0.02% | we'd | 0.01% |
| i'm | 0.30% | you've | 0.06% | we'll | 0.03% | haven't | 0.01% | he'll | 0.01% |
| you're | 0.22% | he's | 0.05% | wouldn't | 0.03% | man's | 0.01% | they'd | 0.01% |
| that's | 0.14% | you'll | 0.05% | ain't | 0.02% | one's | 0.01% | people's | 0.01% |
| can't | 0.12% | doesn't | 0.05% | couldn't | 0.02% | 'em | 0.01% | hadn't | 0.01% |
| i've | 0.11% | won't | 0.05% | let's | 0.02% | who's | 0.01% | weren't | 0.01% |
| there's | 0.10% | i'd | 0.05% | wasn't | 0.02% | he'd | 0.01% | it'll | 0.01% |
| i'll | 0.10% | 'cause | 0.04% | you'd | 0.02% | they've | 0.01% | else's | 0.01% |
| we're | 0.07% | isn't | 0.04% | she's | 0.02% | shouldn't | 0.01% | here's | 0.00% |

The tables above was made using the [Monkeyracer corpus](https://cdn.discordapp.com/attachments/807844118826975262/1092588831955501056/mt.txt?ex=672561a4&is=67241024&hm=fa1c6965e882428336263b6c8ecfb7a143f8cde7d83fd9229c2b1e5caaa49f60&) parsed seperately.

## Top trigrams with apostrophe

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- |
| n't   | 0.31% | 'll   | 0.08% | he'   | 0.04% |
| t's   | 0.22% | at'   | 0.07% | in'   | 0.03% |
| on'   | 0.15% | an'   | 0.06% | e'r   | 0.03% |
| it'   | 0.14% | we'   | 0.05% | y'r   | 0.03% |
| 're   | 0.14% | dn'   | 0.05% | u'v   | 0.02% |
| ou'   | 0.14% | re'   | 0.05% | u'l   | 0.02% |
| i'm   | 0.12% | i'v   | 0.04% | i'd   | 0.02% |
| e's   | 0.10% | sn'   | 0.04% | n's   | 0.02% |
| 've   | 0.09% | i'l   | 0.04% | en'   | 0.02% |
| u'r   | 0.09% | ey'   | 0.04% | r's   | 0.02% |

