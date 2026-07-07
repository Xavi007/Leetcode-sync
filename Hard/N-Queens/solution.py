class Solution:

    def isSafePosi(self, board, row, col, n):
        for i in range (0, n):
            if(board[row][i] == 'Q'):
                return False

        for i in range (0, n):
            if(board[i][col] == 'Q'):
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
            
        return True


    def helper(self,board, row, ans, n):
        if(row == n):
            ans.append(["".join(r) for r in board])
            return

        for i in range(0, n):
            if(self.isSafePosi(board, row, i, n)):
                board[row][i] = 'Q'
                self.helper(board, row+1, ans, n)
                board[row][i] = '.'



    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        self.helper(board, 0, ans, n)
        return ans