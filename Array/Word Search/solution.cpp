class Solution {
public:
    int ROWS, COLS;

    bool helper(vector<vector<char>>& board, string& word, int r, int c, int i) {
        if (i == word.size()) return true;

        if (r < 0 || c < 0 || r >= ROWS || c >= COLS ||
            board[r][c] != word[i]) {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#';  //  visited

        bool res = helper(board, word, r + 1, c, i + 1) ||
                   helper(board, word, r - 1, c, i + 1) ||
                   helper(board, word, r, c + 1, i + 1) ||
                   helper(board, word, r, c - 1, i + 1);

        board[r][c] = temp; // backtrack
        return res;
    }

    bool exist(vector<vector<char>>& board, string word) {
        ROWS = board.size();
        COLS = board[0].size();

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (helper(board, word, r, c, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};