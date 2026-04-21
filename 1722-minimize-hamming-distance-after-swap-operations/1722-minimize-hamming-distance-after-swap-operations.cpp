class Solution {
public:
    // Standard Find with Path Compression
    int find(vector<int>& parent, int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent, parent[i]);
    }

    void unite(vector<int>& parent, int i, int j) {
        int rootI = find(parent, i);
        int rootJ = find(parent, j);
        if (rootI != rootJ) parent[rootI] = rootJ;
    }

    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;

        // Step 1: Union indices
        for (auto& swap : allowedSwaps) {
            unite(parent, swap[0], swap[1]);
        }

        // Step 2: Group source elements by their component root
        unordered_map<int, unordered_map<int, int>> components;
        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            components[root][source[i]]++;
        }

        // Step 3: Count mismatches
        int distance = 0;
        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            if (components[root][target[i]] > 0) {
                components[root][target[i]]--;
            } else {
                distance++;
            }
        }

        return distance;
    }
};