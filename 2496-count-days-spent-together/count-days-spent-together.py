class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day(date):
            month, d = map(int, date.split('-'))
            return sum(days[:month - 1]) + d

        start = max(day(arriveAlice), day(arriveBob))
        end = min(day(leaveAlice), day(leaveBob))

        return max(0, end - start + 1)