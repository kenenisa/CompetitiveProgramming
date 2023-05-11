class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        evenSum = sum([i if i & 1==0 else 0 for i in nums])
        for query in queries:
            added = nums[query[1]]
            added += query[0]
            if nums[query[1]] & 1 == 0:
                evenSum -= nums[query[1]]
            if added & 1 == 0:
                evenSum += added
            nums[query[1]] = added
            answer.append(evenSum)
            # print(nums)
        return answer
# class Solution:
#     def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         answer = []
#         for query in queries:
#             nums[query[1]] += query[0]
#             answer.append(sum([i if i&1==0 else 0 for i in nums]))
#         return answer