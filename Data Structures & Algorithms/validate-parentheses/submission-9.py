class Solution:
    def isValid(self, s: str) -> bool:
        
        l_chars = ["(", "[", "{"]
        r_chars = [")", "]", "}"]
        matching_chars = []
        
        if len(s) % 2 != 0 :
            return False

        for char in s:
            if char in l_chars:
                matching_chars.append(char)

            if char in r_chars:
                if len(matching_chars) == 0:
                    return False

            if char == "]":
                if "[" != matching_chars[-1]:
                    return False
                
                matching_chars.pop(-1)
            if char == "}":
                if "{" != matching_chars[-1]:
                    return False
                matching_chars.pop(-1)
            if char == ")":
                if "(" != matching_chars[-1]:
                    return False
                matching_chars.pop(-1)
             
            
        if len(matching_chars) == 0:
            return True
        return False
