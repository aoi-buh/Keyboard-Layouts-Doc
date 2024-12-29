
# **8. Trigram stats (14 min)**

## 8.1. Alts, rolls, 3rolls & redir

There are four stats that highlight what hand motions are most common in a particular layout. These are calculated based on trigrams (three key sequences):

- **ALTERNATE:** pressing one key with one hand, then one with the other, then back to the first (1, 1, 1). In other words, a pure alternating trigram. E.g: Qwerty `AND`.
- **ROLL:** pressing two keys with one hand, and a third key with the other (2, 1 or 1, 2). In other words, a 2 key roll following or preceding a hand change. E.g: Qwerty `OUR`. Note that the two keys must be pressed by different fingers.
- **3ROLL** (also called "onehand"): a one-handed trigram where all keys go in the same direction. In other words, a trigram roll. For example, Qwerty `WER`.
- **REDIRECT:** a one-handed trigram in which the direction changes. For example, Qwerty `SAD` is a redirect, as `SA` is outward while `AD` is inward. Whether redirects should be minimized or not is a matter of personal preference.

The stats above are based on trigrams to avoid redirects being counted as rolls. For example, if we used bigrams to calculate the stats instead, sequences like `DFDFDF` could be labeled as multiple rolls, when it's really just a long one-handed sequence.

## 8.2. The relation between alts, rolls, 3rolls and redir

Below we list the trigram stats for five layouts. The layouts are sorted from higher to lower alternation. The numbers show percentages, although the % symbol has been omitted:

| Layouts | Alt | 2rolls | 3rolls | Redir |
| - | - | - | - | - |
| **Poqtea** | ${\color{green}Maximal}$<br>46.8 | ${\color{red}Minimal}$<br>35.3 | ${\color{red}Very\ low}$<br>1.2 | ${\color{red}High}$<br>7.5 |
| **Graphite** | ${\color{green}Very\ high}$<br>40.2 | ${\color{yellow}Mid}$<br>45.1 | ${\color{yellow}Mid\ low}$<br>2.6 | ${\color{green}Very\ low}$<br>3.4 |
| **Rolly** | ${\color{yellow}Mid\ low}$<br>32.1 | ${\color{green}High}$<br>49 | ${\color{yellow}Mid}$<br>3.5 | ${\color{yellow}Mid}$<br>high\ 6.9 |
| **Inrolly** | ${\color{red}Low}$<br>26.7 | ${\color{green}Maximal}$<br>52.3 | ${\color{yellow}Mid}$<br>3.8 | ${\color{red}High}$<br>8.2 |
| **Seht Drai** | ${\color{red}Minimal}$<br>22 | ${\color{green}High}$<br>48.4 | ${\color{green}Maximal}$<br>10.6 | ${\color{red}Very\ high}$<br>10.6 |

We can identify some patterns from the table:

- **Lower alternation leads to higher rolling, but also higher redirects.** In fact, there is a huge difference in total rolling (i.e. 2rolls + 3rolls) between a max alternation layout like Poqtea (36.5% total rolls) vs Seht Drai (59% total rolls).

- **Conversely, higher alternation leads to lower rolling, and lower redirects.** However, Poqtea (`T` + vowels setup) is an exception, as it has high redirects despite the high alternation. In all other cases, high alternation will lead to lower redirects.

In any case, the takeaway is that no keyboard layout can fully optimize all the stats, as maximizing one stat will necessarily make other stats worse. So, all layouts will have their pros and cons.

## 8.3. Balancing alternation & rolling

Which to favor between rolling and alternation is subjective. It can be said that **alternation offers a more consistent typing experience, as it feels rhythmic and minimizes awkward sequences. Meanwhile, rolling has higher highs** (words that feel very smooth) but lower lows (long same hand sequences). Regardless, it is not a matter of one or the other. Think of it more as a scale, with max alternation on one end and max rolling on the other. We have to decide where on that scale we want our layout to be.

## 8.4. Which consonants lead to higher or lower rolling

Most layouts place all the vowels on one hand. Doing so leads to a healthy amount of alternation, which ensures there are fewer long same hand sequences and redirects.

Even if we know where the vowels will be, we still have to decide what consonants we want to place on the vowel side. To help us with that we will use the table below, which shows how much each consonant combines with the vowels vs with the consonants. For example, we can see that `R` + vowels amount to 8.588% of all bigrams, while `R` + consonants is 3.343%. The table is sorted based on the third column (vowel column minus consonant column). Additionally, the main consonants (i.e. `T`, `N`, `S`, `R` and `H`) are highlighted, as their placement will have the most effect on a layout’s stats. Repeat bigrams are omitted.

|       | Vowel      | Cons       | V-C         |
| ----- | ---------- | ---------- | ----------- |
| **r** | **8.588%** | **3.343%** |  **5.245%** |
| **n** | **9.831%** | **5.202%** |  **4.628%** |
|   m   |   3.963%   |   0.828%   |    3.134%   |
|   l   |   5.049%   |   2.415%   |    2.634%   |
|   v   |   2.596%   |   0.131%   |    2.465%   |
| **s** | **5.910%** | **3.723%** |  **2.188%** |
|   f   |   2.620%   |   0.557%   |    2.062%   |
|   w   |   2.693%   |   1.045%   |    1.648%   |
|   c   |   3.132%   |   1.647%   |    1.485%   |
|   b   |   1.959%   |   0.649%   |    1.310%   |
|   d   |   3.365%   |   2.568%   |    0.797%   |
|   p   |   1.859%   |   1.108%   |    0.750%   |
|   k   |   1.133%   |   0.807%   |    0.326%   |
|   j   |   0.225%   |   0.024%   |    0.201%   |
|   z   |   0.160%   |   0.019%   |    0.141%   |
|   x   |   0.227%   |   0.096%   |    0.131%   |
|   q   |   0.121%   |   0.016%   |    0.105%   |
|   y   |   2.005%   |   1.965%   |    0.040%   |
| **h** | **6.136%** | **6.141%** |   -0.005%   |
| **t** | **7.719%** | **7.757%** |   -0.039%   |
|   g   |   1.776%   |   2.138%   |   -0.362%   |

*table data: monkeyracer

Generally, the consonants at the top on the table (e.g. `R` and `N`) will increase rolling the most when placed on the same hand as the vowels. Conversely, the letters at the bottom (e.g. `H` and `T`) will favor alternation instead. While this holds mostly true, it is only a generalization. To get a more accurate picture we need to look at trigrams. That is done on the next page.

## 8.5. Common trigrams, rolls & alternation

In order to get a deeper understanding of where a layout’s stats are coming from, we can look at the most common trigrams for a given letter, and check how those trigrams would be typed depending if said letter was on the vowel or the consonant hand. Below are some conclusions we can extract after doing that for the main consonants:

<table><tr>
<th><a href="https://github.com/rdavison/graphite-layout">Graphite</a> (StronglyTyped)</th>
<th>Inrolly (Ec0vid)</th>
<th>Poqtea (Ian Douglas)</th>
</tr><tr>
<td><pre>
b l d w z  ' f o u j ;
n r t s g  y h a e i ,
q x m c v  k p . - /
</pre></td><td><pre>
y o u q x  k d l w ,  
i a e n j  v h t s c '
 " - r b z  f p m g .
</pre></td><td><pre>
y w f l m  k p o q - /
u r s n h  d t e a i '
z x c v j  b g , . ;
</pre></td>
</tr></table>

<ul>
<li>
<p><strong><code>H</code> gives decent rolling regardless if we place it on the vowel hand or not.</strong> To understand why this is the case, we will use the following trigrams: <code>THE</code>, <code>THA</code> & <code>THI</code>.</p>
<p>On the Graphite layout (<code>H</code> on the vowel hand) <code>T-HE</code>, <code>T-HA</code> and <code>T-HI</code> are typed by pressing one key with one hand, and two with the other. Same applies to Inrolly (<code>H</code> on the consonant hand) only that the trigrams are now type as <code>TH-E</code>, <code>TH-A</code> and <code>TH-I</code>. So, they are rolls either way, it is just that the part that is a roll changes.</p>
</li><li>
<p><strong><code>T</code> maximizes alternation on the vowel hand.</strong> This is because the very common <code>T-H-E</code>, <code>T-H-A</code> and <code>T-H-I</code> trigrams are now alternates (i.e. they are typed by pressing only one key at a time, then changing hands). See Poqtea for a layout example. Anyway, <strong>if we want good rolling, <code>T</code> should always stay on the consonant hand.</strong></p>
</li><li>
<p><strong><code>R</code> and <code>N</code> maximize rolling on the vowel hand.</strong> <code>A</code> good example of this is Inrolly, which has tons of rolls. We have the frequent <code>N</code> + vowels rolls (<code>IN</code>, <code>AN</code>, <code>ON</code>, <code>EN</code>...), the <code>R</code> + vowel rolls (<code>ER</code>, <code>RE</code>, <code>OR</code>, <code>AR</code>...), some common 3rolls (<code>YOU</code>, <code>OUR</code>, <code>ION</code>, <code>REA</code>...) plus all the consonant rolls (<code>TH</code>, <code>ST</code>, <code>CH</code>, <code>CT</code>, <code>WH</code>, <code>TS</code>, <code>SH</code>, <code>LD</code>...).</p>
</li>
</ul>

If we want, we could check less frequent letters as well. For example, `D` and `G` favor rolling on the consonant side because the common `A-ND` and `I-NG` trigrams are rolls. However, on the vowel side `D` and `G` now favor alternation, as `A-N-D` and `I-N-G` become alternates.

## 8.6. Roll comfort

The following are the main factors affecting how comfortable a roll will be:

- Ideally, we want the two keys in the bigram to share the same row.
- When the keys are either one or two rows apart, it is preferable for the longer fingers to the higher one (e.g. it is more comfortable for the middle finger to be higher than the index, ring or pinky, rather than the other way around).
- Rolls that do not involve any lateral stretch motion (resulting from pressing two keys that are far apart) are more comfortable than those that do.
- Rolls that are typed with strong fingers (index and middle) are generally considered better than rolls that involve weaker fingers (ring and pinky).
- Some people prefer rolls that are on adjacent fingers. The adjacent finger pairings are: pinky - ring, ring - middle and middle - index. Meanwhile, the non adjacent finger pairings are: pinky - middle, ring - index and pinky - index.
- Finally, some people like taking roll direction into account as well. For example a middle - index finger roll can be either inwards (Qwerty `DF`) or outwards (Qwerty `FD`). There are layouts designed to favor inward rolls.

So, **not all the rolls in a layout will necessarily be comfortable.** After all, the basic roll definition (a trigram where we press two keys with one hand, and a third key with the other) is rather general, and can include bigrams such as scissors, lateral stretches, etc...

## 8.7. Which consonants lead to higher or lower redirects

**The first rule for minimizing redirects is having all vowels on the same hand.** This is because vowels on one side ensures alternation, which reduces redirects.

Next, **we want to identify which consonants roll in a single direction with the vowels,** as that too will minimize redirects. After all, redirects are a change in direction.

The table below shows how much each consonant favors one direction vs the other (i.e. consonant -> vowel vs vowel -> consonant). Letters that score high in one direction but low on the other appear higher on the table, indicating that they are more unidirectional. Lastly, the fourth column shows the ratio in which each consonant favors its preferred direction:


| Cons  | C -> V     | V -> C     | Direction      | Ratio     |
| ----- | ---------- | ---------- | -------------- | --------- |
| **h** | **6.064%** | **0.072%** | **H -> Vowel** | **84.41** |
|   j   |   0.213%   |   0.013%   |   J -> Vowel   |   16.78   |
| **n** | **2.057%** | **7.774%** | **Vowel -> N** | **3.78** |
|   b   |   1.535%   |   0.425%   |   B -> Vowel   |   3.61   |
|   q   |   0.092%   |   0.028%   |   Q -> Vowel   |   3.28   |
|   x   |   0.057%   |   0.170%   |   Vowel -> X   |   2.96   |
|   w   |   1.916%   |   0.777%   |   W -> Vowel   |   2.46   |
|   y   |   1.276%   |   0.729%   |   Y -> Vowel   |   1.75   |
| **s** | **2.230%** | **3.680%** | **Vowel -> S** | **1.65** |
|   p   |   1.117%   |   0.742%   |   P -> Vowel   |   1.51   |
| **r** | **3.568%** | **5.020%** | **Vowel -> R** | **1.41** |
|   m   |   2.301%   |   1.661%   |   M -> Vowel   |   1.39   |
|   c   |   1.809%   |   1.323%   |   C -> Vowel   |   1.37   |
|   g   |   1.013%   |   0.762%   |   G -> Vowel   |   1.33   |
|   v   |   1.464%   |   1.132%   |   V -> Vowel   |   1.29   |
|   k   |   0.636%   |   0.498%   |   K -> Vowel   |   1.28   |
| **t** | **3.495%** | **4.223%** | **Vowel -> T** | **1.21** |
|   d   |   1.619%   |   1.746%   |   Vowel -> D   |   1.08   |
|   z   |   0.079%   |   0.081%   |   Vowel -> Z   |   1.03   |
|   f   |   1.301%   |   1.319%   |   Vowel -> F   |   1.01   |
|   l   |   2.511%   |   2.537%   |   Vowel -> L   |   1.01   |

* table data: monkeyracer

We can see that **any layout that aims to minimize redirects will place the letter `H` with the vowels,** as `H` only combines with them in a single direction (ratio of 83 to 1!). On the other side of the spectrum, **placing `R` or `T` with the vowels will noticeably increase redirects,** as they combine with the vowels in both directions about equally.

## 8.8. Common trigrams & redirects 

As a general rule, redirects are the result of increasing rolling in a layout. The following are the main letter patterns that will lead to redirects:

<table><tr>
<th>Rolly (Ec0vid)</th>
<th>Inrolly (Ec0vid)</th>
</tr><tr>
<td><pre>
y o u f j  q m w l ,
i a e n b  k t s r c '
 ; " h p z  v d g x .
</pre></td><td><pre>
y o u q x  k d l w ,  
i a e n j  v h t s c '
 " - r b z  f p m g .
</pre></td>
</tr></table>

- **Vowel -> consonant -> vowel trigrams.** These will inevitably be redirects when all three letters are on the same hand. For example, `ERE`, `ONE` & `ARE` on Inrolly.
- **Consonant -> vowel -> consonant trigrams.** These would also be redirects if the three letters share one side. For example, `HIN`, `HEN` & `HAN` on Rolly.
- **Vowel -> vowel, followed or preceded by a consonant.** These are redirects or 3rolls depending on our vowel setup. For instance, on Inrolly, `EAR` & `AIN` are redirects, but `OUR`, `ION` & `REA` are 3rolls.
- **Consonant only trigrams.** These are redirects or 3rolls depending on our consonant setup. For example, `STR` on Rolly is a redirect.
- **Trigrams with punctuation.** For example, `T'S` is a redirect on either Rolly or Inrolly.

Ideally, we want all three keys in a redirect to share the same row (e.g. `AIN` or `STR` or Rolly). However, in practice many redirects will have just two letters on the same row, while a third letter is on a different row (e.g. `ONE`, `HIN`, `HEN` or `HAN` on Rolly).

Another aspect that affects how a redirect will feel is if it has SFS or not. If it does, then the redirect is typed with just two fingers, as one finger is utilized twice (e.g. `HIN`, `HEN` or `HAN` on Rolly). If there is no SFS, then three fingers will be used (e.g. `AIN`, `ONE` or `STR` on Rolly).

## 8.9. "Weak" redirects

**Redirects where the index finger is not utilized are sometimes referred to as "weak" or "bad" redirects, as they are trickier to type.** Having said that, people who have developed good finger independence and dexterity with their weaker fingers (from playing a musical instrument for example) will probably not mind "weak" redirects at all.

<table><tr>
<td>
<a href="https://github.com/samuelxyz/layouts#seht-drai">Seht Drai</a> (Tanamr)
<pre>
f u l v b  q g n o j
s e h t k  ' d r a i .
 ; m p w z  y c x / ,
</pre>
</td><td>
The <code>SHE</code> trigram is a weak redirect on Seht Drai, while <code>STE</code> is not. Similarly, <code>AIN</code> is a weak redirect, but not <code>DON</code>.
</td>
</tr></table>

Most trigrams in the English language (and therefore most redirects) involve both vowels and consonants. Conversely, vowel only trigrams are extremely rare. So, **in order to minimize weak redirects, we must place all the vowels on the same hand and on our last three fingers specifically** (pinky, ring and middle). As such:

<table><tr>
<td>
Whix (Ec0vid)
<pre>
f l n d k  ' w o u j
s r h t v  y c a e i
 x b m z q  p g . " ,
</pre>
</td><td>
On the right hand, with consonants being on the index finger, and vowels on middle, ring and pinky, we ensure that any trigram with both vowels + consonants will involve the index.
</td>
</tr></table>

It should be noted that, although vowel only trigrams are rare in English, there are actually some common consonant only trigrams. Regardless, with the right letter arrangement we can avoid weak redirects on the consonant hand as well. For example, none of the redirects on Whix’s left hand (`STR`, `NDS`, `RST`, `NST`, `NTS`, `RTH`...) are weak redirects.

## 8.10. Common trigrams & 3rolls

**Layouts that aim to maximize 3rolls necessarily have to split the vowels, placing three vowels on one hand, and two on the other.** This is done so that the most common trigram in the English language (`THE`) can be a 3roll on one hand, while on the other hand we have some of the next most common trigrams as 3rolls too (`ING`, `AND`, `ION`...). An example of such a layout would be Seht Drai (angle modded) which maximizes 3rolls while also doing a great job at optimizing other layout stats like SFBs, SFSs, etc...

[Seht Drai](https://github.com/samuelxyz/layouts#seht-drai) (Tanamr)
```
f u l v b  q g n o j
s e h t k  ' d r a i .
 ; m p w z  y c x / ,
```

The following are the 3rolls on Seht Drai. For each hand, they are sorted based on frequency (on the TypeRacer corpus):

- Left hand: `THE`, `WHE`, `PLE`, `BLE`, `SEL`, `LES`, `TLE`...
- Right hand: `ING`, `AND`, `ION`, `IND`, `ANY`, `ON`', `ONG`, `ARD`, `ANG`, `ANC`, `ORD`...

Ideally, we want all the letters in a 3roll to be on the same row (e.g. `THE`, `ONG` or `ARD`). However, we can only have a few 3rolls like that in a layout. The best we can hope for most 3rolls is having two of the letters sharing a row. See all the remaining 3rolls on Seht Drai other than `PLE`, `ANY` and `ANC` (those three have each letter on a different row).

Anyway, **the disadvantage of utilizing a 3-2 vowel split is that alternation plummets,** meaning redirects and long same hand sequences will be way higher than on other layouts.
