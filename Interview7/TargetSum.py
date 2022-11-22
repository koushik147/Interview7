class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # creating a dictionary
        return self.backtrack(nums, 0, target, memo) # calling the function recursively with nums
    
    def backtrack(self, nums, i, target, memo):
        if (i, target) in memo: # if i and target in memo then return memo of i and target
            return memo[i, target] 
        if i == len(nums): # if i is equal to length of nums and target is equal to 0 then return 1
            if target == 0: 
                return 1
            else: # else return 0
                return 0

        curSum = 0 # create currsum to 0
        curSum += self.backtrack(nums, i+1, target - nums[i], memo) # calling the backtrack function with target-nums and assing it to cursum
        curSum += self.backtrack(nums, i+1, target + nums[i], memo) # calling the backtrack function with target+nums and assing it to cursum
        memo[(i, target)] = curSum # assigning the cursum to memo
        return curSum # returning the cursum