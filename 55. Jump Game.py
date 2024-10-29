from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        steps = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                steps -= 1
                if steps <= 0:
                    return False
            else:
                steps = max(steps-1, nums[i])
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4])) # True
    print(s.canJump([3,2,1,0,4])) # False
    print(s.canJump([2,0])) # True
    print(s.canJump([1,0])) # True
    print(s.canJump([0])) # True
    print(s.canJump([1])) # True
    print(s.canJump([0,1])) # False
    print(s.canJump([1,2])) # True
    print(s.canJump([1,2,3])) # True
    print(s.canJump([2,3,1,1,4])) # True
