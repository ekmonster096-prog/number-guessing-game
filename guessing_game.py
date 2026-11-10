import random
import time

def play_round(maximum, attempts):
    secret = random.randint(1, maximum)

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - guess (1-{maximum}): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == secret:
            print(f"You win! Took {attempt} attempts.")
            return True
        elif guess < secret:
            print("Higher!")
        else:
            print("Lower!")

    print(f"Out of attempts! The number was {secret}")
    return False


def main():
    win = 0
    loss = 0

    print("1. Easy\n2. Medium\n3. Hard")
    ask = input("Choose: ")

    settings = {
        "1": (3, 10, 4),      # rounds, maximum, attempts per round
        "2": (3, 50, 6),
        "3": (3, 100, 7),
    }

    if ask not in settings:
        print("Invalid choice!")
        return

    rounds, maximum, attempts = settings[ask]

    for r in range(1, rounds + 1):
        print(f"\n--- Round {r} ---")
        if play_round(maximum, attempts):
            win += 1
        else:
            loss += 1
        time.sleep(1)

    print("\n----- GAME RESULTS -----")
    print(f"Won: {win} | Lost: {loss} | Rounds: {rounds}")


if __name__ == "__main__":
    main()