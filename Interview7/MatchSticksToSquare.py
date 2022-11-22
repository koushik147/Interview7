class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks: # if not in matchsticks then return false
            return False
        sum_val = sum(matchsticks) # assigning the sum of matchsticks to sumn
        matchsticks.sort(reverse=True) # soorting the matchsticks to reverse
        if sum_val % 4: # if sum value modules 4 then return false
            return False
        return self.dfs(matchsticks, [0,0,0,0], 0, sum_val/4) # calling the dfs function recursively with matchsticks value
    
    def dfs(self, matchsticks, t, pos, target):
        if pos == len(matchsticks): # if position is equal to length of matchsticks
            if t[0] == t[1] == t[2]: # if all the values is equal then return true
                return True
            return False # else return false
        for i in range(4):
            if t[i] + matchsticks[pos] > target: # run until the loop when t of i th value and matchsticks position is greater than the target
                continue
            t[i] += matchsticks[pos] # adding the matchsticks of position to t of ith value
            if self.dfs(matchsticks, t, pos+1, target): # if recursive calling function with matchsticks then return true
                return True
            t[i] -= matchsticks[pos] # subtracting the matchsticks of i from t of ith value
        return False # else returning false