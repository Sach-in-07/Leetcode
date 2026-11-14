class Solution:
    def findDelayedArrivalTime(self, arr: int, d: int) -> int:
        return (arr+d)%24