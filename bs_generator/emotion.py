import random
import re
from typing import Optional

_DEFAULT_PUNCT_MAP: dict[str, str] = {
    ".": " fr.",
    "!": " no cap!",
    "?": " huh?",
    ",": " lowkey,",
    ";": " bussin;",
    ":": " deadass:",
}

_KEYBOARD_FACES: list[str] = [
    # classic
    ":)", ":D", ":P", ";)", ":3", "uwu", "owo", ">_<", "^_^", "-_-", "x_x",

    # cute
    "(｡•ᴗ•｡)", "(•◡•)", "(◕‿◕)", "(◍•ᴗ•◍)", "(｡◕‿◕｡)",

    # happy
    "(≧◡≦)", "(＾▽＾)", "(⌒▽⌒)", "(´｡• ω •｡`)", "(´▽`ʃ♡ƪ)",

    # love
    "(♡˙︶˙♡)", "(❤ω❤)", "(づ｡◕‿‿◕｡)づ", "(っ˘ω˘ς)", "(｡♥‿♥｡)",

    # sleepy
    "(－_－) zzZ", "(︶︹︺)", "(´-ω-`)", "(￣o￣) . z Z", "(＿ ＿*) Z z z",

    # shy
    "(〃▽〃)", "(*/ω＼)", "(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)", "(⁄ ⁄•⁄ω⁄•⁄ ⁄)", "(〃ω〃)",

    # sad
    "(｡•́︿•̀｡)", "(╥﹏╥)", "(っ˘̩╭╮˘̩)っ", "(ノ_<。)", "(T_T)",

    # funny
    "(☞ﾟヮﾟ)☞", "(づ￣ ³￣)づ", "(ง •̀_•́)ง", "(☞ ͡° ͜ʖ ͡°)☞", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",

    # smug
    "(¬‿¬)", "(￣︶￣)", "(ಡωಡ)", "( ͡° ͜ʖ ͡°)", "(￢‿￢ )",
]

_EMOTION_FACES: dict[str, list[str]] = {
    "classic": _KEYBOARD_FACES[0:11],
    "cute": _KEYBOARD_FACES[11:16],
    "happy": _KEYBOARD_FACES[16:21],
    "love": _KEYBOARD_FACES[21:26],
    "sleepy": _KEYBOARD_FACES[26:31],
    "shy": _KEYBOARD_FACES[31:36],
    "sad": _KEYBOARD_FACES[36:41],
    "funny": _KEYBOARD_FACES[41:46],
    "smug": _KEYBOARD_FACES[46:51],
}

_EMOTION_EXCLAMATIONS: dict[str, str] = {
    "classic": "!",
    "cute": "!!",
    "happy": "!!!",
    "love": "!!!",
    "sleepy": "...",
    "shy": "..",
    "sad": "...",
    "funny": "!!",
    "smug": "!",
}


def emotion_mutator(
    text: str,
    emotion: str = "classic",
    punctuation_map: Optional[dict[str, str]] = None,
) -> str:
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__!r}.")
    if not isinstance(emotion, str):
        raise TypeError(f"Expected str for emotion, got {type(emotion).__name__!r}.")

    emotion_key = emotion.lower()
    if emotion_key not in _EMOTION_FACES:
        valid = ", ".join(_EMOTION_FACES.keys())
        raise ValueError(f"emotion must be one of {valid}; got {emotion!r}.")

    if not text.strip():
        return text

    replacements = _DEFAULT_PUNCT_MAP if punctuation_map is None else punctuation_map
    if not isinstance(replacements, dict):
        raise TypeError("punctuation_map must be a dict[str, str].")

    for key, value in replacements.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("punctuation_map must be a dict[str, str].")
        if len(key) != 1:
            raise ValueError("Each punctuation_map key must be a single character.")

    result = re.sub(
        "[" + re.escape("".join(replacements.keys())) + "]",
        lambda m: replacements[m.group()],
        text,
    )

    exclamation_token = _EMOTION_EXCLAMATIONS[emotion_key]
    result = re.sub(r"!+", exclamation_token, result)

    words = result.split(" ")
    out = []
    added_face = False
    chance = 0.2 if emotion_key == "classic" else 0.4
    face_pool = _EMOTION_FACES[emotion_key]

    for i, word in enumerate(words):
        out.append(word)
        if word and i < len(words) - 1 and random.random() < chance:
            out.append(random.choice(face_pool))
            added_face = True

    if not added_face:
        out.append(random.choice(face_pool))

    return " ".join(out)
