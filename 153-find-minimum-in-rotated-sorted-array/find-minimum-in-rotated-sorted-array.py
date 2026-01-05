class Solution:
    def findMin(self, nums: List[int]) -> int:
        ind = 0
        l, r = 0, len(nums)-1
        n = len(nums)
        ans = nums[0]
        while l <= r:
            m = (l+r)//2
            if nums[m] <= nums[n-1]:
                ans = nums[m]
                r = m-1
            else:
                l = m+1


        
        return ans