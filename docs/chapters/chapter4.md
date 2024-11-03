---
layout: page
title: "Chapter 4"
---

# Chapter 4: SFBs, SFSs and distance (18 min)

## Same finger bigrams (SFBs)

**A SFB consists of pressing two keys in succession with the same finger.** For example, take the word `decade` on Qwerty. The line shows letters pressed by the left middle:

<div style="width: 100%; overflow: hidden;">
<div markdown='1' style="width: 100px; float: left;">

 ```
 ┌┬┬─┬┐
 decade
 ```

</div>
<div markdown='1'> 

So, this word contains three SFBs: `DE`, `EC` and `DE` again. This is an extreme example, as five out of six letters are typed with one finger!

**SFBs are dependent on which letters are sharing a column.** For example, Qwerty’s **EDC** column is very poor, as it leads to lots of SFBs.

</div>
</div>

As a reference, [Qwerty](https://en.wikipedia.org/wiki/QWERTY) has around 6% SFBs, [Dvorak](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout) 2.5% and [Colemak](https://en.wikipedia.org/wiki/Colemak) 1.5%. Modern layouts can go as low as 0.5%. It should be noted that these numbers can vary greatly depending on the analyzer and corpus being utilized. For example, Qwerty may receive 4.5% SFBs in a different analyzer. All that matters is how layouts perform in relation to one another. In that sense, Qwerty will always have high SFBs, regardless of the analyzer.

When we say that a layout has a certain SFB percent, we are assuming that the layout is being utilized with proper [touch typing](chapters/chapter1.md#touch-typing). Advanced Qwerty users often use personalized fingerings (e.g. they press the letter C with the index finger, rather than with the middle) in order to avoid SFBs like CE . This is referred to as “alt fingering” and will be explored later.

Aside from the overall SFB percentage, we should also pay attention to how the SFBs are being distributed across the fingers. Generally, **we will favor SFBs being on the index and the middle fingers, and avoid them on weak fingers like the pinkies.**

Another thing to keep in mind is that **lowering SFBs past a certain point will produce diminishing returns.** For instance, the layouts with the lowest SFBs also have the lowest home row use. Additionally, they have lower index finger usage. Finally, they often have higher pinky movement. So, we should not disregard other stats when optimizing SFBs.


## Calculating the distance between two keys

Let’s say we want to know the distance for Qwerty `RG` (we are using Qwerty as a method to refer to the different keys on the keyboard):

![*Qwerty RG distance*](../assets/qwerty rg distance.png)

We can obtain the length of the red line by using [Pythagoras' theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem). All we need to know is the vertical distance between the two keys (the green line) and the horizontal distance (the blue line).

**On a row stagger keyboard, the top row is horizontally shifted 0.25 units in relation to the home row, and the bottom row is shifted 0.5 units.** This makes the horizontal distance between the top row and bottom row to be 0.75 units. As for vertical distance, the top and the bottom row are each 1 unit away from the home row.

In our Qwerty `RG` example, the vertical distance is 1U and the horizontal distance is 1.25U (1U from `G` to `F`, and 0.25U from `F` to `R`). Knowing this, we can use Pythagoras to determine the distance between the two keys. We have to square both the horizontal and vertical distances, and then square root the sum:

<div math='1'>
c = \sqrt{a^2+ b^2} = \sqrt{1.25^2 + 1^2} = 1.60 U
</div>

`RG` is a 1.6U SFB

Another example, Qwerty `MY`. The vertical distance is 2U and the horizontal one 1.75U (1U from `M` to `N`, 0.5U from `N` to `H`, and 0.25U from `H` to `Y`). Thus:

<div math='1'>
\sqrt{1.75^2 + 2^2} = 2.66 U
</div>

`MY` is a 2.66U SFB

One final example, Qwerty `VT`. The vertical distance is 2U and the horizontal one 0.25U (from `V` to `G` it would be 0.5U, but then we subtract 0.25U going from `G` to `T`). Thus:

<div math='1'>
\sqrt{0.25^2 + 2^2} = 2.02 U
</div>

`VT` is a 2.02U SFB


## 1U and 2U SFB

Using the method explained above, we will now list the distance for the different SFBs. In this section we look at either 1U or 2U ones. In the following section we check the rest.

**If the two keys that form a SFB are on adjacent keys, then it will be around 1U.** In the image below, Qwerty `FG` is exactly 1U, `FR` is 1.03U, and `FV` is 1.12U:

![*Qwerty FG FR FV*](../assets/qwerty fg fr fv.png)

**If one of the keys is on the bottom row and the other on the top row, then the SFB will be around 2U.** In this case, our finger has to jump over the home row to go from one key to the other. Below, Qwerty `VT` & `NU` are 2.02U, while `VR` & `NY` are 2.14U:

![*Qwerty 2u distances*](../assets/qwerty 2u distance.png)

Naturally, **the SFBs we do have in a layout should mostly be 1U.** In other words, 2U SFBs should be reserved for rare bigrams only. The Qwerty layout clearly fails in this regard.

## Diagonals

Traditional keyboards are not symmetrical. For instance, the distance between the left index’s resting position (F) and its bottom diagonal (B) is larger than the distance to the top diagonal (T). Below, Qwerty FT is 1.25U, while FB is 1.8U:



On the right side it is the opposite. Now it is the top diagonal that is further away. Below, Qwerty JY is 1.6U, Qwerty JN is 1.12U:



So, from best to worst (i.e. from closest to furthest): Qwerty N → T → Y → B.

The absolute longest diagonals are Qwerty RB and MY which are 2.66U! There is also MH which is is 1.8U, and RG being is 1.6U:



Finally, when using angle mod fingering (Qwerty C being pressed with the index finger, rather than the middle), we add two other diagonals: Qwerty CT (2.36U) and CG (1.8U):



Anyway, the bigger the distance, the higher priority not to have that diagonal as a SFB in a layout.

## Same finger Skipgrams (SFSs)

A SFS consists of pressing two keys with the same finger, but separated by X letters. An example would be typing may on Qwerty (M and Y are both typed with the right index).

There are two aspects to SFSs: distance, and how many keys there are of separation. For example, the aforementioned M_Y SFS is 2.66U, and it is a skip-1-gram (i.e. in between M and Y, there is only one key, A, being pressed by a different finger).

The M_Y SFS is the worst of both worlds. Firstly, our right index finger must make a huge jump to go from M to Y. Secondly, this is done almost consecutively, as there is a single letter, A, of separation. Having more keys in between, before a particular finger is needed again, is better, as it gives our finger more time to go back to its resting position (J in this case). An ideal word would be one where each finger is only utilized once.

Qwerty is unfortunately full of words that are typed with just two fingers. For example, the word burn is typed by alternating both index fingers. In the image below, the orange line shows letters pressed by the left index. Yellow for right index:

So, this word contains two SFSs. Not only that, but the B_R SFS on the left index is 2.66U, and U_N on the right index is 2.02U. Try typing it.

Another example would be thought on Qwerty. Same color/finger pairings as above:

Here, T_G is a same finger skip-3-gram (i.e. there are three letters separating T and G). Therefore, that SFS will be barely noticeable, especially when compared to H_U, U_H or G_T, all of which are SF skip-1-grams. This time they are only 1U, though. Try typing it.

So, Qwerty performs terribly at SFSs. The benefit of optimizing SFSs is that each word will be spread across more fingers. Moreover, when we do have to use any particular finger almost consecutively, the distance between the two keys will be minimal.

## Distance on a layout

For the longest time, distance used to be measured as “distance off the home row”. In other words, it was assumed that pressing keys on the home row required no movement, while pressing keys outside the home row did. However, this is a great oversimplification. Take the word refer on Qwerty for example:

If you quickly type this word, you will find that pressing the second E requires no movement (despite E being on the top row) as our left middle finger was already over it. Meanwhile, even though F is on the home row, pressing it implicates moving our left index downward.

This goes to show that, to accurately measure the distance it will take to press a key, we need to keep track of which key that finger had pressed beforehand. This does not only apply within a given word, but also to the connections between words. For example, imagine typing the word when followed by you on Qwerty:

The yellow line shows letters pressed by the right index. The letter N in when is followed by a space, and right after our right index has to jump over the home row to press Y. Therefore, N_Y is an inter-word (i.e. in between words) SFS, while H_N or Y_U are intra-word (i.e. within a word) SFSs.

With all this in mind, the simplest way to measure how a layout performs at SFB distance is to scale each SFB by its distance. For example, if the frequency of a SFB is 0.4% and the distance is 1.2, we simply multiply 0.4 by 1.2. Then we do the same for all the remaining SFBs in the layout. Same applies to the SFSs, to get the SFS distance.

The method above keeps SFB and SFS distances as separate stats. A more elaborate approach is to combine both stats into one, but penalizing consecutive finger usage more than semi consecutive usage. For example, we could weight SFB distance by 1, SF skip-1-gram distance by 0.5, and then drop off exponentially (e.g. skip-2-grams by 0.25, skip-3-grams by 0.125). This allows us to account for all skipgrams (not just skip-1-grams).

Moreover, this later approach can be used to calculate the movement per finger. With “movement” being SFB + SFS distance. It will sometimes also be referred to as “finger speed”. Regardless, the purpose of finger speed is to, given a group of letters (3 letters on pinky, ring or middle, 6 on index) tell us how to arrange those letters so that SFB + SFS distance is minimized. The Genkey and Oxeylyzer analyzers calculate distance in this way.

## Decentivicing 2U SFBs and SFSs

As explained earlier, to calculate the distance between two keys we simply have to square both the horizontal and vertical distances, and then square root the sum. Doing that, Qwerty RT would be 1U, RG 1.6U, RV  2.02U and RB 2.66U:



However, in order to calculate the distance or movement per finger (i.e. “finger speed”) analyzers like de Genkey or Oxeylyzer will not square root the sum. Therefore, Qwerty RT would still be 1U, but RG would now be 2.56U, RV 4.56U and RB 7.06U!

The point of omitting the square root when measuring distance is to punish longer distances more severely (2U SFBs will now be punished 4 times as hard as a 1U). This results in the analyzer outputting layouts where most of the SFBs and SFSs are only 1U.

## Weights for each finger

On Genkey and Oxeylyzer, distance is weighted based on each finger's strength or dexterity level. The following are the default weights on Genkey (Oxeylyzer uses the same ones, although it does not allow us to customize them, while Genkey does):

Index:  5.5
Middle: 4.8
Ring:   3.6
Pinky:  1.5

Basically, the purpose of these weights is to establish that weaker fingers (e.g. pinky) can handle much less movement than stronger fingers (e.g. index). Using that information, the analyzer can then spread movement accordingly when making a layout.

## Distributing movement across the fingers

Even if we discard letter columns that perform poorly at SFB and SFS distance, the English language still offers a lot of flexibility regarding how to arrange the alphabet to construct keyboard layouts.

There is a key concept we need to be aware of when designing layouts. To explain it we will use an analogy. Think of a balloon full of air. If we press down on it, air will be displaced to other parts of the balloon. The same is true for finger movement in keyboard layouts. If we place little effort in one part of the layout, more effort will be displaced elsewhere.

To help us visualize this we will use a few layout examples. All of them will share the exact same right hand (the vowel hand). Then, we will use the remaining consonants to come up with different arrangements for the left hand. The point being that each consonant home row will distribute movement differently across the fingers.
Rsnt
x f h m z
r s n t v
q b l d k
Snht
v r l d z
s n h t k
q x m b f
Nstr
b f d l z
n s t r k
q v m h x
Srht
f l n d k
s r h t v
q x b m z
Vowel hand
' w o u j
y c a e i
p g . - ,

The following table shows the movement (according to Genkey when using the MonkeyType + TypeRacer corpus) of each finger on the consonant hand:



Pinky
Ring
Middle
Index
Top row pinky
Rsnt
0.16
1.89
8.94
11.07
0.1% (x)
Snht
0.67
3.92
5.78
11.33
1.1% (v)
Nstr
0.68
1.41
5.83
14.03
1.4% (b)
Srht
0.75
2.62
5.35
11.07
2% (f)


On Rsnt the ring and especially the pinky are very relaxed, yet center column use is low as well. The drawback is that the middle finger has to make up for it. By comparison, on Snht ring finger movement almost doubles and top row pinky use increases by 1%, but in return middle finger movement is much lower than before. Nstr purposely concentrates movement on the index finger, where the SFBs can be comfortably alt fingered. Lastly, Srht has the least overall movement, at the expense of top row pinky use being the highest.

4.10. Distance on Qwerty
q w e r t  y u i o p
a s d f g  h j k l ;
z x c v b  n m , . /

There are three fingers that have extremely high movement on Qwerty:

The left middle’s high distance is explained by the common ED and DE SFBs & SFSs, and even more so by EC and CE, as these last two are 2U.

On the left index, the letter R causes lots of SFBs: TR, RT, FR, also GR (1.6U) and BR (2.66U). There are plenty of SFSs as well: TR, FR, RT, BT and VR (the last two are 2U).

The right index does poorly at distance, as all its SFBs are 2U or more: UN, NY, UM, MU and MY. As for SFSs, the main ones are MN, HN and YU, all of which are 1U. However, there are 2U SFSs as well: UH, UN and NY.

Finally, although the right ring is not anywhere as bad as the prior three, it is poor nonetheless, as it has the common LO and OL (1U) SFBs and SFSs.

Anyway, the point is that Qwerty was not optimized with SFB and SFS distance in mind.

4.11. Examples of bad words on Qwerty

In the following sections we list words that are tricky to type as they involve Qwerty’s problematic fingers: left middle, left index, right index (and to a lesser extent right ring).

For each word example, colored lines will indicate the keys pressed by each finger. This aims to accomplish two things. Firstly, it allows us to easily visualize SFBs and SFSs, to ensure the concept is understood well. Secondly, it makes Qwerty’s flaws more apparent.

For example, take the word decided on Qwerty:

A single colored line points to most of the letters, indicating they are all pressed by the same finger. So, this is a heavy SFB word.

Now take the word amendment instead:

Here there are two lines, for two fingers. Furthermore, there is always a one letter gap before a finger is utilized again, indicating SFSs. So, this would be a heavy SFS word.

The color code for the different fingers is as follows:

- Yellow indicates keys pressed by the right index finger. So, in this example NUM would be a SF trigram (NU being 2U and UM 2.1U).
- Orange for the left index finger. So, B_R is a 2.66U SFS.
- Green for the left middle finger. E_E is a SFS followed by a SFB (ED).
- Blue for the right ring finger (does not appear in this example).
- Grey for the remaining fingers

If a finger only presses a single letter in a word, no line will be shown, as SFB and SFS distance for that finger would be zero. Furthermore, there won’t be a line either for SFSs deeper than a skip-3-gram (i.e. skip-4-grams, etc…) as they stop being relevant.

4.11.1. Heavy SFS words on Qwerty

Note: SFSs that involve pressing the same key twice require no movement, as our finger is already over said letter after the first press. An example of such a SFS would be E_E.

Words typed mostly by alternating two fingers:


































Words with all their SFSs on one finger:















4.11.2. Heavy SFB words on Qwerty


Word with high distance (SFBs and SFSs) on the right index finger:






















Word with high distance (SFBs and SFSs) on the left middle finger:
















