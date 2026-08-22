class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sorting the array
        people = sorted(people)
        left = 0
        right = len(people)-1
        boats = 0
        while left <= right:
            if people[right] == limit or people[right] + people[left] > limit:
                boats+=1
                right-=1
            elif people[right] + people[left] <= limit:
                right-=1
                left+=1
                boats+=1
        return boats