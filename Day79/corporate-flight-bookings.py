class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n+1)

        for book in bookings:
            result[book[0]-1] += book[2]
            result[book[1]] -= book[2]
        for i in range(1,n):
            result[i] += result[i-1]
        result.pop()
        return result