import re
import random

_PUNCT_MAP: dict[str, str] = {
    ".": " fr.",
    "!": " no cap!",
    "?": " huh?",
    ",": " lowkey,",
    ";": " bussin;",
    ":": " deadass:",
}

_SLANG_WORDS: list[str] = [
    "skibidi", "rizz", "sigma", "bussin", "slay",
    "no cap", "fr fr", "goated", "based", "sheesh", "67",
]


def brain_rot_mutator(text: str, intensity: int = 1) -> str:
    if not isinstance(text, str): #if text is not a str
        raise TypeError(f"Expected str, got {type(text).__name__!r}.")
    if intensity not in (1, 2, 3): #if intensity is not 1, 2, or 3
        raise ValueError(f"intensity must be 1, 2, or 3; got {intensity!r}.")
    if not text.strip():
        return text

    result = re.sub( # replaces punctuation with slang
        "[" + re.escape("".join(_PUNCT_MAP.keys())) + "]",
        lambda m: _PUNCT_MAP[m.group()],
        text,
    )

    if intensity >= 2: #randomly injects slang words for ge 2
        words = result.split(" ")
        out = []
        for i, word in enumerate(words):
            out.append(word)
            if word and i < len(words) - 1 and random.random() < 0.40:
                out.append(random.choice(_SLANG_WORDS))
        result = " ".join(out)

    if intensity == 3: #converts everything to ALL CAPS
        result = result.upper()

    return result