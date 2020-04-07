def digitize(n):
    digits = []
    while n:
        digits.append( n % 10 )
        n = n // 10
    return digits[::-1]

def is_palindrome(n):
    digits = digitize(n)
    for i in range(len(digits)):
        if digits[i] != digits[-i-1]:
            return False
    return True

palindromes = []

for i in range(100,1000):
    for j in range(i, 1000):
        if is_palindrome(i*j):
            palindromes.append(i*j)

print(max(palindromes))
