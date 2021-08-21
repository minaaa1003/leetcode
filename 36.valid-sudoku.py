#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for row in range(9):
            my_list = []
            for col in range(9):
                num = board[row][col]
                if num.isnumeric():
                    if num not in my_list:
                        my_list.append(num)
                    else:
                        return False

        for x in range(9):
            my_list = []
            for y in range(9):
                num = board[y][x]
                if num.isnumeric():
                    if num not in my_list:
                        my_list.append(num)
                    else:
                        return False
    
            for row_start in range(0,9,3):
                for col_start in range(0,9,3):
                    my_list = []
                    for x in range(row_start, row_start+3):
                        for y in range(col_start, col_start+3):
                            num = board[y][x]
                            if num.isnumeric():
                                if num not in my_list:
                                    my_list.append(num)
                                else:
                                    return False
        return True
