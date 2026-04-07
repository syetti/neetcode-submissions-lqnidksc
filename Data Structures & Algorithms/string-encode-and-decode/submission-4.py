class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "!" + string   
            print(encoded)
        return encoded
        

    def decode(self, s: str) -> List[str]:
        last = 0
        decoded = []

        while last < len(s):
            first = last
            while s[first] != "!":
                first += 1
            length = int(s[last:first])
            decoded.append(s[first +1 : first +1 +length])
            last = first + 1 + length

        return decoded 
        

        
       
