"""pipenv run python example.py"""
from bs_generator.brain_rot import brain_rot_mutator
from bs_generator.emotion import emotion_mutator
from bs_generator.emoji import emoji_mutator

SAMPLES = [
    "I just pushed my code to production.",
    "The tests are failing again.",
    "Can someone review my pull request?",
    "Hello, can someone fix this?",
    "Yes, I love this new feature",
    "Ok, cool",
    "Yippe blue is a pretty color",
    "Flying chickens are the best",
    "I can't believe this is happening",
    "this is a super super super super super long sentence",
]

def main() -> None:
    for sentence in SAMPLES:

        print(f"Original: {sentence}")

        print("\nEmotion Mutator")
        for emotion in ("classic", "cute", "happy", "love", "sleepy", "shy", "sad", "funny", "smug"):
            print(f"    Emotion {emotion}: {emotion_mutator(sentence, emotion=emotion)}")
    
        print("\nBrain Rot Mutator")
        for level in (1, 2, 3):
            print(f"    Intensity {level}: {brain_rot_mutator(sentence, intensity=level)}")
                      
        print("\nEmoji Mutator")
        for color in ("multicolor", "red", "blue", "green", "yellow"):
            print(f"    Color {color}: {emoji_mutator(sentence, color=color)}")
        
        print("\n")

    print("Error Handling")
    try:
        brain_rot_mutator("oops", intensity=9)
    except ValueError as e:
        print(f"    Brain rot ValueError: {e}")

    try:
        emotion_mutator("999")
    except TypeError as e:
        print(f"    Emotion TypeError: {e}")

    try:
        emotion_mutator("oops", emotion="angry")
    except ValueError as e:
        print(f"    Emotion ValueError: {e}")

    try:
        brain_rot_mutator("999", intensity=1) 
    except TypeError as e:
        print(f"    Brain rot TypeError: {e}")

    try:
        emoji_mutator("hello world", color="purple")
    except ValueError as e:
        print(f"    Emoji ValueError: {e}")

    try:
        emoji_mutator("999", color="red")
    except TypeError as e:
        print(f"    Emoji TypeError: {e}")

if __name__ == "__main__":
    main()