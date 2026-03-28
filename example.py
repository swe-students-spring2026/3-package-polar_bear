"""pipenv run python example.py"""
from bs_generator.brain_rot import brain_rot_mutator

SAMPLES = [
    "I just pushed my code to production.",
    "The tests are failing again.",
    "Can someone review my pull request?",
]

def main() -> None:
    for level in (1, 2, 3):
        print(f"\nIntensity {level}")
        for sentence in SAMPLES:
            print(f"  Original : {sentence}")
            print(f"  Mutated  : {brain_rot_mutator(sentence, intensity=level)}")

    print("\nError handling")
    try:
        brain_rot_mutator("oops", intensity=9)
    except ValueError as e:
        print(f"  ValueError: {e}")

    try:
        brain_rot_mutator(999, intensity=1) 
    except TypeError as e:
        print(f"  TypeError: {e}")

if __name__ == "__main__":
    main()