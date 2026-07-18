class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_sort = sorted(nums)
        length = [1 for _ in range(len(nums))]
        length_index = 0
        for i in range(len(nums)-1):
            if nums_sort[i] == nums_sort[i+1]:
                continue
            
            if nums_sort[i] + 1 == nums_sort[i+1]:    
                length[length_index] += 1
            else:
                length_index += 1

        return max(length)