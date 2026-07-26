import heapq

def kthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kthLargest([3,2,1,5,6,4],2))