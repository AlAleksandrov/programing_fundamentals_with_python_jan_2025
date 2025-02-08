words = input().split()
palindrome = input()
all_found_palindromes = []

[all_found_palindromes.append(word) for word in words if word == word[::-1]]

print(all_found_palindromes)
print(f"Found palindrome {all_found_palindromes.count(palindrome)} times")