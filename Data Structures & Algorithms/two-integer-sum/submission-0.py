class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        n=len(nums)
        for i in range(0,n):
            required = target - nums[i]
            if required in freq:
                return [freq[required],i]
            freq[nums[i]]=i



            

        