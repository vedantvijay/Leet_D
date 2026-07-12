class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int>st;
        
        for(int i=0;i<arr.size();i++){
            st.insert(arr[i]);
        }

        unordered_map<int,int>mp;
        int rk=1;
        
        for(int num:st){
            mp[num]=rk;
            rk++;
        }

        for(int i=0;i<arr.size();i++){
            arr[i]=mp[arr[i]];
        }

        return arr;

    }
};