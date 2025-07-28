class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Start with the first list as a set
        common = set(nums[0])
        
        # Intersect with each remaining list
        for lst in nums[1:]:
            common &= set(lst)
        
        # Return the sorted list of common elements
        return sorted(common)

        