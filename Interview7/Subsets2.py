class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # soting the nums
        self.res = [] # creating the empty array
        self.backtrack(nums, [], 0) # calling the function recursively with nums
        return self.res # returning the result
    
    def backtrack(self, nums, current, start):
        self.res.append(current) # appending the current to result
        if start > len(nums): # if start is greater than length of nums
            return
        for i in range(start, len(nums)): # run until length of nums and check i is greater than start and numsof i-1 is equal to nums of i then continue
            if i > start and nums[i-1] == nums[i]:
                continue
            self.backtrack(nums, current + [nums[i]], i + 1) # calling the function recursively with current+nums[i]