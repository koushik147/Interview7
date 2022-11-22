class Solution:
    def countArrangement(self, n: int) -> int:
        if not n or n < 1: # if not n and n is less than 1 then return 0
            return 0

        visited = [False]*n # creating the array with length of n 
        count = [0]
        self.dfs(visited, n, 0, count) # calling the function recursively with visited array

        return count[0] # returning the count of 0

    def dfs(self, visited, n, i, count):
        if i == n: # if i is equal to n the count[0] is incremented by 1
            count[0] += 1
            return

        for j in range(n):
            divisible = ((j+1) % (i+1) == 0) or ((i+1) % (j+1)== 0) # if j+1 is divisible by i+1 or i+1 is divisible by j+1
            if not visited[j] and divisible: # if divisible is not null then assign visited to true
                visited[j] = True
                self.dfs(visited, n, i+1, count) # calling the dfs function recursively with visited
                visited[j] = False # assign the visited to false
