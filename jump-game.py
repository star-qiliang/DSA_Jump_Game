class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        i = 0
        while True:
            for j in range(i+1, i+nums[i]+1):
                # print("j:", j)
                if j<len_nums:
                    if j+nums[j]>=i+nums[i]:
                        i=j
                        break
            
            # print("i:", i)
            # print()

            if i+nums[i]>=len_nums-1:
                return True

            if nums[i]==0:
                return False

            if j>=len_nums:
                return False


        