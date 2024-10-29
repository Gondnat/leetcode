from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        i = 0
        while i < len(nums)-1:
            if i + nums[i] >= len(nums)-1:
                return steps + 1
            max_num = 0
            max_index = 0
            for j in range(1, nums[i]+1):
                if j + nums[i+j] > max_num:
                    max_num = j + nums[i+j]
                    max_index = j
            i += max_index

            steps += 1
        return steps
    
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4])) # 2
    print(s.jump([2,3,0,1,4])) # 2
    print(s.jump([1,2,3])) # 2
    print(s.jump([1,1,1,1])) # 3
    print(s.jump([1,2])) # 1
