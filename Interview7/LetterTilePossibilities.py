class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cur = set(['']) # craeting a set
        for tile in tiles: # for every tile in tiles assign the copied value of cur to next_cur
            next_cur = cur.copy()
            for word in cur: # for every word in cur run the loop until the length of word
                for j in range(len(word)+1):
                    next_cur.add(word[:j]+ tile +word[j:]) # add the formulated string in the next_cur set
            cur = next_cur # assign the cur_next to cur
        return len(cur)-1 # returning the length of cur