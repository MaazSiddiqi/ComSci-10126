numWords = int(input('How many words do you want to enter? '))
longestWord = ''

for i in range(1,numWords+1):
    word = input('Enter word #{}: '.format(i))
    if len(longestWord) < len(word):
        longestWord = word

print(f'The longest word is “{longestWord}”, with length {len(longestWord)}.')
