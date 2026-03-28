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

_COLOR_EMOJI_MAP: dict[str, list[str]] = {
    "multicolor": ["🌈", "✨", "🎉", "🦄"],
    "red": ["❤️", "🌹", "🍓", "🔥"],
    "blue": ["💙", "🫐", "🌊", "🌀"],
    "green": ["💚", "🌿", "🍀", "🐢"],
    "yellow": ["💛", "🌟", "🌼", "🍋"],
}

def emoji_mutator(text: str, color: str = "multicolor") -> str:
    if not isinstance(text, str): #if text is not a str
        raise TypeError(f"Expected str, got {type(text).__name__!r}.")
    
    if color in _COLOR_EMOJI_MAP: #if mood is invalid
        raise ValueError(f"color must be one of {_COLOR_EMOJI_MAP.keys()}; got {color!r}.")
    
    if not text.strip():
        return text

    emojis = _COLOR_EMOJI_MAP[color]
    words = text.split(" ")
    out = []
    added_color_emoji = False

    for word in words:
        out.append(word)

        # word replacement
        key = word.lower().strip(".,!?:")
        if key in _WORD_EMOJI_MAP:
            out.append(_WORD_EMOJI_MAP[key])

        # randomly inject color emoji
        if word and random.random() < 0.40:
            out.append(random.choice(emojis))
            added_color_emoji = True

    if not added_color_emoji:
        out.append(random.choice(emojis))

    return " ".join(out)