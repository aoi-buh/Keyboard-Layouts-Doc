# 6. Scissors (9 min)

## 6.1. Row skips vs scissors

**A row skip or row jump is any bigram where one finger reaches to the top row and another finger on that same hand contracts to hit the bottom row.** A popular layout that minimizes row skips is Mtgap:

[Mtgap](https://mathematicalmulticore.wordpress.com/the-keyboard-layout-project/) (Michael Dickens)
```
y p o u j  k d l c w
i n e a ,  m h t s r
q z ' . :  b f g v x
```

The issue with minimizing all up-down motions is that it limits layouts design significantly. Furthermore, not every up-down motion is equal. So, **rather than penalizing all up-down movements, the usual approach is to utilize the “scissor” concept which penalizes some up-down motions but not others.** The Canary layout was made with that mindset:

[Canary](https://github.com/Apsu/Canary#canary) (Eve)
```
w l y p k  z x o u ;
c r s t b  f n e i a '
 j v d g q  m h / , .
```

The difficulty with defining scissors is that, unlike row skips, they are intrinsically subjective as not everyone will agree on which up-down motions should be included or excluded. In any case, a definition is proposed below.

## 6.2. Full scissors bigrams (FSBs)

**A FSB is a bigram where:**
1. **The vertical separation between the keys is two rows.**
2. **The finger that prefers being higher is not.** This includes bigrams where the middle finger is lower than any other finger, and bigrams where the ring is lower than the pinky or the index.

To understand the suggested scissor definition we will use the following images. The ${\color{#ED161C}red}$ lines indicate scissors, while the ${\color{#2DCB70}green}$ lines are the preferred finger patterns.

Adjacent finger pairings.

<img src="../assets/chapter6/adjacent scissors.png" alt="*Adjacent scissors*">

Non adjacent finger pairings.

<img src="../assets/chapter6/non adjacent scissors.png" alt="*Non adjacent scissors*">

On the left hand, the ${\color{#ED161C}red}$ lines show bigrams where the longer finger is lower than the shorter one. On the right hand it is the opposite (the longer finger is now higher). If you try both, you will likely find the ${\color{#2DCB70}green}$ lines to be noticeably more comfortable to type.

Although accounting for finger length is important, we also have to consider the fact that our arms approach the keyboard at an angle. That is to say, our wrists are not at a 90º angle in relation to the keyboard, but closer to 70º. This naturally places the index finger a bit closer to the bottom row, and the pinky closer to the top row. Anyway, the preferred placements for each finger (in relation to the other finger in the bigram) will be:
- The index prefers being lower.
- The middle prefers being higher.
- The ring prefers being higher than index and pinky, but lower than the middle.
- The pinky prefers being lower than middle and ring, but higher than index.

## 6.3. Other potential scissors

One issue some people might have with the above scissor definition is that, for a given finger pairing (e.g. pinky-ring), only one of the two possible movements is counted as a scissor. For example, most people will agree that the ring finger being lower than the pinky is more uncomfortable than the other way around. Despite that, some will argue that the opposite movement (i.e. pinky bottom row - ring top row) should be penalized regardless.

The main up-down motions that could be added to the earlier scissor definition are bigrams where the pinky is lower than the ring, or the ring is lower than the middle:

<img src="../assets/chapter6/fake scissor 1.png" alt="*Fake scissor image 1*">

So, even though the longer finger is higher, one might choose to count those bigrams as scissors anyway. Note that when using traditional fingering on row stagger the above bigrams become more uncomfortable on the left hand because of the steep angle:

<img src="../assets/chapter6/fake scissor 2.png" alt="*Skill issue part 2*">

## 6.4. Scissor angle

The angle between the two keys has a significant impact on how a scissor will feel. For instance, the following are the middle-index scissors when using standard fingering on a row staggered keyboard (the letter `C` is pressed by the middle finger):

<img src="../assets/chapter6/scissor angle.png" alt="*Scissor angle*">

**Generally, steeper angles have a more distinct scissor feel, while shallower angles introduce a lateral stretch component.** For example, on Qwerty ${\color{#ED1A21}CR}$ the main issue is the up-down motion where our fingers almost cross each other. By comparison, on Qwerty ${\color{#ED1A21},Y}$ the lateral stretch becomes a more noticeable problem.

## 6.5. Adjacent vs non adjacent scissors

When making a layout, **we should aim to minimize adjacent finger scissors in particular as they are the most noticeable.** If possible we will reduce non adjacent scissors as well, but those are a lesser priority.

## 6.6. Full scissor skipgrams (FSSs)

The difference between a FSB and a FSS is that on the first the two keys forming the scissor are pressed consecutively, while on the later there is another key in between the two, pressed by a third finger. The fact that there is an in-between key that breaks the scissor means that FSSs are less noticeable than FSBs. Although high frequency FSSs should be avoided regardless (e.g. `L_V`).

## 6.7. Half scissors bigrams (HSBs)

A HSB is a bigram where:
1. The vertical separation between the keys is only one row.
2. The finger that prefers being higher is not. This includes bigrams where the middle finger is lower than any other finger, and bigrams where the ring is lower than the pinky or the index.

In other words, **the only difference between a full scissor and a half scissor is that the vertical separation between the two keys is cut in half.** Naturally, this makes half scissors much less problematic than full scissors, although they are still not ideal.

In the images below the ${\color{#ED1B23}red}$ lines indicate half scissors, while the ${\color{#2CC76E}green}$ lines are the preferred finger patterns.

Adjacent HSB:

<img src="../assets/chapter6/adjacent half scissors.png" alt="*Adjacent half scissors*">

Non adjacent HSB:

<img src="../assets/chapter6/non adjacent half scissors.png" alt="*Non adjacent half scissors*">

## 6.8. Half scissor skipgrams (HSSs)

The difference between a HSB and a HSS is that on the first the two keys forming the half scissor are pressed consecutively, while on the later there is another key in between the two, pressed by a third finger.

## 6.9. Keysolve analyzer

To obtain the scissor and half scissor stats for a given layout we can use [keysolve](https://clemenpine.github.io/keysolve-web/). The only difference between the scissor definition proposed in this document and the keysolve one is that keysolve counts all ring-middle bigrams as a scissor, independently of which of the two fingers is higher.

## 6.10. Minimizing scissors

### 6.10.1. Reducing bottom row use

A straightforward way of minimizing scissors is to **place only rare characters on the bottom row middle, ring and pinky keys.** A layout that does this is [Canary](https://github.com/Apsu/Canary#canary):

<img src="../assets/chapter6/canary bottom row.png" alt="Canary layout with red boxes on bottom row middle, ring and pinky keys.">

We can see that the keys inside the ${\color{#F1161A}red}$ blocks have low usage. On the left hand there are no scissors, as `Q`, `J` and `V` rarely combine with the letters on the top row. Same applies for punctuation on the right hand. **With this approach, the only part of the bottom row that is heavily utilized are the index finger keys.** Any layout that arranges the bottom row in this manner will perform well at scissors.

### 6.10.2. Strategically avoiding scissors

If we place common characters on the bottom row middle, ring or pinky keys, then we have to be careful as to not cause scissors. For example, take this layout:

<img src="../assets/chapter6/layout with lots of row jumps.png" alt="*Layout with lots of row jumps*">

There is a lot of up-down motion on the left hand: ${\color{#ED1B23}WH}$, ${\color{#ED1B23}BL}$, ${\color{#ED1B23}LD}$ and ${\color{#ED1B23}LK}$. Having said that, this can be easily solved by swapping which letters are on the top or bottom row:chapter

<img src="../assets/chapter6/layout with lots of row jumps fixed.png" alt="*Layout with lots of row jumps fixed*">

All the letters remain on the same fingers, yet the scissors have been greatly reduced. Point being, **with smart letter placings it is possible to have relatively low scissors despite having common letters on the bottom row non index keys.** Still, the layouts with the least scissors will often place only rare letters in those locations as seen earlier.

### 6.10.3. Common scissors in layouts

**On the vowel hand, scissors usually come from punctuation.** An extreme example are layouts which utilize the `YI OA UE` vowel block and then place punctuation right below it. For example, take Semimak:

<img src="../assets/chapter6/semimak scissors.png" alt="*Semimak punctuation scissors*">

So, when a letter on the top row is followed by a punctuation symbol, we get a scissor.

On the consonant hand, the letter that can lead to the most scissors is `L`. The reason for this is that `L` almost never goes on the home row, yet it combines with all the letters that are often relegated to the top or bottom row (`Y`, `D`, `P`, `B`, `C`, `F`, `G`...). So, when `L` is on the top/bottom row and any of the aforementioned letters is on the opposite row, we get a scissor. An extreme example would be Hands Down Neu:

<img src="../assets/chapter6/hands down neu lmfao.png" alt="*Hands down neu*">

Another letter that sometimes causes scissors is `M`. Thankfully, `M` only really causes scissors with `B` and `P` (`MB` and `MP` bigrams) making it much more flexible than the letter `L`.
