class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic = {}

        for char in s:
            sdic[char] = sdic.get(char , 0) + 1
        
        for char in t:
            tdic[char] = tdic.get(char , 0) + 1
        

        return sdic == tdic