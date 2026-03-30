# BS Generator

### Gen-Z Text Chaos Package

**BS Generator** is a fun, developer friendly Python package that brings a little chaos and joy to your terminal. Whether you want to mangle a string into peak Gen-Z internet speak, filter text with emojis, or summon a random motivational quote, this package has you covered. No serious software here, just good vibes.

Give it a sentence and pick a mode. It gives you back terminal chaos.
 

## Team

- [Harry](https://github.com/harrywzl)
- [Claire](https://github.com/clairewwwwww)
- [Frank](https://github.com/HandEater)
- [Angelina](https://github.com/Tangelinawu)
- [Howard](https://github.com/hewlett-packard-lovecraft)




## Installation

Install from the local project folder:

```bash
python -m pip install -e .
```

Or use Pipenv:

```bash
pipenv install --dev
```

## Usage

Once you see >>> try the commands below.

### brain_rot_mutator(text, intensity=1)

Mutates punctuation and slang level in your sentence.

- text (str): input sentence to mutate
- intensity (int): mutation level, must be 1, 2, or 3

Place in any string and intensity.

```python
from bs_generator import brain_rot_mutator

print(brain_rot_mutator("The tests are failing again.", intensity=1))
print(brain_rot_mutator("The tests are failing again.", intensity=2))
print(brain_rot_mutator("The tests are failing again.", intensity=3))
```

### emoji_mutator(text, color="multicolor")

Adds word-mapped and random color-themed emojis.

- text (str): input sentence
- color (str): emoji palette, one of multicolor, red, blue, green, yellow

Place in any string and color.

```python
from bs_generator import emoji_mutator

print(emoji_mutator("hello yes ok", color="multicolor"))
print(emoji_mutator("hello yes ok", color="blue"))
```

To exit when done: >>> exit()

## Example Program

See example.py for a complete demo using all functions.

Run it with:

```bash
python example.py
```

## Contributing

### Setup

```bash
git clone <https://github.com/swe-students-spring20263-package-polar_bear.git>
cd 3-package-polar_bear
pipenv install --dev
```

### Running Tests

```bash
pipenv run pytest
```

If not using Pipenv:

```bash
python -m pip install pytest
python -m pytest -q
```

### Building the Package

```bash
pipenv run python -m build
```

## Configure, Environment Variables, and Data

- Run mode: No long-running server.
- Environment variables: None required.
- Database: None.
- Secrets / .env: Not required.

