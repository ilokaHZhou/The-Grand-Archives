class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        hashmap = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if (difference in hashmap.keys()):
                return [hashmap[difference], index]
            hashmap[nums[index]] = index
        return []


print(Solution.twoSum(Solution,[2,7,11,15], 9))