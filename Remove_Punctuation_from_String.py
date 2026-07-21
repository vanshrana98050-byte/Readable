import string

text = input()

result = ""

for ch in text:
    if ch not in string.punctuation:
        result += ch

print(result)