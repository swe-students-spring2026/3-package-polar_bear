import re
import random

_WORD_REPLACEMENTS: dict[str, str] = {
    "hi": "hai",
    "love": "wuv",
    "small": "smol",
    "cute": "kawaii",
    "fluff": "floof",
    "little": "wittle",
    "what": "whawt",
    "stupid": "baka",
    "cat": "kitteh",
    "dog": "doggo",
    "you": "u",
    "senior": "senpai",  
    "adorable": "kawaii",
    "world": "warudo"
}

_PUNCT_SUFFIX_MAP: dict[str, list[str]] = {
    ".": [
        " uwu.",
        " owo.",
        " >w<.",
        " ^w^.",
        " nyaa~",
    ],
    "!": [
        " owo!",
        " >w<!",
        " ^_^!",
        " :3!",
        " nyaa!!",
    ],
    "?": [
        " owo?",
        " uwu?",
        " >_<?",
        " ;w;?",
        " nyaa??",
    ],
}


def _replace_word_match(match: re.Match[str]) -> str:
    word = match.group(0)
    replacement = _WORD_REPLACEMENTS[word.lower()]

    if word.isupper():
        return replacement.upper()
    if word[0].isupper():
        return replacement.capitalize()
    return replacement


def uwu_mutator(text: str, intensity: int = 1) -> str:
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__!r}.")
    if intensity not in (1, 2, 3):
        raise ValueError(f"intensity must be 1, 2, or 3; got {intensity!r}.")
    if not text.strip():
        return text

    result = text

    # intensity 1: basic uwu-style consonant swap
    result = re.sub(r"[rl]", "w", result)
    result = re.sub(r"[RL]", "W", result)

    if intensity >= 2:
        # whole-word replacements
        pattern = r"\b(" + "|".join(map(re.escape, _WORD_REPLACEMENTS.keys())) + r")\b"
        result = re.sub(pattern, _replace_word_match, result, flags=re.IGNORECASE)

        # add "ny" sound before vowels after n/N
        result = re.sub(r"n([aeiou])", r"ny\1", result)
        result = re.sub(r"N([aeiouAEIOU])", r"Ny\1", result)

    if intensity == 3:
        # add cute suffixes after sentence-ending punctuation
        result = re.sub(
            r"[.!?]",
            lambda m: random.choice(_PUNCT_SUFFIX_MAP[m.group()]),
            result,
        )

    return result