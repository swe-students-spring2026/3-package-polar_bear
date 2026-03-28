import random

_WORD_EMOJI_MAP: dict[str, str] = {
    "hello": "👋",
    "hi": "👋",
    "ok": "👌",
    "okay": "👌",
    "yes": "👍",
    "no": "❌",
    "love": "❤️",
    "fire": "🔥",
    "cool": "😎",
}

_EMOJI_MAP: dict[str, list[str]] = {
    "happy": ["💛", "✨", "😊", "🌟"],
    "sad": ["😭", "💔", "😢", "🥲"],
    "angry": ["😡", "🔥", "🤬", "💢"],
    "silly": ["🥴", "🤪", "😵‍💫", "😖"],
}

def emoji_mutator(text: str, mood: str = "happy") -> str:
    if not isinstance(text, str): #if text is not a str
        raise TypeError(f"Expected str, got {type(text).__name__!r}.")
    
    if mood not in _EMOJI_MAP: #if mood is invalid
        raise ValueError(f"mood must be one of {_EMOJI_MAP.keys()}; got {mood!r}.")
    
    if not text.strip():
        return text

    emojis = _EMOJI_MAP[mood]
    words = text.split(" ")
    out = []

    for i, word in enumerate(words):
        out.append(word)

        # word replacement (hello -> 👋)
        key = word.lower().strip(".,!?:")
        if key in _WORD_EMOJI_MAP:
            out.append(_WORD_EMOJI_MAP[key])

        # randomly inject mood emoji
        if word and random.random() < 0.40:
            out.append(random.choice(emojis))

    result = " ".join(out)

    return result