"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730490949"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must be a single character.")
        exit()

character_match: int = 0
print("Searching for " + single_character + " in " + five_character_word)

if single_character == five_character_word[0]: 
    print(single_character + " found at index 0")
    character_match = character_match + 1
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
    character_match = character_match + 1
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
    character_match = character_match + 1
if single_character == five_character_word[3]: 
    print(single_character + " found at index 3")
    character_match = character_match + 1
if single_character == five_character_word[4]: 
    print(single_character + " found at index 4")
    character_match = character_match + 1 

if character_match == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
else:
    if character_match == 1:
        print("1 instance of " + single_character + " found in " + five_character_word)
    else:
        print(str(character_match) + " instances of " + single_character + " found in " + five_character_word)