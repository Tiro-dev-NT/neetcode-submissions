class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            total = numbers[left] + numbers[right]
            
            if total == target:
                return [left + 1, right + 1]  # +1 vì 1-indexed
            elif total < target:
                left += 1   # tổng nhỏ hơn target -> tăng số bé lên
            else:
                right -= 1  # tổng lớn hơn target -> giảm số lớn xuống
        
        return []  # không cần thiết vì đề bài đảm bảo có nghiệm