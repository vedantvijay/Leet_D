class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int>res;
        vector<int>z;
        string s="123456789";
        int n=0;
        int i=0;
        while(i<s.length()){
            string r={s[i]};
            for(int j=i+1;j<s.length();j++){
                r+=s[j];
                n=stoi(r);
                res.push_back(n);
            }
            i++;
        }
        for(int k=0;k<res.size();k++){
            if(res[k]>=low && res[k]<=high){
                z.push_back(res[k]);
            }
        }
        sort(z.begin(),z.end());
        return z;
    }
};