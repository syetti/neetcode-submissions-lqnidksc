class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_table = {}
        t_freq_table = {}

        for char in s:
            if char in s_freq_table:
                s_freq_table[char] += 1
            else:
                s_freq_table[char] = 0
            
        for char in t:
            if char in t_freq_table:
                t_freq_table[char] += 1
            else:
                t_freq_table[char] = 0
            
        if s_freq_table == t_freq_table:
            return True
        else:
            return False
        