from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValid(row):
                return False
        for col in zip(*board):
            if not self.isValid(col):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValid([board[x][y] for x in range(3*i, 3*i+3) for y in range(3*j, 3*j+3)]):
                    return False
        return True

    def isValid(self, nums: List[str]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != '.':
                return False
        return True