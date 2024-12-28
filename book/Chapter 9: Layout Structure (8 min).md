
# **9. Layout structure (8 min)**

## 9.1. Letter stacks

One of the first steps when making a layout is deciding where the high frequency letters will be. These are `E`, `A`, `O`, `I` for the vowels and `T`, `N`, `S`, `R`, `H` for the consonants.

The aforementioned letters are the main ones competing for the 8 home row spots in a layout. **Since there are 9 high frequency letters for 8 home row spots, one of them will inevitably be pushed off the home row. The result is that there will always be at least 2 high frequency letters sharing a column/finger. This is referred to as a "stack".** The viable consonant stacks are `NH`, `RH` & `NR`, while the vowel stacks are `EO` & `AO`:

<table><tr>
<th markdwon=1>${\color{pink}1\ Consonant\ Stack:}$</th>
<th markdwon=1>${\color{pink}1\ Vowel\ Stack:}$</th>
</tr><tr>
<td>
<strong>Isrt</strong> (Whorf)
<pre>
y c l m k  z f u , '
i s r t g  p n e a o ;
 v w d j q  b h / . x
</pre></td><td>
<a href="https://github.com/rdavison/graphite-layout">Graphite</a> (StronglyTyped)
<pre>
b l d w z  ' f o u j ;
n r t s g  y h a e i ,
q x m c v  k p . - /
</pre></td>
</tr></table>

Despite not being that common, **the letter `C` plays a key role in layouts.** The unique thing about `C` is that it cannot share a column with `T`, `N`, `R` or `H` (high SFBs). Therefore, **on 1 stack layouts, `C` will always be on a `SC` column** (see the layouts above).

However, there are certain aspects of layout design (SFBs, for example) that can only be fully optimized **if we break the `SC` pair and give the letter `C` its own column. And for that, we need 2 stacks** (a consonant stack + a vowel stack):
2 stacks with `C` on index:

<table><tr>
<th markdwon=1>${\color{pink}2\ stacks\ with\ `C`\ on\ index:}$</th>
<th markdwon=1>${\color{pink}2\ stacks\ with\ `C`\ on\ pinky:}$</th>
</tr><tr>
<td>
<a href="https://o-x-e-y.github.io/layouts/sturdy/index.html">Sturdy</a> (Oxey)
<pre>
v m l c p  x f o u j
s t r d y  . n a e i
 k q g w z  b h ' ; ,
</pre></td><td>
<strong>Pine</strong> (ClemenPine)
<pre>
y l r m k  q f o u ,
c s n t g  b h a e i
j x z w v  p d ' / .
</pre></td>
</tr></table>

So, there are 4 main categories: 1 consonant stack, 1 vowel stack, and 2 stacks with either a `C` index or a `C` pinky. Layouts in the same category will share more similarities. In the next few pages, we go over the properties shared by layouts in each category.

## 9.2. One consonant stack

Layouts that have two of the top consonants on the same column (e.g. a `NH` column):

<table><tr>
<td>
<a href="https://colemakmods.github.io/mod-dh/">Colemak DH</a> (SteveP)
<pre>
q w f p b  j l u y ;
a r s t g  m n e i o '
 x c d v z  k h , . /
</pre></td>
<td>
<a href="https://github.com/DreymaR/BigBagKbdTrixPKL/tree/master/Layouts/Colemak/Cmk-Qmods#colemak-qix-by-nyfee-2021-03">Colemak Qi;x</a> (Nyfee)
<pre>
; l c m k  j f u y q
a r s t g  p n e i o '
 x w d v z  b h / . ,
</pre></td>
<td>
<strong>Isrt</strong> (Whorf)
<pre>
y c l m k  z f u , '
i s r t g  p n e a o ;
 v w d j q  b h / . x
</pre></td>
</tr></table>

**These layouts have the highest home row use, as the letter `O` (the 4th most common English letter) is on the home row.** To make room for `O`, `H` is pushed off the home row.

Since one of the main vowels (usually `A` or `I`) is moved to the consonant hand, alternation will noticeably decrease. Consequently, rolls, and especially redirects, will increase.

## 9.3. One vowel stack

Layouts that have two of the top vowels on the same column (e.g. an `AO` or `EO` column):

<table><tr>
<td>
<a href="https://github.com/GalileoBlues/Gallium">Gallium</a> (Brys)
<pre>
b l d c v  z y o u ,
n r t s g  p h a e i
q x m w j  k f ' ; .
</pre></td><td>
<a href="https://github.com/Apsu/APT#aptv3-layout">APT</a> (Eve)
<pre>
w g d f b  q l u o y
r s t h k  j n e a i ;
X c m p v  z , . ' /
</pre></td><td>
<a href="https://github.com/samuelxyz/layouts#rollla">Rollla</a> (Tanamr & Heart)
<pre>
y o u b .  x k c l v
i a e n ,  m h s r t
 ' / p w z  f d g j q
</pre></td>
</tr></table>

**The letter `O` is now relegated to the top row,** (despite in some corpus `O` is more frequent than `A` it is still desirable to have `O` on the top row for the `OU` same row) with `H` taking the home row spot. Therefore, **home row use will be a bit lower,** as `H` is less common than `O`.

A fundamental difference between the previous subgroup and this one is that **here the vowels take just three home row spots, rather than four.** This allows us to have all vowels on one side, while still being able to fit consonants on that same hand. This way we can have good rolling (from consonants + vowels) and low redirects (from one side vowels).

## 9.4. Two stacks (1 vowel + 1 consonant)

Layouts that have a vowel stack (`EO` or `AO`) and a consonant stack (`HN`, `RN` or `HR`). **Double stack layouts have the lowest home row use. Despite that, they offer multiple benefits in return.** We can subdivide this group into two based on the location of the letter `C`.

### 9.4.1. With C on index

`C` and `D` cause negligible SFBs & SFSs with plenty of moderately common letters. We can take advantage of this by placing `C` / `D` on an index finger with five other letters:

<table><tr>
<td>
<a href="https://o-x-e-y.github.io/layouts/sturdy/index.html">Sturdy</a> (Oxey)
<pre>
v m l c p  x f o u j
s t r d y  . n a e i
 k q g w z  b h ' ; ,
</pre></td><td>
<a href="https://github.com/samuelxyz/layouts#seht-drai">Seht Drai</a> (Tanamr)
<pre>
f u l v b  q g n o j
s e h t k  ' d r a i .
 ; m p w z  y c x / ,
</pre></td><td>
<a href="https://o-x-e-y.github.io/layouts/noctum/index.html">Noctum</a> (Oxey)
<pre>
b f d l z  j g o u ,
n s t r k  y c a e i
 v m h x q  p w ' ; .
</pre></td>
</tr></table>

**Double stack layouts with a `C` index have the least SFBs and SFSs.** The table below lists multiple `C` index arrangements and gives a layout example for each:

<table><tr>
<td><table><tr>
<th><strong>With <code>D</code>:</strong></th>
<th><strong>Without <code>D</code>:</strong></th>
</tr><tr>
<td><table>
<tr><td>
<strong>DC WGP</strong><br>Semimak
</td></tr><tr><td>
<strong>DCYWG</strong><br>Gemini
</td></tr><tr><td>
<strong>DC WGP   '</strong><br>Semimak JQ
</td></tr><tr><td>
<strong>DCY G    '</strong><br>Seht Drai
</td></tr><tr><td>
<strong>DC WG  MV</strong><br>Trance
</td></tr><tr><td>
<strong>DC W PB  '</strong><br>Trendy
</td></tr><tr><td>
<strong>DCYWGP</strong><br>Sturdy
</td></tr>
</table></td>
<td><table>
<tr><td>
<strong>CYWG    F'</strong><br>Dina
</td></tr><tr><td>
<strong>C WGPV   '</strong><br>Rainy
</td></tr><tr><td>
<strong>CYWGP    '</strong><br>Whix
</td></tr><tr><td>
<strong>C WGPV B</strong><br>Recurva
</td></tr><tr><td>
<strong>CYWG  M</strong><br>Stronk
</td></tr><tr><td>
<strong>C WG VMB</strong><br>Snug
</td></tr><tr><td>
<strong>CYWGPV</strong><br>Whorf
</td></tr>
</table></td>
</tr></table></td><td><br>For an easier comparison, letters that appear on multiple rows of the table are kept on the same vertically line.

For example, the indexes on Semimak and Gemini share `D`, `C`, `W` & `G`, but differ on `Y` & `P`.

**The letters that can be paired with `C` / `D` while causing few SFBs are `Y`, `M`, `W`, `F`, `G`, `P`, `B` & `V`.**

</td></tr></table>

### 9.4.2. With C on pinky

One drawback with the layouts in the previous section is that `C` being on the index finger leads to low index usage (11 - 14%). If this is an issue, the letter `C` can be moved to the pinky instead:

<table><tr>
<td>
<a href="https://github.com/Apsu/Canary#canary">Canary</a> (Eve)
<pre>
w l y p k  z x o u ;
c r s t b  f n e i a '
 j v d g q  m h / , .
</pre></td><td>
<strong>Pine</strong> (ClemenPine)
<pre>
y l r m k  q f o u ,
c s n t g  b h a e i
j x z w v  p d ' / .
</pre></td><td>
<a href="https://engram.dev/">Engram</a> (Arno Klein)
<pre>
b y o u '  " l d w v z
c i e a ,  . h t s n q
g x j k -  ? r m f p
</pre></td>
</tr></table>

Compared to `C` index layouts, **moving `C` to the pinky sacrifices some SFB and SFS optimization, in favor of more traditional indexes with higher usage.**

The table below lists examples of `C` pinky setups and gives a layout example for each:

<table>
<tr><td>
<strong>WC</strong><br>Canary
</td></tr><tr><td>
<strong>YC</strong><br>Pine
</td></tr><tr><td>
<strong>WC'</strong><br>Crest
</td></tr><tr><td>
<strong>,C.'</strong><br>Rolly
</td></tr><tr><td>
<strong>WCG'</strong><br>Saiga
</td></tr><tr><td>
<strong>BCG</strong><br>Engram
</td></tr>
</table><br>

## 9.5. Summary table

The table below summarizes the characteristics of the different layout categories. To see the pros and cons of a particular category, go through a row of the table. To compare how the different categories perform on a particular aspect, check a column instead:

||Home row<br>use|SFBs|SFSs|Redirects|Index<br>use|Pinky<br>use|Usual vowel<br>hand split|
|-|-|-|-|-|-|-|-|
|**1 consonant stack**<br>(e.g. NH)|${\color{green}High}$|${\color{yellow}Mid}$|${\color{yellow}Mid}$|${\color{red}High}$|${\color{green}High}$|${\color{yellow}Mid}$|4 - 1|
|**1 vowel stack**<br>(e.g. AO or EO)|${\color{yellow}Mid}$|${\color{yellow}Mid}$|${\color{green}Low}$|${\color{yellow}Variable}$|${\color{red}Low}$|${\color{yellow}Mid}$|5 - 0|
|**2 stacks with<br>C on index**|${\color{red}Low}$|${\color{green}Low}$|${\color{green}Low}$|${\color{yellow}Variable}$|${\color{red}Low}$|${\color{yellow}Mid}$|5 - 0|
|**2 stacks with<br>C on pinky**|${\color{red}Low}$|${\color{yellow}Mid}$|${\color{green}Low}$|${\color{yellow}Variable}$|${\color{green}High}$|${\color{red}Low}$|5 - 0||

\* It is possible to get "low SFBs" with any of the categories. The reason only the third appears as ${\color{green}Low}$, is simply to highlight that it can optimize SFBs further than the others.

\* The word ${\color{yellow}Variable}$ refers to the redirects being dependent on what consonants are with the vowels. For example, `H` + vowels has low redirects, but `NR` + vowels has high redirects.

We can identify some patterns from the table:

- **Low index finger use correlates with lower SFBs.** Reaching the lowest SFBs requires using a `C` index, and those indexes have low use. Having said that, there are layouts that manage to get quite low SFBs while maintaining high index finger use.
- **Low index finger use also correlates with lower SFSs.** The reason for this is straightforward. Since index fingers have six keys assigned to them, there are many more letter interactions on the indexes, all of which can cause SFSs. The purpose of SFS optimization is for each word to be spread across more fingers. Naturally, this means concentrating fewer common letters on any particular finger.
- **Minimal SFSs requires a vowel stack (an `AO` column specifically).** This is why 1 consonant stack layouts can not reduce SFSs past a certain point. We will elaborate on this in the next chapter.
