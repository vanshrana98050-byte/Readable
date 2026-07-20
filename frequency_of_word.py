sentence = input().split()

freq = {}

for word in sentence:
    freq[word] = freq.get(word, 0) + 1

for key, value in freq.items():
    print(key, ":", value)