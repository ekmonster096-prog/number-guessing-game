# Number Guessing Game

A terminal-based number guessing game in Python. Pick a difficulty, then guess the secret number using Higher/Lower hints.

## Features
- 3 difficulty levels: Easy, Medium, Hard
- 3 rounds per game
- Limited attempts per round
- Higher/Lower hints after each guess
- Input validation (no crash on wrong input)
- Win/loss summary at the end

## Difficulty

| Level  | Number range | Attempts per round |
|--------|--------------|--------------------|
| Easy   | 1-10         | 4                  |
| Medium | 1-50         | 6                  |
| Hard   | 1-100        | 7                  |

## How to run

Make sure Python 3 is installed, then:

```bash
git clone https://github.com/ekmonster096-prog/number-guessing-game.git
cd number-guessing-game
python guessing_game.py
```

## Concepts used
- Functions
- Dictionaries
- Loops and conditionals
- Exception handling (`try/except`)
- `random` and `time` modules

## Author
ekmonster096-prog
