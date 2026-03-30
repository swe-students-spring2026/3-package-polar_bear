import random

_WORD_EMOJI_MAP: dict[str, str] = {
    "hello": "👋",
    "hi": "👋",
    "ok": "👌",
    "okay": "👌",
    "yes": "👍",
    "no": "❌",
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
    if not isinstance(text, str):  # if text is not a str
        raise TypeError(f"Expected str, got {type(text).__name__!r}.")

    if color not in _COLOR_EMOJI_MAP:  # if color is invalid
        raise ValueError(
            f"color must be multicolor, red, blue, green, or yellow; got {color}."
        )

    if not text.strip():
        return text

    emojis = _COLOR_EMOJI_MAP[color]
    words = text.split(" ")
    out = []
    added_color_emoji = False

    for word in words:
        # split punctuation
        stripped = word.rstrip(".,!?:")
        punctuation = word[len(stripped) :]

        key = stripped.lower()

        # add emoji based on word
        key = stripped.lower()
        if key in _WORD_EMOJI_MAP:
            new_word = f"{stripped} {_WORD_EMOJI_MAP[key]}{punctuation}"

        else:
            new_word = word
        out.append(new_word)

        # random emoji
        if random.random() < 0.40:
            out.append(random.choice(emojis))
            added_color_emoji = True

    if not added_color_emoji:
        out.append(random.choice(emojis))

    return " ".join(out)
