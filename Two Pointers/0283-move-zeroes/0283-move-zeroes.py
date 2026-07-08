class Solution(object):
    def moveZeroes(self, nums):
        count = nums.count(0)

        while 0 in nums:
            nums.remove(0)

        nums.extend([0] * count)