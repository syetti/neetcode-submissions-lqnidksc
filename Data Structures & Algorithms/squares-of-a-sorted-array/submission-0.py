class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L,R = 0, len(nums)-1
        res = [0] * len(nums)
        res_i = len(nums)-1

        while L <= R:
            if abs(nums[L]) < abs(nums[R]):
                res[res_i] = abs(nums[R])**2
                R-=1
            else:
                res[res_i] = abs(nums[L])**2
                L +=1

            res_i -=1
        return res