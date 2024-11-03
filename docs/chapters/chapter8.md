---
layout: page
title: "Chapter 8"
---


# Trigram stats (14 min)

## Alts, rolls, 3rolls & redir

There are four stats that highlight what hand motions are most common in a particular layout. These are calculated based on trigrams (three key sequences):

ALTERNATE: pressing one key with one hand, then one with the other, then back to the first (1, 1, 1). In other words, a pure alternating trigram. E.g: Qwerty AND.

ROLL: pressing two keys with one hand, and a third key with the other (2, 1 or 1, 2). In other words, a 2 key roll following or preceding a hand change. E.g: Qwerty OUR.

3ROLL (also called “onehand”): a one-handed trigram where all keys go in the same direction. In other words, a trigram roll. For example, Qwerty WER.

REDIRECT: a one-handed trigram in which the direction changes. For example, Qwerty SAD is a redirect, as SA is outward while AD is inward. Whether redirects should be minimized or not is a matter of personal preference.

The stats above are based on trigrams to avoid redirects being counted as rolls. For example, if we used bigrams to calculate the stats instead, sequences like DFDFDF could be labeled as multiple rolls, when it's really just a long one-handed sequence.

## The relation between alts, rolls, 3rolls and redir

Below we list the trigram stats for five layouts. The layouts are sorted from higher to lower alternation. The numbers show percentages, although the % symbol has been omitted:



Alt
rolls
3rolls
Redir
Poqtea
Maximal
46.8
Minimal
35.3
Very low
1.2
High
7.5
Graphite
Very high
40.2
Mid
45.1
Mid low
2.6
Very low
3.4
Rolly
Mid low
32.1
High
49
Mid
3.5
Mid high
6.9
Inrolly
Low
26.7
Maximal
52.3
Mid
3.8
High
8.2
Seht Drai
Minimal
22
High
48.4
Maximal
10.6
Very high
10.6


We can identify some patterns from the table:

Lower alternation leads to higher rolling, but also higher redirects. In fact, check the huge difference in total rolling (i.e. rolls + 3rolls) between a max alternation layout like Poqtea (36.5% total rolls) vs Seht Drai (59% total rolls)

Conversely, higher alternation leads to lower rolling, and lower redirects. However, Poqtea (T + vowels setup) is an exception, as it has high redirects despite the high alternation. In all other cases, high alternation will lead to lower redirects.

In any case, the takeaway is that no keyboard layout can fully optimize all the stats, as maximizing one stat will necessarily make other stats worse. So, all layouts will have their pros and cons.

## Balancing alternation & rolling

Which to favor between rolling and alternation is subjective. It can be said that alternation offers a more consistent typing experience, as it feels rhythmic and minimizes awkward sequences. Meanwhile, rolling has higher highs (words that feel very smooth) but lower lows (long same hand sequences). Regardless, it is not a matter of one or the other. Think of it more as a scale, with max alternation on one end and max rolling on the other. We have to decide where on that scale we want our layout to be.

## Which consonants lead to higher or lower rolling

Most layouts place all the vowels on one hand. Doing so leads to a healthy amount of alternation, which ensures there are fewer long same hand sequences and redirects.

Even if we know where the vowels will be, we still have to decide what consonants we want to place on the vowel side. To help us with that we will use the table below, which shows how much each consonant combines with the vowels vs with the consonants. For example, we can see that R + vowels amount to 9.38% of all bigrams, while R + consonants is 4.19%. The table is sorted based on the third column (vowel column minus consonant column). Additionally, the main consonants (i.e. T, N, S, R and H) are highlighted, as their placement will have the most effect on a layout’s stats. Anyway, X, J, Q and Z were omitted:



vowels
cons
 v-c
r
9.38
4.19
 5.19
n
9.946
5.279
 4.667
m
3.788
1.114
 2.674
v
2.237
0.194
 2.043
f
2.903
0.866
 2.037
c
4.405
2.505
 1.9
l
5.264
3.47
 1.794
s
6.492
4.802
 1.69
d
3.864
2.313
 1.551












w
1.851
0.717
 1.134
b
1.75
0.8
 0.95
p
2.214
1.902
 0.312
k
0.571
0.464
 0.107
g
1.704
1.813
-0.109
h
5.387
5.563
-0.176
t
8.243
8.62
-0.377
y
0.691
1.733
-1.042


* table data: Norvig



Generally, the consonants at the top on the table (e.g. R and N) will increase rolling the most when placed on the same hand as the vowels. Conversely, the letters at the bottom (e.g. H and T) will favor alternation instead. While this holds mostly true, it is only a generalization. To get a more accurate picture we need to look at trigrams. We do that on the next page.

## Common trigrams, rolls & alternation

In order to get a deeper understanding of where a layout’s stats are coming from, we can look at the most common trigrams for a given letter, and check how those trigrams would be typed depending if said letter was on the vowel or the consonant hand. Below are some conclusions we can extract after doing this with the main consonants:
Graphite (StronglyTyped)
b l d w z  ' f o u j ;
n r t s g  y h a e i ,
q x m c v  k p . - /
Inrolly (Ec0vid)
y o u q x  k d l w ,  
i a e n j  v h t s c '
 " - r b z  f p m g .
Poqtea (Ian Douglas)
y w f l m  k p o q - /
u r s n h  d t e a i '
z x c v j  b g , . ;


H gives decent rolling regardless if we place it on the vowel hand or not. To understand why this is the case, we will use the following trigrams: THE, THA & THI.

On the Graphite layout (H on the vowel hand) T–HE, T–HA and T–HI are typed by pressing one key with one hand, and two with the other. Same applies to Inrolly (H on the consonant hand) only that the trigrams are now type as TH–E, TH–A and TH–I. So, they are rolls either way, it is just that the part that is a roll changes.

T maximizes alternation on the vowel hand. This is because the very common T–H–E, T–H–A and T–H–I trigrams are now alternates (i.e. they are typed by pressing only one key at a time, then changing hands). See Poqtea for a layout example. Anyway, if we want good rolling, T should always stay on the consonant hand.

R and N maximize rolling on the vowel hand. A good example of this is Inrolly, which has tons of rolls. We have the frequent N + vowels rolls (IN, AN, ON, EN…), the R + vowel rolls (ER, RE, OR, AR…), some common 3rolls (YOU, OUR, ION, REA…) plus all the consonant rolls (TH, ST, CH, CT, WH, TS, SH, LD…).

If we want, we can check less frequent letters as well. For example, D and G favor rolling on the consonant side because the common A–ND and I–NG trigrams are rolls. However, on the vowel side D and G now favor alternation, as A–N–D and I–N–G become alternates.

## Roll comfort

The following are the main factors affecting how comfortable a roll will be:

Ideally, we want the two keys in the bigram to share the same row.

When the keys are either one or two rows apart, it is preferable for the longer fingers to the higher one (e.g. it is more comfortable for the middle finger to be higher than the index, ring or pinky, rather than the other way around).

Rolls that do not involve any lateral stretch motion (resulting from pressing two keys that are far apart) are more comfortable than those that do.

Rolls that are typed with strong fingers (index and middle) are generally considered better than rolls that involve weaker fingers (ring and pinky).

Some people prefer rolls that are on adjacent fingers. The adjacent finger pairings are: pinky - ring, ring - middle and middle - index. Meanwhile, the non adjacent finger pairings are: pinky - middle, ring - index and pinky - index.

Finally, some people like taking roll direction into account as well. For example a middle - index finger roll can be either inwards (Qwerty DF) or outwards (Qwerty FD). There are layouts designed to favor inward rolls.

So, not all the rolls in a layout will necessarily be comfortable. After all, the basic roll definition (a trigram where we press two keys with one hand, and a third key with the other) is rather general, and can include bigrams such as scissors, lateral stretches, etc…

## Which consonants lead to higher or lower redirects

The first rule for minimizing redirects is having all vowels on the same hand. This is because vowels on one side ensures alternation, which reduces redirects.

Next, we want to identify which consonants roll in a single direction with the vowels, as that too will minimize redirects. After all, redirects are a change in direction.

The table below shows how much each consonant favors one direction vs the other (i.e. consonant → vowel vs vowel → consonant). Letters that score high in one direction but low on the other appear higher on the table, indicating that they are more unidirectional. Lastly, the fourth column shows the ratio in which each consonant favors its preferred direction:



c→v
v→c
Favored
direction
ratio
h
5.322
0.064
H → vowel
83.2
n
1.921
8.025
Vowel → N
4.18
w
1.343
0.508
W → vowel
2.64
b
1.209
0.541
B → vowel
2.23
s
2.409
4.083
Vowel → S
1.69
p
1.391
0.824
P → vowel
1.69
k
0.338
0.233
K → vowel
1.45
v
1.308
0.929
V → vowel
1.41
y
0.288
0.402
Vowel → Y
1.4















f
1.269
1.634
Vowel → F
1.29
r
4.123
5.258
Vowel → R
1.28
m
2.127
1.661
M → vowel
1.28
c
2.428
1.978
C → vowel
1.23
d
1.746
2.118
Vowel → D
1.21
g
0.903
0.801
G → vowel
1.13
t
4.374
3.87
T → vowel
1.13
l
2.503
2.761
Vowel → L
1.10


* table data: Norvig



We can see that any layout that aims to minimize redirects will place the letter H with the vowels, as H only combines with them in a single direction (ratio of 83 to 1!). On the other side of the spectrum, placing R or T with the vowels will noticeably increase redirects, as they combine with the vowels in both directions about equally.

## Common trigrams & redirects 

As a general rule, redirects are the result of increasing rolling in a layout. The following are the main letter patterns that will lead to redirects:
Rolly (Ec0vid)
y o u f j  q m w l ,
i a e n b  k t s r c '
 ; " h p z  v d g x .
Inrolly (Ec0vid)
y o u q x  k d l w ,  
i a e n j  v h t s c '
 " - r b z  f p m g .

Vowel → consonant → vowel trigrams. These will inevitably be redirects when all three letters are on the same hand. For example, ERE, ONE & ARE on Inrolly.

Consonant → vowel → consonant trigrams. These would also be redirects if the three letters share one side. For example, HIN, HEN & HAN on Rolly.

Vowel → vowel, followed or preceded by a consonant. These are redirects or 3rolls depending on our vowel setup. For instance, on Inrolly, EAR & AIN are redirects, but OUR, ION & REA are 3rolls.

Consonant only trigrams. These are redirects or 3rolls depending on our consonant setup. For example, STR on Rolly is a redirect.

Trigrams with punctuation. For example, T'S is a redirect on either Rolly or Inrolly.

Ideally, we want all three keys in a redirect to share the same row (e.g. AIN or STR or Rolly). However, in practice many redirects will have just two letters on the same row, while a third letter is on a different row (e.g. ONE, HIN, HEN or HAN on Rolly).

Another aspect that affects how a redirect will feel is if it has SFS or not. If it does, then the redirect is typed with just two fingers, as one finger is utilized twice (e.g. HIN, HEN or HAN on Rolly). If there is no SFS, then three fingers will be used (e.g. AIN, ONE or STR on Rolly).

## “Weak” redirects

Redirects where the index finger is not utilized are sometimes referred to as “weak” or “bad” redirects, as they are trickier to type. Having said that, people who have developed good finger independence and dexterity with their weaker fingers (from playing a musical instrument for example) will probably not mind “weak” redirects at all.
Seht Drai (Tanamr)
f u l v b  q g n o j
s e h t k  ' d r a i .
 ; m p w z  y c x / ,

The SHE trigram is a weak redirect on Seht Drai, while STE is not. Similarly, AIN is a weak redirect, but not DON.

Most trigrams in the English language (and therefore most redirects) involve both vowels and consonants. Conversely, vowel only trigrams are extremely rare. So, in order to minimize weak redirects, we must place all the vowels on the same hand and on our last three fingers specifically (pinky, ring and middle). As such:
Whix (Ec0vid)
f l n d k  ' w o u j
s r h t v  y c a e i
 x b m z q  p g . " ,

On the right hand, with consonants being on the index finger, and vowels on middle, ring and pinky, we ensure that any trigram with both vowels + consonants will involve the index.

It should be noted that, although vowel only trigrams are rare in English, there are actually some common consonant only trigrams. Regardless, with the right letter arrangement we can avoid weak redirects on the consonant hand as well. For example, none of the redirects on Whix’s left hand (STR, NDS, RST, NST, NTS, RTH…) are weak redirects.

8.10. Common trigrams & 3rolls

Layouts that aim to maximize 3rolls necessarily have to split the vowels, placing three vowels on one hand, and two on the other. This is done so that the most common trigram in the English language (THE) can be a 3roll on one hand, while on the other hand we have some of the next most common trigrams as 3rolls too (ING, AND, ION…). An example of such a layout would be Seht Drai (angle modded) which maximizes 3rolls while also doing a great job at optimizing other layout stats like SFBs, SFSs, etc…
Seht Drai (Tanamr)
f u l v b  q g n o j
s e h t k  ' d r a i .
 ; m p w z  y c x / ,

The following are the 3rolls on Seht Drai. For each hand, they are sorted based on frequency (on the TypeRacer corpus):

Left hand: THE, WHE, PLE, BLE, SEL, LES, TLE...
Right hand: ING, AND, ION, IND, ANY, ON', ONG, ARD, ANG, ANC, ORD…

Ideally, we want all the letters in a 3roll to be on the same row (e.g. THE, ONG or ARD). However, we can only have a few 3rolls like that in a layout. The best we can hope for most 3rolls is having two of the letters sharing a row. See all the remaining 3rolls on Seht Drai other than PLE, ANY and ANC (those three have each letter on a different row).

Anyway, the disadvantage of utilizing a 3-2 vowel split is that alternation plummets, meaning redirects and long same hand sequences will be way higher than on other layouts.
