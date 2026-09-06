class Solution:
    def isValid(self, s: str) -> bool:
        isValid = {")" : "(" , "]" : "[" , "}" : "{"}
        records = []

        for char in s:
            if char in isValid:
                if records and isValid[char] == records[-1] :
                    records.pop()
                else:
                    return False
            else:
                records.append(char)
        
        return not records