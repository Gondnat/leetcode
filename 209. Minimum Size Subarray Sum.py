from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        left = 0
        right = 0
        sum_ = 0
        min_len = n + 1
        while right < n:
            sum_ += nums[right]
            while sum_ >= target:
                min_len = min(min_len, right - left + 1)
                sum_ -= nums[left]
                left += 1
            right += 1
        return 0 if min_len == n + 1 else min_len
    
if __name__ == '__main__':
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    target = 213
    print(Solution().minSubArrayLen(target, nums))
    