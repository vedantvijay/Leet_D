class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int c = 0;
       int k = 0;
        for(int i = 0; i<moves.length();i++){
            if(moves[i] == 'L' || moves[i] == '_' ){
                c++;
            }
             if(moves[i] == 'R'){
                c--;
             }
        }
        for(int i = 0; i<moves.length();i++){
            if(moves[i] == 'R' || moves[i] == '_' ){
                k++;
            }
             if(moves[i] == 'L'){
                k--;
             }
        }

        return max(c,k);
    }
};