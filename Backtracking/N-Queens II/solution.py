class Solution:

    def isSafeBuffer(self, board, row, col, n):
        for i in range(0, n):
            if(board[row][i] == 'Q'):
                return False

        for i in range(0, n):
            if(board[i][col] == 'Q'):
                return False
            
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if(board[i][j] == 'Q'):
                return False
            
        i, j = row, col

        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
            
        return True

    def helper(self, board, row, n, ans):
        if(row == n):
            ans.append([''. join(row) for row in board])
            return 

        for i in range(n):
            if(self.isSafeBuffer(board, row, i, n)):
                board[row][i] = 'Q'
                self.helper(board, row + 1, n, ans)
                board[row][i] = '.'


    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.helper(board, 0, n, ans)
        return len(ans)
        