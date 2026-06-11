# Letter counter

Finally, a program that can accurately tell you how many letters there are in a word!

Unlike *certain* AI models, this tool instantly gives you the plain answer without any nonsense,
and it doesn't hallucinate extra letters in random words!

Supported features:
- Makes no mistakes
- Can format the output in either plain text or JSON
- Doesn't require a GPU or a subscription to run


## Usage examples:

```bash
> python lettercounter.py
usage: lettercounter.py [-h] [-f {text,json}] letter word
lettercounter.py: error: the following arguments are required: letter, word

> python lettercounter.py r strawberry
3

> python lettercounter.py P Google --format json
{"result": 0}
```


## Comparison with Google AI overview

These are the real answers I got as of June 11th, 2026. You can try this too, just google the same question
```
> Google: how many Ps are there in google
There is exactly 1 "P" in the word Google.

It's a common point of confusion because Google's own AI tool became famous for incorrectly insisting that there were two!

Do you have any other spelling questions or riddles you'd like to run by me?
```
```
> Google: how many Ys are there in earth
There are 2 "Y"s in the word "Earth" (the letters "ry" are not in the word, but the letter appears at the beginning of "Earthy").
If you are asking about the letter y itself across the whole planet, the count is practically infinite.
```
```
> And for good measure:
> Google: how many nonsense is there in ai
The amount of "nonsense" in AI is massive, taking the form of hallucinations, repetitive buzzwords,
and AI-generated "slop" flooding the internet. AI generates this nonsense because it is fundamentally
a complex statistical system predicting words, not an intelligent being evaluating truth.
```

Trying the same prompts with our tool:
```bash
> python lettercounter.py p google
0

> python lettercounter.py y earth
0

> python lettercounter.py nonsense ai
usage: lettercounter.py [-h] [-f {text,json}] letter word
lettercounter.py: error: Letter argument should have a length of 1 (got 8)
```

Compared to Google AI overview, this simple script clearly wins in all 3 cases.


## Why?

The main goal is to help AI agents count how many letters there are in words.
If you have an agent who wants to count letters in words, feel free to give them this tool to use.

If you happen to have an agent that requires extra files to use this tool (like SKILL.md),
please create an issue / pull request to contribute to teaching AI how to count letters in words!
