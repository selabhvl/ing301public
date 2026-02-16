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

## Table of contents 

### Part 1: Working with integer numbers 

To warm up, we will start with some simple operations on integers.
By solving these exercises, you will get some practice in using basic control structure (conditionals, loops, (recursive) functions).
You may read [this part of the Python standard library documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) when needed.

- [Exercises](./ints/exercises.py)




