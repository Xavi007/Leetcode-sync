class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {

        vector<int>frequency_map(26, 0);

        for(int i=0;i<magazine.size();++i){
            frequency_map[magazine[i]-'a']++;
        }
        for(int i=0;i<ransomNote.size();++i){
            if(frequency_map[ransomNote[i]-'a']<=0)
            {
                return 0;
            }
            else
            {
                frequency_map[ransomNote[i]-'a']--; 
            }  
        }
        return 1;
    }
};