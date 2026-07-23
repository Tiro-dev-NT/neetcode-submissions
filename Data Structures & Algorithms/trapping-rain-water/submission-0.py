class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        
        for i in range(1, len(height)-1):
            max_left = max(height[:i])
            max_right = max(height[i+1:])

            water_i = min(max_left,max_right) - height[i]

            if water_i > 0:
                total_water += water_i
        return total_water