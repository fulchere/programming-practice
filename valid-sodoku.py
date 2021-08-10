class Solution:
    def validateRow(self, board, rowNum):
        nums = [False for i in range(9)]

        for n in board[rowNum]:
            #print("nums is", nums)
            if n.isnumeric():
                if nums[int(n)-1]:
                    return False
                else:
                    nums[int(n)-1] = True
        return True

    def validateCol(self, board, colNum):
        nums = [False for i in range(9)]
        col = [row[colNum] for row in board]

        for n in col:
            if n.isnumeric():
                if nums[int(n)-1]:
                    return False
                else:
                    nums[int(n)-1] = True
        return True

    def validateBox(self, board, boxNum):
        boxCoords = [[0, 0],
                     [3, 0],
                     [6, 0],
                     [0, 3],
                     [3, 3],
                     [6, 3],
                     [0, 6],
                     [3, 6],
                     [6, 6]]
        nums = [False for i in range(9)]
        box = []
        c = boxCoords[boxNum]
        for i in range(3):
            for j in range(3):
                box.append(board[c[0]+i][c[1]+j])

        #print("box is", box)
        for n in box:
            if n.isnumeric():
                if nums[int(n)-1]:
                    return False
                else:
                    nums[int(n)-1] = True
        return True

    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            if not (self.validateRow(board, i) and self.validateCol(board, i) and self.validateBox(board, i)):
                return False
        return True


s = Solution()

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(s.isValidSudoku(board))

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(s.isValidSudoku(board))
