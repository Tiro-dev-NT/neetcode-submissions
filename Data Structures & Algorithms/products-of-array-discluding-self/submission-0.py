class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_num = []
        for i in range(len(nums)):
            s = 1
            for j in range(len(nums)):
                if i != j:
                    s = s * nums[j]
            out_num.append(s)
        return out_num
