"""EX03 - Wordle."""

__author__ = "730490949"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
alt_idx: int = 0


# matching a single character within the user input
def contains_char(search_input: str, single_char: str) -> bool:
    """When given two strings, the first of any length and the second a single character, will return True if index matches and False if otherwise."""
    assert len(single_char) == 1
    idx: int = 0
    while idx < len(search_input):
        if search_input[idx] == single_char:
            return True
        else:
            idx += 1

    return False


# returning the correct-colored emoji boxes based on the matched indices
def emojified(guess: str, secret: str) -> str:
    """Given two strings of equal length, return a string of emoji whose color are green, yellow, or white."""
    assert len(guess) == len(secret)
    idx: int = 0
    resulting_emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            resulting_emoji += GREEN_BOX
        else:
            yellow_white_box: bool = contains_char(secret, guess[idx])
            if yellow_white_box is True:
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        idx += 1
    return resulting_emoji


# user guessing a word of the specified length
def input_guess(expected_length: int) -> str:
    """Will prompt user for a guess and continue prompting them until they provide a guess of expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    el: int = len(guess)
    while el != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
        el = len(guess)
    return guess


# pulling together functions
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    number_turns: int = 1
    while number_turns < 7:
        print(f"=== Turn {number_turns}/6 ===")
        user_guess: str = input_guess(len(secret_word))
        emoji_string: str = emojified(user_guess, secret_word)
        print(emoji_string)
        if user_guess == secret_word:
            print(f"You won in {number_turns}/6 turns!")
            return
        else:
            number_turns += 1
    if number_turns >= 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()