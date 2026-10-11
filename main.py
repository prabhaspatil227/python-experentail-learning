import random

WORDS = [
    {"word": "python", "hint": "A popular programming language."},
    {"word": "computer", "hint": "An electronic device used to process data."},
    {"word": "keyboard", "hint": "You use this to type."},
    {"word": "algorithm", "hint": "A step-by-step method for solving a problem."},
    {"word": "variable", "hint": "A named place to store a value in code."},
    {"word": "internet", "hint": "A worldwide network connecting computers."},
    {"word": "function", "hint": "Reusable block of code that performs a task."},
    {"word": "science", "hint": "The systematic study of the natural world."},
    {"word": "planet", "hint": "A large object that orbits a star."},
    {"word": "puzzle", "hint": "A game or problem that tests your thinking."},
    {"word": "developer", "hint": "A person who creates software."},
    {"word": "database", "hint": "An organized collection of information."},
    {"word": "network", "hint": "A group of connected computers or devices."},
    {"word": "security", "hint": "Protection against danger or unauthorized access."},
    {"word": "education", "hint": "The process of learning and gaining knowledge is superpower."},
]

ATTEMPTS_PER_ROUND = 3
ROUNDS_PER_GAME = 5


def scramble_word(word):
    """Return a shuffled version of a word, avoiding the original when possible."""
    letters = list(word)
    scrambled = letters[:]
    for _ in range(10):
        random.shuffle(scrambled)
        result = "".join(scrambled)
        if result != word:
            return result
    return "".join(letters[::-1]) if word[::-1] != word else word


def play_round(round_number, used_words):
    available = [item for item in WORDS if item["word"] not in used_words]
    if not available:
        used_words.clear()
        available = WORDS[:]

    item = random.choice(available)
    word = item["word"]
    used_words.add(word)

    print(f"\n--- Round {round_number} of {ROUNDS_PER_GAME} ---")
    print("Unscramble this word:", scramble_word(word))
    print(f"You have {ATTEMPTS_PER_ROUND} attempts.")

    score = 0
    hint_used = False

    for attempt in range(1, ATTEMPTS_PER_ROUND + 1):
        if attempt == 2 and not hint_used:
            choice = input("Would you like a hint? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                print("Hint:", item["hint"])
                hint_used = True

        guess = input(f"Attempt {attempt}/{ATTEMPTS_PER_ROUND} — Your guess: ").strip().lower()
        if guess == word:
            points = 10 if attempt == 1 else 7 if attempt == 2 else 5
            if hint_used:
                points = max(1, points - 2)
            print(f"Correct! The word was '{word}'. You earned {points} points.")
            score = points
            break
        else:
            print("Not quite. Try again!")

    if score == 0:
        print(f"Out of attempts! The correct word was '{word}'.")
    return score


def main():
    print("=" * 42)
    print("          WORD JUMBLE GAME")
    print("=" * 42)
    print("Unscramble the letters, guess the word, and earn points!")
    print(f"Each game has {ROUNDS_PER_GAME} rounds.\n")

    while True:
        total_score = 0
        used_words = set()

        for round_number in range(1, ROUNDS_PER_GAME + 1):
            total_score += play_round(round_number, used_words)
            print(f"Current score: {total_score}")

        print("\n" + "=" * 42)
        print(f"GAME OVER! Final score: {total_score}/{ROUNDS_PER_GAME * 10}")
        print("=" * 42)

        again = input("Play another game? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing Word Jumble. Goodbye! have a nice day")
            break


if __name__ == "__main__":
    main()
