from collections import Counter

def topK(nums, k):
    count = Counter(nums)
    return [x for x, _ in count.most_common(k)]

print(topK([1,1,1,2,2,3],2))