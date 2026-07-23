class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for left in range(n):
            for right in range(left+1,n):
                width = right - left
                height = min(heights[left], heights[right])
                area_new = width * height
                if area < area_new:
                    area = area_new
        return area