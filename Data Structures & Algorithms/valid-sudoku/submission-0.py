class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        
        # check col
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        
        # check 3*3 grid 
        for row in range(3):
            for col in range(3):
                start_i = row * 3
                start_j = col * 3
                # [i, j] => [i+3][j+3]
                s = set()
                for i in range(start_i, start_i+3):
                    for j in range(start_j, start_j+3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in s:
                            return False
                        s.add(board[i][j])
        
        return True