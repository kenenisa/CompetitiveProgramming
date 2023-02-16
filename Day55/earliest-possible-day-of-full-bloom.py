class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        df = []
        for i in range(n):
            df.append((plantTime[i],growTime[i]))
        def sort_growTime(item):
            return item[1]
        df.sort(key=sort_growTime,reverse=True)
        max_bloom = 0
        total_plant = 0
        for plant,grow in df:
            total_plant += plant
            max_bloom = max(max_bloom,total_plant+grow)
        return max_bloom