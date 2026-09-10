class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Array to store the net change in passengers at each location
        diff = [0] * 1001
        
        # Populate the difference array
        for num_passengers, start, end in trips:
            diff[start] += num_passengers  # Passengers get in
            diff[end] -= num_passengers    # Passengers get out
            
        # Calculate prefix sum to find the current passengers at any point
        cur_passengers = 0
        for change in diff:
            cur_passengers += change
            # If at any point the car is over capacity, return False
            if cur_passengers > capacity:
                return False
                
        return True