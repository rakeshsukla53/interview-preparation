__author__ = 'rakesh'

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        rooms = 0
        end_time = []
        for i in range(len(intervals)):

            if i == 0:
                rooms += 1
                start, end = intervals[i]
                end_time.append(end)
            else:
                start, end = intervals[i]
                if start <= end_time[0]:
                    rooms += 1
                    end_time.append(end)
                else:
                    end_time.append(end)

                end_time.sort()

        return rooms

print Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
