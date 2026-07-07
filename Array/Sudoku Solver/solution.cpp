class Solution {
public:

    bool isSafePos(vector<vector<char>>& board, int row, int col, char digit)
    {
        for(int i = 0; i < 9; ++i)
        {
            if(board[row][i] == digit)
            {
                return false;
            }
        }

        for(int j = 0; j < 9; ++j)
        {
            if(board[j][col] == digit)
            {
                return false;
            }
        }

        int gridstartRow = (row / 3) * 3;
        int gridstartCol = (col / 3) * 3;

        for(int i = gridstartRow; i <= gridstartRow+2; ++i)
        {
            for(int j= gridstartCol; j <= gridstartCol+2; ++j)
            {
                if(board[i][j] == digit)
                {
                    return false;
                }
            }
        }

        return true;
    }

    bool helper(vector<vector<char>>& board, int row, int col)
    {
        if(row ==9)
        {
            return true;
        }


        int NextRow = row, NextCol = col + 1;

        if (NextCol == 9)
        {
            NextRow = row + 1;
            NextCol = 0;
        }

        if(board[row][col] != '.')
        {
            return helper(board, NextRow, NextCol);
        }


        for(char pos = '1'; pos <= '9'; ++pos)
        {
            if(isSafePos(board, row, col, pos))
            {
                board[row][col] = pos;
                if(helper(board, NextRow, NextCol))
                {
                    return true;
                }
                board[row][col] = '.';
            }
        }
        return false;
    }


    void solveSudoku(vector<vector<char>>& board) 
    {
        helper(board, 0, 0);
    }
};