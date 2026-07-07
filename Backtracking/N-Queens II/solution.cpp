class Solution {
public:
    bool isPositionSafe(vector<string> &board, int row, int col, int n)
    {
        for(int i = 0; i < n; ++i) // row
        {
            if(board[row][i] == 'Q')
            {
                return false;
            }
        }

        for(int j = 0; j < n; ++j) // column
        {
            if(board[j][col] == 'Q')
            {
                return false;
            }
        }


        // left diagonal
        for(int i = row, j = col; i >= 0 && j >= 0; --i, --j)
        {
            if(board[i][j] == 'Q')
            {
                return false;
            }
        }


        // right diagonal
        for(int i = row, j = col; i >= 0 && j >= 0; --i, ++j)
        {
            if(board[i][j] == 'Q')
            {
                return false;
            }
        }

        return true;
    }

    void helper(vector<string> &board, int row, int n, vector<vector<string>> &ans)
    {
        if(row == n)
        {
            ans.push_back({board});
            return;
        }

        for(int i = 0; i < n; ++i)
        {
            if(isPositionSafe(board, row, i, n))
            {
                board[row][i] = 'Q';
                helper(board, row+1, n , ans);
                board[row][i] = '.';
            }
            
        }
    }


    int totalNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> ans;

        helper(board, 0, n, ans);

        return ans.size();
    }
};