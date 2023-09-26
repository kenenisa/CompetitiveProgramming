import string

s = input()

low = 0
result = 0
for i in range(len(s)):
    if s[i] in string.ascii_lowercase:
        low += 1
    if s[i] in string.ascii_uppercase:
        if low:
            low -= 1
            result += 1
print(result)
