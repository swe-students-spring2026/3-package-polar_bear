# BS Generator

[![Test Package](https://github.com/swe-students-spring2026/3-package-polar_bear/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/swe-students-spring2026/3-package-polar_bear/actions/workflows/test.yml)

BS Generator is a lightweight Python package that transforms plain text into fun internet-style output.
It currently includes three mutators:

- `brain_rot_mutator`: adds slang-style punctuation replacements and optional intensity effects.
- `emotion_mutator`: changes punctuation with emotion modes and keyboard faces like `:)`, `:D`, `uwu`, and `(¬‿¬)`.
- `emoji_mutator`: injects word-based and color-themed emojis.
- `wingdings`: convert text into wingdings symbols

This project has no server, no database, and no required environment variables.

## Team

- [Harry](https://github.com/harrywzl)
- [Claire](https://github.com/clairewwwwww)
- [Frank](https://github.com/HandEater)
- [Angelina](https://github.com/Tangelinawu)
- [Howard](https://github.com/hewlett-packard-lovecraft)


## PyPI

Package page: https://pypi.org/project/bs-generator/

Note: If the package has not been published yet, this link may show "Not Found" until release.

## Installation

Install locally for development (editable install):

```bash
python -m pip install -e .
```

Or install dev dependencies with Pipenv:

```bash
pipenv install --dev
```
or 
```bash
pipenv run python
```

## API Usage (Import Into Your Own Code)

### 1) `brain_rot_mutator(text, intensity=1)`

Mutates punctuation and slang level in a sentence.

- `text (str)`: input sentence
- `intensity (int)`: must be `1`, `2`, or `3`

```python
from bs_generator import brain_rot_mutator

print(brain_rot_mutator("The tests are failing again.", intensity=1))
print(brain_rot_mutator("The tests are failing again.", intensity=2))
print(brain_rot_mutator("The tests are failing again.", intensity=3))
```

### 2) `emoji_mutator(text, color="multicolor")`

Adds mapped emojis (for words like hello/ok/yes) and random color-set emojis.

- `text (str)`: input sentence
- `color (str)`: one of `multicolor`, `red`, `blue`, `green`, `yellow`

```python
from bs_generator import emoji_mutator

print(emoji_mutator("hello yes ok", color="multicolor"))
print(emoji_mutator("hello yes ok", color="blue"))
```

### 3) `emotion_mutator(text, emotion="classic")`

Changes punctuation, applies emotion-based exclamation styles, and adds keyboard drawings.

- `text (str)`: input sentence
- `emotion (str)`: one of `classic`, `cute`, `happy`, `love`, `sleepy`, `shy`, `sad`, `funny`, `smug`


```python
from bs_generator.emotion import emotion_mutator

print(emotion_mutator("Wow! Really?", emotion="smug"))
print(emotion_mutator("Wow! Really?", emotion="funny"))
print(emotion_mutator("Wow! Really?", emotion="sleepy"))

```

### 4) `wingdingsify(input, only_alphanumeric=False)`

Change input text into wingdings symbols.

- `input`: Your input string.
- `only_alphanumeric`: Boolean. When true, will only convert alphanumeric characters into wingdings symbols.

``` python
from bs_generator.wingdings import wingdingsify

print(wingdingsify("Hello world!"))
print(wingdingsify("Hello world!", only_alphanumneric=True))
```

## Example Program (Uses All Functions)

Complete runnable example: [example.py](example.py)

Run it:

```bash
python example.py
```

## Run Instructions (Any Platform)

All commands below work in Git Bash, macOS/Linux Bash, and Windows CMD/PowerShell.

From the repository root:

```bash
python example.py
```

Interactive Python usage:

```bash
python
```
>>>

Then in the Python prompt:

```python
from bs_generator import brain_rot_mutator, emotion_mutator, emoji_mutator
brain_rot_mutator("your sentence here", intensity=3)
emotion_mutator("your sentence here!", emotion="cute")
emoji_mutator("your sentence here", color="green")
```

## Contributing

### Clone and Set Up Environment

```bash
git clone https://github.com/swe-students-spring2026/3-package-polar_bear.git
cd 3-package-polar_bear
pipenv install --dev
```

### Run Tests

With Pipenv:

```bash
pipenv run pytest tests/ -v
```

Without Pipenv:

```bash
python -m pip install pytest
python -m pytest tests/ -v
```

### Build Package

With Pipenv:

```bash
pipenv run python -m build
```

Without Pipenv:

```bash
python -m pip install build
python -m build
```

## Configuration, Environment Variables, and Data

- Environment variables: none required.
- Database: none used.
- Starter/imported data: not required.
- Secret config files (`.env` or similar): none required for this project.

Because no secrets are required, there is no `env.example` file needed for runtime.

## Additional Quick Commands

### Install For Importing In Another Project

If published on PyPI:

```bash
pip install bs-generator
```

Local editable install from source:

```bash
python -m pip install -e .
```

### Minimal Import Example

```python
from bs_generator import brain_rot_mutator, emotion_mutator, emoji_mutator

text = "Hello, can someone review this pull request?"
print(brain_rot_mutator(text, intensity=2))
print(emotion_mutator(text, emotion="smug"))
print(emoji_mutator(text, color="yellow"))
```

### Platform-Specific Run Notes

Git Bash / macOS / Linux:

```bash
python example.py
```

Windows CMD:

```bat
python example.py
```

Windows PowerShell:

```powershell
python example.py
```

## Requirement Coverage Checklist

- Plain-language description: included at top of this README.
- Latest workflow badge: included at top and linked to GitHub Actions workflow.
- PyPI link: included in the PyPI section.
- Function documentation with code examples: included for every public function.
- Link to complete example program: included as [example.py](example.py).
- Contributor setup/build/test instructions: included in Contributing section.
- Teammates linked to GitHub: included in Team section.
- Cross-platform run/config instructions: included in Run Instructions and Additional Quick Commands.
- Environment variables and starter data instructions: included in Configuration section.
- Secret files guidance: explicitly documented as not required for this project.

