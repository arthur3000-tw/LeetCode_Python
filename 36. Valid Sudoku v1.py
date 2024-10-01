class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            s = set()
            for num in row:
                if num == ".":
                    continue
                if num in s:
                    return False
                else:
                    s.add(num)
        
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                else:
                    s.add(board[j][i])
        
        for i in range(9):
            s = set()
            for j in range(3):
                n = (i // 3) * 3 + j
                for k in range(3):
                    m = (i % 3) * 3 + k
                    if board[n][m] == ".":
                        continue
                    if board[n][m] in s:
                        return False
                    else:
                        s.add(board[n][m])

        return True
        # Time: O(n * n)
        # Space: O(n)
