from typing import List
# This is a solution to the problem of merging two sorted arrays in-place.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
        while n >= 0:
            nums1[i] = nums2[n]
            n -= 1
            i -= 1

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1) # [1,2,2,3,5,6]
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1) # [1]
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1) # [1]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [4,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1) # [1,2,3,4,5,6]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [0,0,0]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1) # [0,0,0,1,2,3]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [0,1,2]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1) # [0,1,1,2,2,3]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [3,4,5]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1) # [1,2,3,3,4,5]
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3