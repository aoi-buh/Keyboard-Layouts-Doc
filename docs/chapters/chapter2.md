---
layout: default
title: "Chapter 2"
---

# Chapter 2: English data (5 min)

To understand where the stats for a layout are coming from, first we need to be familiar with the letter, bigram and trigram frequency of the language the layout is for. Most layouts were designed for English, so that is what we will be looking at.

Note: the bigram and trigram tables in the following sections were created using the [Monkeyracer corpus](https://cdn.discordapp.com/attachments/807844118826975262/1092588831955501056/mt.txt?ex=672561a4&is=67241024&hm=fa1c6965e882428336263b6c8ecfb7a143f8cde7d83fd9229c2b1e5caaa49f60&).

## English letter frequency

xychart-beta
    title ""
    x-axis [e, t, o, a, i, n, s, r, h, l, d, u, y, m, w, c, g, f, p, b, v, k, j, x, z, q]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [12.36, 9.33, 8.21, 7.73, 7.11, 7.00, 6.08, 5.53, 5.42, 4.24, 3.73, 3.25, 2.66, 2.64, 2.42, 2.32, 2.15, 2.09, 1.63, 1.56, 1.11, 0.99, 0.16, 0.13, 0.08, 0.07]
    line [12.36, 9.33, 8.21, 7.73, 7.11, 7.00, 6.08, 5.53, 5.42, 4.24, 3.73, 3.25, 2.66, 2.64, 2.42, 2.32, 2.15, 2.09, 1.63, 1.56, 1.11, 0.99, 0.16, 0.13, 0.08, 0.07]

As one would expect, the vowels `E`, `A`, `O`, `I` are very frequent, while the most common consonants are `T`, `N`, `S`, `R`. These 8 would be the most important letters. Afterwards we would have the letter `H`, followed by `L`, `D`, `C`, and then the vowel `U`.

Note that the results will vary to some extent when using a different corpus. For example, on popular typing websites like TypeRacer or MonkeyType the letter H has around the same usage as R, while W and Y are on par with C.

## Top 50 bigrams

**Two-letter sequences are known as `bigrams`.** The following is the top 50:

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| th    | 3.89% | ha    | 1.36% | is    | 1.05% | le    | 0.84% | wh    | 0.61% |
| he    | 3.09% | ng    | 1.31% | me    | 1.03% | ne    | 0.82% | ho    | 0.60% |
| in    | 2.51% | to    | 1.23% | ar    | 1.01% | of    | 0.79% | om    | 0.60% |
| an    | 2.14% | en    | 1.23% | hi    | 0.93% | ti    | 0.78% | ro    | 0.60% |
| ou    | 1.98% | it    | 1.21% | ea    | 0.92% | as    | 0.76% | ow    | 0.60% |
| er    | 1.95% | ve    | 1.16% | se    | 0.88% | li    | 0.74% | de    | 0.60% |
| re    | 1.85% | or    | 1.16% | al    | 0.88% | be    | 0.73% | wa    | 0.59% |
| on    | 1.49% | yo    | 1.08% | ll    | 0.88% | no    | 0.72% | ut    | 0.58% |
| nd    | 1.49% | es    | 1.08% | te    | 0.87% | nt    | 0.69% | el    | 0.57% |
| at    | 1.39% | st    | 1.06% | ed    | 0.85% | ur    | 0.62% | co    | 0.56% |

We can see that **most bigrams involve a consonant + a vowel.** Having said that, there are some consonant-only bigrams that are very common (e.g. `TH`, `ND`, `ST`, `NT`, `NG`, `CH`, `LL`...). Lastly, the most relevant vowel-only bigrams are `OU`, `IO` and `EA`.

## Top 50 trigrams

**Three-letter sequences are known as `trigrams`.** The following is the top 50:

| 1-10  | freq  | 11-20 | freq  | 21-30 | freq  | 31-40 | freq  | 41-50 | freq  |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| the   | 3.28% | all   | 0.54% | ter   | 0.39% | tio   | 0.32% | ers   | 0.27% |
| ing   | 1.53% | for   | 0.53% | rea   | 0.39% | ill   | 0.32% | ive   | 0.27% |
| you   | 1.50% | hin   | 0.53% | not   | 0.39% | but   | 0.32% | hav   | 0.27% |
| and   | 1.47% | eve   | 0.52% | are   | 0.38% | out   | 0.32% | ate   | 0.27% |
| hat   | 0.96% | our   | 0.50% | ght   | 0.35% | igh   | 0.31% | hey   | 0.26% |
| tha   | 0.79% | ome   | 0.44% | ave   | 0.35% | was   | 0.30% | nce   | 0.25% |
| her   | 0.72% | ion   | 0.42% | ith   | 0.34% | whe   | 0.29% | com   | 0.25% |
| thi   | 0.71% | ent   | 0.42% | now   | 0.33% | hen   | 0.29% | ess   | 0.25% |
| ere   | 0.59% | one   | 0.42% | ear   | 0.33% | can   | 0.28% | wor   | 0.25% |
| ver   | 0.57% | his   | 0.41% | wit   | 0.32% | oul   | 0.28% | uld   | 0.25% |

**Most trigrams involve both consonants and vowels.** In fact, vowel only trigrams are extremely rare. Although not seen on the table, some consonant-only trigrams are decently common, though (e.g. `LLY`, `STR`, `NGS`...).

## Extended bigram tables

Over the following pages we look at bigram data in more detail. In order to make the information easier to digest, we will subdivide bigrams into different tables:

- Vowel + vowel bigrams
- Consonant + consonant bigrams
- Consonant + vowel bigrams
- Double letters

For a given table, bigrams will be sorted from most to least frequent. The number next to each bigram will indicate its frequency in percent (e.g. `OU` amounts to 0.870% of bigrams).

At the end of this chapter you will also find some additional data:

- Consonant only trigrams
- Consonant only trigrams (excluding Y)
- Top words with apostrophe
- Top trigrams with apostrophe

## Vowel + vowel bigrams

1-10
ou
0.870
io
0.835
ea
0.688
ie
0.385
ai
0.316
ia
0.286
ei
0.183
ue
0.147
ua
0.136
au
0.119




11-20
ui
0.101
oi
0.088
eo
0.073
oa
0.057
oe
0.039
eu
0.031
iu
0.017
ae
0.012
uo
0.011
ao
0.005




Vowel bigrams amount to 4.4% of bigrams.

## Consonant + consonant bigrams

1-10
th
3.556
nd
1.352
st
1.053
nt
1.041
ng
0.953
ch
0.598
ns
0.509
pr
0.474
ct
0.461
tr
0.426




11-20
ly
0.425
nc
0.416
rs
0.397
wh
0.379
rt
0.362
ts
0.337
sh
0.315
pl
0.263
ld
0.253
ry
0.248




21-30
mp
0.239
bl
0.233
gh
0.228
ty
0.227
fr
0.213
gr
0.197
sp
0.191
rd
0.189
by
0.176
rm
0.175




31-40
rn
0.160
sc
0.155
cr
0.149
cl
0.149
ls
0.142
ht
0.130
ds
0.126
lt
0.124
rc
0.121
ck
0.118




41-50
br
0.112
pt
0.106
rg
0.100
tl
0.098
ny
0.098
rk
0.097
ys
0.097
ph
0.094
ms
0.093
mb
0.090




Consonant bigrams amount to 21.406% of bigrams.

## Consonant + vowel bigrams

Bigrams under 0.175% frequency are omitted. As expected, less common consonants have fewer bigrams that make the cut. In fact, Q, J and Z have none. The top 50 are highlighted:

T + vowels
at
1.487
ti
1.343
te
1.205
it
1.123
to
1.041
ta
0.530
ot
0.442
et
0.413
ut
0.405
tu
0.255




N + vowels
in
2.433
an
1.985
on
1.758
en
1.454
ne
0.692
no
0.465
un
0.394
na
0.347
ni
0.339




S + vowels
es
1.339
is
1.128
se
0.932
as
0.871
si
0.550
us
0.454
so
0.398
su
0.311
os
0.290
sa
0.218




R + vowels
er
2.048
re
1.854
or
1.277
ar
1.075
ri
0.728
ro
0.727
ra
0.686
ur
0.543
ir
0.315




H + vowels
he
3.075
ha
0.926
hi
0.763
ho
0.485




L + vowels
al
1.087
le
0.829
li
0.624
el
0.530
la
0.528
il
0.432
lo
0.387
ol
0.365
ul
0.346




D + vowels
ed
1.168
de
0.765
di
0.493
ad
0.368
id
0.296
od
0.195
do
0.188




C + vowels
co
0.794
ic
0.699
ce
0.651
ca
0.538
ec
0.477
ac
0.448
ci
0.281
uc
0.188







M + vowels
me
0.793
ma
0.565
om
0.546
em
0.374
mo
0.337
im
0.318
mi
0.318
am
0.285




F + vowels
of
1.175
fo
0.488
fi
0.285
fe
0.237
if
0.203




P + vowels
pe
0.478
po
0.361
pa
0.324
op
0.224
ap
0.203




G + vowels
ge
0.385
ig
0.255
ag
0.205




W + vowels
wa
0.385
wi
0.374
we
0.361
ow
0.330
wo
0.222




Y + vowels
ay
0.217




B + vowels
be
0.576
ab
0.230
bo
0.195
bu
0.185




V + vowels
ve
0.825
iv
0.288
vi
0.270
ev
0.255
av
0.205
ov
0.178




K + vowels
ke
0.214




X + vowels
ex
0.214








Consonant + vowel bigrams amount to 71.686% of bigrams.

## Double letters

1-10
ll
0.577
ss
0.405
ee
0.378
oo
0.210
tt
0.171
ff
0.146
pp
0.137
rr
0.121
mm
0.096
cc
0.083




11-20
nn
0.073
dd
0.043
gg
0.025
ii
0.023
bb
0.011
aa
0.003
xx
0.003
zz
0.003
hh
0.001
uu
0.001




21-26
jj
0.000
kk
0.000
qq
0.000
vv
0.000
ww
0.000
yy
0.000




Double letters amount to 2.508% of bigrams.

## Consonant only trigrams

1-10
ght
lly
str
ngs
nly
rld
nds
thr
rst
yth




11-20
nst
nts
ttl
mpl
rth
try
tly
tch
ntr
rds




21-30
ryt
why
lls
ngl
sts
rry
mys
ntl
nyt
rts




31-40
rly
ldn
yst
hts
bly
nch
rty
sky
cks
sch




41-50
scr
cts
rch
mpt
ppy
rms
dly
ppr
ply
ctl




## Consonant only trigrams (excluding Y)

1-10
ght
str
ngs
rld
nds
thr
rst
nst
nts
ttl




11-20
mpl
rth
tch
ntr
rds
lls
ngl
sts
ntl
rts




21-30
ldn
hts
nch
cks
sch
scr
cts
rch
mpt
rms




31-40
ppr
ctl
ndr
nth
nsw
xpl
lth
mpr
stl
mbl




41-50
rns
nct
ndl
ncl
ngt
ckl
ths
lds
ddl
ldr





The two tables above were made using the TypeRacer corpus.

## Top words with apostrophe

1-10
it's
don't
i'm
you're
that's
can't
i've
there's
i'll
we're




11-20
they're
didn't
you've
he's
i'd
you'll
won't
doesn't
'cause
isn't




21-30
what's
ain't
we'll
we've
wouldn't
couldn't
wasn't
let's
you'd
she's




31-40
man's
haven't
aren't
who's
they'll
'em
one's
he'd
he'll
they've




41-50
shouldn't
world's
hadn't
they'd
we'd
people's
weren't
else's
goin'
it'll




## Top trigrams with apostrophe

1-10
n't
t's
i'm
e's
u'r
i'v
i'l
e'r
y'r
u'v




11-20
i'd
u'l
n's
r's
e'l
y's
e'v
e'd
d's
u'd




21-30
o's
y'l
g's
y'v
a's
y'd
d'v
t'l
l's
h's





The two tables above were made using the TypeRacer corpus.

