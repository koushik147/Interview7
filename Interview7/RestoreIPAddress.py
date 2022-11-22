class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s) # length of s
        #edge condition     
        self.result=[] # creating the empty result array 
        self.backtrack(n,s,0,[]) # calling the backtrack function recursively with pivot, substring values
        return self.result # returning the result array


    def backtrack(self,n,s,pivot,substrings):
        #base condition
        if pivot==n and len(substrings)==4: # if pivot is equal to n and length of substring is equal to 4
            temp = ".".join(substrings) # join the substrings and store in temp
            self.result.append(temp) # appending the temp in the resultant array
            return

        if len(substrings)>4: # if length of substrings is greater than 4
            return
        #logic
        for i in range(pivot,len(s)): # run until the length of s 
            substr = s[pivot:i+1] # generate the substring by s from pivot to i+1th element
            if self.isValidIP(substr): # checking the substring is valid IP address
                #action
                substrings.append(substr) # appending the substring in the substring array

                #recurse
                self.backtrack(n,s,i+1,substrings) # recursively calling the backtrack function with i+1th value

                #backtrack
                substrings.pop() # popping the substring



    def isValidIP(self,s):
        ip = int(s)

        if len(s)!=len(str(ip)): # if length of s is not equal to length of ip address then return false
            return False

        if ip<0 or ip>255: # if ip address is less than 0 or greater than 255 then return false
            return False
        return True # else return true

