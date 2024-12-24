# 5. Alt fingering, SFB collisions and sliding (6 min)

## 5.1. Alt fingering
${\color{#ED1B23}RG}$
**Using a finger other than the intended one to type a certain bigram, with the purpose of avoiding a is referred to alt fingering.** For example, if we use standard fingering on Qwerty, the ${color{#ED1B23}CE}$ and ${color{#ED1B23}EC}$ bigrams are 2U SFBs:

<img src="../assets/chapter5/qwerty ce.png" alt="*Qwerty ce*">

Instead, to remove the aforementioned SFBs we can alt finger ${color{#ED1B23}CE}$/${color{#ED1B23}EC}$ by pressing `C` with the index finger (rather than the middle). This is what many advanced Qwerty users do.

## 5.2. SFB collisions

**A collision refers to when alt fingering a SFB creates a new SFB.** For instance, with standard fingering, ${color{#870014}CT}$ is not a SFB on Qwerty. However, if we alt finger ${color{#ED1B23}EC}$ by pressing `C` with the index, then ${color{#870014}CT}$ does become a SFB specifically on the `ECT` trigram:

<img src="../assets/chapter5/qwerty ct.png" alt="*Qwerty ct*">

Ideally, we should aim to minimize SFB collisions, but they are sometimes unavoidable.

## 5.3. Designing a layout with alt fingering in mind

Although alt fingering can be used to circumvent some of the issues of poor layouts like Qwerty, we are mainly interested in using it to further improve well optimized layouts.

If we do not ever deviate from either standard fingering or angle mod, we can only minimize SFBs up to a certain point, as we are restricted by English’s bigram frequency. **In order to reduce SFBs further, we can purposely place a few SFBs in a location where they are comfortable to alt finger.** A layout that does this is [Noctum](https://oxey.dev/noctum/) which has three intended alt fingers: ${color{#21B04C}RK}$, ${color{#21B04C}RL}$ and ${color{#21B04C}LK}$. Note that below the layout has been angle modded:

<img src="../assets/chapter5/noctum alt.png" alt="*Noctum index alts*">

To alt finger ${color{#21B04C}RK}$ we press `R` with the middle finger, and `K` with the index. Since the ${color{#21B04C}RK}$ bigram is never preceded by one of the letters on the middle finger (i.e. trigrams like `DRK`, `TRK` or `MRK` are nonexistent in English) alt fingering ${color{#21B04C}RK}$ will not cause SFB collisions on Noctum. Similarly, the ${color{#21B04C}LK}$ alt finger (typed by pressing `L` with the middle finger and `K` with the index) is also free of SFB collisions.

The ${color{#21B04C}RL}$ alt finger (`R` with the index, `L` with the middle) does introduce a SFB collision in the word `WORLD`, as both `L` and `D` are pressed with the middle finger in this case. A possible solution would be to introduce yet another alt finger, and press the letter `D` with the ring finger in this specific case. Some people might argue that if to remove one SFB (${color{#21B04C}RL}$) we must perform two alt fingers (${color{#21B04C}RL}$ and `LD`), then it is preferable to just type the SFB normally.

## 5.4. Most comfortable alt fingers

It is generally agreed that **the best location to place a SFB that we intend to alt finger is the index finger. That way we can comfortably press one of the two index finger keys with the middle finger.** Furthermore, we will often use keys that are adjacent to one another for alt fingers. This is done so that, if the SFB is typed normally, it will only be 1U.

### 5.4.1. On row stagger

Standard keyboards are not symmetrical. Therefore, a bigram and its mirror (i.e. the same bigram but on the opposite hand) may vary in length. We will compare each alt finger to its mirror. The more comfortable of the two will be shown in ${color{#21B04C}green}$, the other in ${color{#FFF200}yellow}$.

<img src="../assets/chapter5/qwerty index alts.png" alt="*Qwerty index alts*">

Qwerty ${color{#21B04C}FR}$ (index -> middle) is an easy alt. This is because the stagger makes it so `R` is very close to the middle finger’s resting position (`D`). On the right hand, `K` is noticeably further away from `U`, making ${color{#FFF200}JU}$ a bigger jump for the middle finger.

Qwerty ${color{#21B04C}UH}$ (middle -> index) is very comfortable on the right hand. Its mirror (${color{#FFF200}RG}$) forces us to splay our fingers a bit more, as the keys are further apart. Having said that, ${color{#FFF200}RG}$ does require a smaller jump from the middle finger.

Qwerty ${color{#21B04C}RT}$ (middle -> index) is nicer than its mirror (${color{#FFF200}UY}$) simply because `T` is closer to the index finger’s resting position (`F`) than `Y` is to `J`. Same reasoning applies to Qwerty ${color{#21B04C}MN}$ being better than ${color{#FFF200}VB}$.

Qwerty ${color{#21B04C}DC}$ (middle -> index) is a possible alt finger if we use standard fingering. If we used angle mod instead, it wouldn’t be an alt finger, but `CV` would become one.

Qwerty ${color{#21B04C}FG}$ is identical to ${color{#21B04C}JH}$, and so are ${color{#21B04C}FV}$ and ${color{#21B04C}JN}$.

Anyway, if we have a common index finger SFB in our layout of choice, we can turn it into a comfortable alt finger by placing it in one of the lines above.

### 5.4.2. On matrix

**On matrix keyboards there are fewer comfortable alt fingers than on row stagger. This is because the row stagger happens to be useful for alt fingering in particular.**

For example, compare the "vertical alt fingers" on row stagger vs matrix:

<span>
	<img src="../assets/chapter5/rowstag vertical alts.png" alt="*Rowstag vertical alts*">
	<img src="../assets/chapter5/ortho vertical alts.png" alt="*Ortho vertical alts*">
</span>

The fact that on row stagger each row is a bit shifted to the side in relation to one another is what made the alt fingers above comfortable. It allowed us to use the middle finger to press one of the index finger keys without our fingers feeling cramped.

Furthermore, some of the center column diagonals (namely Qwerty `N` & `T`) are easier to press on row stagger, as they are closer to our index finger’s resting position. Therefore, alt fingers involving those keys work better on row stagger as well.

Anyway, the following alts remain basically the same regardless of the keyboard type:

<img src="../assets/chapter5/identical alts.png" alt="*Identical alts*">

## 5.5. Sliding

Similarly to alt fingering, sliding is an alternative method for typing SFBs. **It consists of sliding our finger downwards, going from the first key in the SFB to the second.** An example of a layout were people might use sliding is [Dvorak](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout):

<img src="../assets/chapter5/dvorak is ass.png" alt="*Sliding on every column on cons hand on Dovark*">

On the right hand, all the SFBs happen to go downwards as shown by the arrows. For example, the GH SFB only happens in the direction `G` -> `H`. To type it, we could press the letter `G` and then slide our index finger downwards to `H`. Whether someone prefers doing that or typing the SFB normally is a matter of personal preference.

**Note that sliding is intended only for certain key profiles.** (e.g. laptop keyboards) On keyboards with taller keycaps, sliding our finger over the gap between the two keys will not be comfortable.
