class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                return [dict[diff],i]
            else:
                dict[nums[i]] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]