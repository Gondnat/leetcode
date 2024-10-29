from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        for i in range(len(nums)):
            if i == 0:
                start = nums[i]
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    ret.append(str(start))
                else:
                    ret.append(str(start) + "->" + str(nums[i])) 
                start = nums[i + 1] if i != len(nums) - 1 else None
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(s.summaryRanges([]))
    print(s.summaryRanges([-1]))
    print(s.summaryRanges([0]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 10, 11]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16]))
    print(s.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17]))