"""ex02 - One Shot Wordle."""

__author__ = "730490949"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
resulting_emoji: str = ""
guessed_character: bool = False
alt_idx: int = 0

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

while idx < len(secret_word):
    if guess[idx] == secret_word[idx]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        while guessed_character is not True and idx < len(secret_word) and alt_idx < len(secret_word):
            if secret_word[alt_idx] == guess[idx]:
                guessed_character = True
            else:
                alt_idx = alt_idx + 1
        if guessed_character is True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
        guessed_character = False
        alt_idx = 0
    idx = idx + 1
print(resulting_emoji)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")