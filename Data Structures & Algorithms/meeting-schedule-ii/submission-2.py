import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ends = []                                 # end time of every busy room
        for meeting in intervals:
            if ends and ends[0] <= meeting.start:   # earliest room is free → reuse it
                heapq.heappop(ends)
            heapq.heappush(ends, meeting.end)       # this meeting takes a room
        return len(ends)