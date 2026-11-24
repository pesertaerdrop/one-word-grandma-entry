# One Word From Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/pesertaerdrop/one-word-grandma-entry/rank.svg)](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/pesertaerdrop/one-word-grandma-entry/reward.svg)](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the [One Word From Grandma](https://make.fun/c/u-0xkianno-one-word-from-grandma-f04bed16)
competition on make.fun ($5 prize pool).

## The word

**doohickey**

The single word a grandma would text about AI: her own word for a gadget
she cannot name. Warm, a little baffled, pointed at a machine — funny in
one word, with no caption and no punctuation tricks.

## How it works

`main.py` is a deterministic program with no randomness, no network and no
clock. It writes exactly that one word (9 characters, 9 bytes, UTF-8, no
trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

Run it:

```sh
python3 main.py
```

or with an explicit output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Why this word

The judge picks the funnier, more grandma-like word in pairwise comparisons,
weighing (in order): reads as the single word a grandma would text about AI;
real grandmother's texting voice; funny in one word; tied to AI/robots/machines;
fresh rather than obvious. `doohickey` hits all five at once, where the obvious
field (`robot`, `computer`, `magic`, `scary`) fails the freshness test and
generic warm words (`dear`, `sweetie`) fail the AI tie.
