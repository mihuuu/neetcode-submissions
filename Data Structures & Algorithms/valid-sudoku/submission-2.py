class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one pass (instead of checking rows/cols/grids separately)
        # for each element, check if it was seen in the same row/col/grid
        rows = defaultdict(set)  # i: seen set of row i
        cols = defaultdict(set)
        grids = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                grid_index = (i // 3) * 3 + (j // 3)
                print(grid_index)
                if board[i][j] in grids[grid_index]:
                    return False
                # no dup
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grids[grid_index].add(board[i][j])
        
        return True
