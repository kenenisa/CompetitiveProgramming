class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        mx = 0
        while right > left:
            mx = max(mx, (right-left) * min(height[left],height[right]))
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return mx