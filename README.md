# Learn

A collection of small Python programs for studying languages and practicing vocabulary.

The repository contains several interactive command-line tools for vocabulary testing, English irregular verbs, and Ancient Greek typing.

## Features

- 📚 **Vocabulary quizzes** using custom `.txt` word lists
- 🔀 **Randomized questions** so vocabulary is tested in a different order each time
- 📊 **Quiz results** including correct answers, mistakes, total questions, and time
- 🇬🇧 **English irregular verb practice** with:
  - Infinitive / base form
  - Past simple
  - Past participle
- 🇬🇷 **Ancient Greek typing** using a custom keyboard mapping
- 📝 **Word-list creation** through an interactive Python script
- 📖 Includes several vocabulary lists for different languages and school subjects

## Files

### `Overhoring.py`

A general vocabulary quiz program.

It can load one or more `.txt` vocabulary lists, combine them, randomize the questions, and test the user.

At the end of the quiz it displays:

- Number of correct answers
- Number of incorrect answers
- Number of questions
- Time taken
- A score out of 10
- The words that were answered incorrectly

### `Bijvoegen.py`

A simple tool for creating vocabulary files.

The program asks for the name of the file and then lets you enter vocabulary in the following format:

```text
foreign_word = Dutch_word
