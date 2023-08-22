class Solution {
public:
    bool isValid(string s) {
        stack<char> com;
    

        for(int i=0; i<s.length(); i++)
        {
            if(com.empty()){
                com.push(s[i]);
                
            }

            else if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            {
                com.push(s[i]);
                
            }
            
            else if(s[i]==')' || s[i]=='}' || s[i]==']')
            {
                if((com.top()=='(' && s[i]==')') || (com.top()=='{' && s[i]=='}') || (com.top()=='[' && s[i]==']'))
                {
                    com.pop();
                    x= true;
                }
                else
                {
                    x= false;
                }
            }
        }
        
        return x;
        
        
        
          
        };
};
