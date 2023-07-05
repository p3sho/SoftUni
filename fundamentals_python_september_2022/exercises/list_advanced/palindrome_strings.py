strings = input().split(' ')
serached_palindrome = input()
palindromes = []

for word in strings:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(f'{palindromes}')
print(f'Found palindrome {palindromes.count(serached_palindrome)} times')