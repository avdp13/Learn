# Learn

A collection of Python programs for studying languages and practicing
vocabulary.

This repository contains several small command-line programs that were
created to make language learning easier. The programs focus mainly on
vocabulary testing, creating vocabulary lists, practicing English
irregular verbs, and typing Ancient Greek.

The repository also contains vocabulary files that can be used with the
learning programs.

## Contents

- `Overhoring.py` - Vocabulary testing program
- `Bijvoegen.py` - Vocabulary file creation tool
- `Irregular verbs En.py` - English irregular verbs practice
- `OudGrieks typen.py` - Ancient Greek keyboard tool
- Several `.txt` files containing vocabulary

---

## Overhoring.py

`Overhoring.py` is the main vocabulary testing program in the
repository.

It is designed to turn vocabulary lists stored in `.txt` files into an
interactive test. Instead of studying the vocabulary in a fixed order,
the program can select and randomize vocabulary so that each test is
different.

### Selecting vocabulary

The program allows vocabulary files to be selected for the test. The
repository contains vocabulary lists for several languages and
subjects, including Latin, Ancient Greek, English, German, and Dutch.

Multiple vocabulary lists can be used together. This makes it possible
to create a larger test from several separate lists.

### Answering questions

During the test, the program presents a vocabulary item and asks the
user to provide its translation.

The program checks each answer and keeps track of the number of correct
and incorrect answers.

The vocabulary is randomized so that the same words do not always
appear in the same order.

### Results

After the test has finished, the program calculates the result and
shows information about the performance.

The incorrect answers are also recorded so that the user can see which
words were difficult.

This makes the program useful not only for testing knowledge, but also
for identifying vocabulary that requires additional practice.

### Vocabulary format

The vocabulary files use a dictionary-like text format.

For example:

```text
{"word": "translation", "another word": "another translation"}