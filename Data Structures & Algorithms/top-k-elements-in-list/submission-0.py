from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create dict - count
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        freq =[[] for _ in range(len(nums)+1)]
        for i, j in count.items():
            freq[j].append(i)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result