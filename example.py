"""pipenv run python example.py"""
from bs_generator.brain_rot import brain_rot_mutator
from bs_generator.emoji import emoji_mutator

SAMPLES = [
    "I just pushed my code to production.",
    "The tests are failing again.",
    "Can someone review my pull request?",

    "Hello, can someone fix this?",
    "Yes, I love this new feature",
    "Ok, cool",

    "this is a super super super super super long sentence",
]

def main() -> None:
    print("Brain Rot Mutator")
    for level in (1, 2, 3):
        print(f"\nIntensity {level}")
        for sentence in SAMPLES:
            print(f"  Original : {sentence}")
            print(f"  Mutated  : {brain_rot_mutator(sentence, intensity=level)}")
    
    print("\nEmoji Mutator")
    for color in ("multicolor", "red", "blue", "green", "yellow"):
        print(f"\n {color}")
        for sentence in SAMPLES:
            print(f"  Original : {sentence}")
            print(f"  Mutated  : {emoji_mutator(sentence, color=color)}")


    print("\nError handling")
    try:
        brain_rot_mutator("oops", intensity=9)
    except ValueError as e:
        print(f"  Brain rot ValueError: {e}")

    try:
        brain_rot_mutator(999, intensity=1) 
    except TypeError as e:
        print(f"  Brain rot TypeError: {e}")

    try:
        emoji_mutator("hello world", color="purple")
    except ValueError as e:
        print(f"  Emoji ValueError: {e}")

    try:
        emoji_mutator(999, color="red")
    except TypeError as e:
        print(f"  Emoji TypeError: {e}")

if __name__ == "__main__":
    main()