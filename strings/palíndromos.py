#versão 1
texto = input('Digite a palavra: ')
if texto[::-1] == texto:
    print(f'A palavra {texto} é um palíndromo')
else:
    print(f'A palavra {texto} não é um palíndromo')

#versão 2
word = input('Type a word: ')
palindrome = word == word[::-1]
print(f'Is the word {word} a palindrome?')
print(palindrome)
