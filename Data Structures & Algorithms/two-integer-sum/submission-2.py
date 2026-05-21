class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in a:
                return [a[diff],i]
            else:
                a[nums[i]]=i
        

        