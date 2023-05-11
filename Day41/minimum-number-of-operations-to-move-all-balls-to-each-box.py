class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = []
        for i in range(n):
            left = i - 1
            right = i + 1
            count = 0
            while left >= 0:
                count += i - left if boxes[left] == '1' else 0
                left -= 1
            while right < n:
                count += right - i if boxes[right] == '1' else 0
                right += 1
            result.append(count)
        return result    
