class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int right = colors.size()-1;
        int maxi = 0;
        if(right<2){
            return 1;
        }
        for(int i = 0;i<colors.size();i++){
            if(colors[i]!=colors[right]){
                int current = abs(i-right);
                maxi = max(maxi,current);   
            }
            if(colors[right-i]!=colors[0]){
                int current = abs(i-right);
                maxi = max(maxi,current);   
            }   
        }

        return maxi;
    }
};