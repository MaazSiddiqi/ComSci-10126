def pigLatin(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    word = word.lower()
    idx = -1

    for letter in word:
        idx += 1
        if letter not in consonants:
            break

    _word = ''
    if idx == 0:
        _word = word + 'yay'
    else:
        _word = word[idx:] + word[:idx] + 'ay'

    return _word


test = ['pig', 'computer', 'science', 'scram', 'Western',  'Ontario', 'apple']

for Word in test:
    print(f'{Word} in Pig Latin is {pigLatin(Word)}')
