# Python Programming Exercises

The goal of the course ING310 is to move beyond basic programming in Python to introduce some central
concepts in computer science and and software engineering that are essential in order to be able to 
understand and work within modern day software system projects. Hence, we assume basic programming 
and problem solving skills for this course. At the same time, we acknowledge the fact that programming 
and problem solving is craft that is practicted and obtained via training. Simply speaking:

> "The only way to get better at programming is programming"

This means, by trying to solve many programming exercises, you will over time get better at it. 
A single introductory programming course often does not yield the necessary "mendgetrening".
This part of the repository is therefore designed as a collection of "simple" programming exercises.


Doing these exercises is completely voluntary and we will not check your work.
We simply provide you with the exercises and some basic "check code".

## Structure and how to use

The exercises are roughly grouped by problem domains and ordered in increasingly degrees of complexity and difficulty.
Each section comes with a `exercises.py` file which contains _skeletons_ of function definitions.
Each function has a short comment explaining what is does, the function bodies are filled with a _placeholder_ code 
that produces an error when the function is called. Your task is to replace the placeholer with meaninful code 
such that the function does what it says. Some functions contain som additional references about background 
and may require some "googling".
Each section also has an accompanying `tests.py`. This file contains some pre-made "unit tests", which check
whether your function works correctly. You can use these to check your work.
For instance, running the "integer tests" is done by:

```shell
python training_exercises/ints/tests.py
```

which will output something like:

```
EEEEEEEEEEEEE
=======================
...
Ran 13 tests in 0.002s

FAILED (errors=13)
```

This signals that there were `13` test and none of them succeeded (because they all contain placeholder code).
When solving the individual problems, more and more of these tests will succeed.

## Some words on AI use 

Some may already have some sort of "AI coding assistant" installed in their IDE, others may be considering it.
Examples of such assistant are [GitHub Copilot](https://github.com/copilot), [Cursor](https://cursor.com/), [Claude Code](https://code.claude.com/docs/en/overview).

Those tools are rapidly changing how Software Engineers are working and they most likely will become a permanent 
part of the "tooling belt" of software engineers.
Advantages ascribed to these tools are increased productivity, however, it also looks like that they negatively
affect the cognitive side of coding, especially learning new technology or patterns.

Those who are interested, may have a look at [this paper from Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)

The short story is that, while practicing coding with these exercises, you shall turn off these assistants as they 
invite to take shortcuts. And taking such shortcuts unfortunately means that you will not learn anything.
Please try to solve these exercises on your own. If you get stuck, you may consult AI such as ChatGPT.
But, when doing so, try to ask for hints rather than the complete solution.

## Table of contents 

### Part 1: Working with integer numbers 

To warm up, we will start with some simple operations on integers.
By solving these exercises, you will get some practice in using basic control structure (conditionals, loops, (recursive) functions).
You may read [this part of the Python standard library documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) when needed.

- [Exercises](./ints/exercises.py)

### Part 2: Working with strings 

As the next step, we will explore the `str`(ing) type. A string is basically a sequence of characters. 
String value are enclosed in quotes (`'` or `"`). Then length of the string can be obtained by calling [`len()`](https://docs.python.org/3/library/functions.html#len).
The characters of the string are accessed by indices: `s[0]` is the first character, and `s[n - 1]` is the last character (if `n` is the length of the string).
Implementing basic string functionality will teach to work programmatically with sequences.
Quite a few of the functions in the string-exercise file can be solved by delegating to an already existing
string method in the standard library. It is generally advisable to use a standard library method when it 
exists but for learning purposes it may be worthwile to try to implement them from scratch.

- [Exercises](./strings/exercises.py)


### Part Bonus: Advent of Code 

[Advent of Code (AoC)](https://adventofcode.com/) is an advent calender consisting of programming exercises run 
every year by Eric Wastl. Participating in the advent of code is free, can be done anytime (even if it is not advent),
and only requires a GitHub account. 

The exercises are at times quite tricky but are very valuable and very satisfying once they are solved.
Here, I hvae taken out some exercises.

- [Exercises](./aod/exercises.py)



