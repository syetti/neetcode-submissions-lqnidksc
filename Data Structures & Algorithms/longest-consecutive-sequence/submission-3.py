class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = 1
        numsSet = set(nums)
        if nums == []:
            return 0
        for num in nums:
            temp_num_m = num -1
            temp_num_p = num + 1
            if temp_num_m not in numsSet:
                temp_seq=1
                print("seq:", temp_seq)
                   
                while temp_num_p in numsSet:
                    print("next_num: +", temp_num_p)
                    temp_seq+=1
                    print("seq:", temp_seq)
                    temp_num_p += 1

                    if temp_seq > seq:
                        seq  = temp_seq
        return seq