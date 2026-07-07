class MinStack {
private:
    vector<vector<int>> mystack;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        int min_val = getMin();
        if (mystack.empty() || min_val > val) {
            min_val = val;
        }
        mystack.push_back({val, min_val});        
    }
    
    void pop() {
        mystack.pop_back();
    }
    
    int top() {
        return mystack.empty() ? -1 : mystack.back()[0];
    }
    
    int getMin() {
        return mystack.empty() ? -1 : mystack.back()[1]; 
    }
};