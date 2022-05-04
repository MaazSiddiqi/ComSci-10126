def countVowels(word):
    numVowels = 0  # Vowels count should initialize with a value of 0, not q
    for letter in word:  # loop should run over the string passed in, 'string' is undefined
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:  # letter must be put to lowercase before checking with array to catch capital vowels as well
            numVowels += 1

    return numVowels  # must return vowel count stored in numVowels, not the letter inside loop. Also should be run after loop, not within loop or else the loop will immediately return after first itteration


print(countVowels('Authorize'))
