class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Build adjacency list locally so it resets per test case
        vector<vector<int>> adj(numCourses);
        for (const auto& pre : prerequisites) {
            adj[pre[1]].push_back(pre[0]); // pre[1] must be taken before pre[0]
        }
        
        // 0 = unvisited, 1 = visiting (in current DFS path), 2 = visited
        vector<int> state(numCourses, 0);
        
        auto hasCycle = [&](auto& self, int node) -> bool {
            if (state[node] == 1) return true;  // Cycle detected!
            if (state[node] == 2) return false; // Already checked and safe
            
            state[node] = 1; // Mark as currently visiting
            for (int neighbor : adj[node]) {
                if (self(self, neighbor)) return true;
            }
            state[node] = 2; // Mark as fully visited
            return false;
        };
        
        // Check every course for cycles
        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0) {
                if (hasCycle(hasCycle, i)) return false;
            }
        }
        
        return true;
    }
};