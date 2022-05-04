# COMP 1026 – Assignment 2

# Maaz Siddiqi

# Program made to compare names using a phonetic algorithm


def format_soundex(soundex):
    """
    format_soundex
    Formats provided soundex to ensure length is 0 by either trimming down or adding 0s to the end
    soundex: a partial soundex string that may be greater or less than the formal length of 4 for soundex strings
    Returns soundex, a copy of soundex provided formatted to a length of 4
    """

    # Based on length, adjust partial soundex provided
    # If more than 4, trim
    # If less, add 0s until length of soundex is 4
    if len(soundex) > 4:
        return soundex[:4]
    else:
        while len(soundex) != 4:
            soundex += '0'

        return soundex


def simplify_digits(digits: str):
    """
    simplify_digits
    Remove all immediate duplicates within string of digits provided
    digits: string of soundex digits provided possibly containing immediate duplicates
    Returns simplified_digits, a copy of digits without any immediate duplicates
    """

    # Create new simplified string where
    # for each letter in soundex digits string, if value is same as previous value, skip iteration (continue)
    simplified_digits = ''
    for i, digit in enumerate(digits):
        if i != 0 and digits[i - 1] == digit:
            continue
        simplified_digits += digit

    return simplified_digits


def to_soundex_digits(word):
    """
    to_soundex_digits
    Replace characters in word with corresponding soundex digits
    word: string to format corresponding to soundex digits
    Returns digits, a string of digits from soundex table
    """

    # Soundex table from phonetic algorithm
    SOUNDEX_TABLE = {
        0: ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w'],
        1: ['b', 'f', 'p', 'v'],
        2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
        3: ['d', 't'],
        4: ['l'],
        5: ['m', 'n'],
        6: ['r']
    }

    # For each letter in word, find corresponding soundex digit in soundex table and create new soundex digits string
    digits = ''
    for char in word:
        for digit, letters in SOUNDEX_TABLE.items():
            if char in letters:
                digits += str(digit)

    return digits


def encode_soundex(word):
    """
    encode_soundex
    Translate a word into soundex using a phonetic algorithm
    word: original string to translate into soundex
    Returns soundex, the soundex of word
    """

    # Set word to lower and extract F value
    word = word.lower()
    f = word[0]

    # Transform word into soundex
    d = to_soundex_digits(word)
    d = simplify_digits(d)
    d = d.replace('0', '')

    # Based on starting value of D after conversion to soundex digits, implement F into soundex
    f_soundex = to_soundex_digits(f)
    if len(d) == 0:
        partial_soundex = f_soundex
    elif f_soundex == d[0]:
        partial_soundex = f + d[1:]
    else:
        partial_soundex = f + d

    # Format partial soundex formed to a length of 4
    soundex = format_soundex(partial_soundex)

    return soundex


def prompt_for_names():
    """
    prompt_for_names
    Prompt the user to enter a list of names and store the names locally in a list
    No Parameters
    Returns an array of all the names the user entered
    """

    print("Enter names, one on each line. Type DONE to quit entering names.")
    names = []
    while True:
        name = input()

        if name == "DONE":
            break

        names.append(name)

    return names


def main():
    # Get names from user
    names = prompt_for_names()

    # Encode each name into a soundex and store as tuple (soundex, name)
    encoded_names = []
    for name in names:
        soundex = encode_soundex(name)
        encoded_names.append((soundex, name))

    # For each name, search list of names for different words with same soundex and record them
    same_soundex_names = []
    for soundex1, name1 in encoded_names:
        for soundex2, name2 in encoded_names:
            if name2 == name1:
                # If names are the same, skip iteration; ensures examining unique names
                continue

            # If soundex is the same, format output in alphabetical order
            # Ensure output isn't already in output list, same_soundex_names, otherwise add to output list
            if soundex2 == soundex1:
                output = f'{min(name1, name2)} and {max(name1, name2)} have the same Soundex encoding.'
                if output not in same_soundex_names:
                    same_soundex_names.append(output)

    # Sort output list alphabetically
    same_soundex_names.sort()

    # Print each output in output list
    for output in same_soundex_names:
        print(output)


help(prompt_for_names())
main()
