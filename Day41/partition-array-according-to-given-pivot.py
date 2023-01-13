class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        partition = defaultdict(list)
        for num in nums:
            if num > pivot:
                partition['right'].append(num)
            elif num < pivot:
                partition['left'].append(num)
            else:
                partition['center'].append(num)
        return partition['left'] + partition['center'] + partition['right']
