class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCatcher = set()
        for num in nums:
            if num in dupCatcher:
                return True
            dupCatcher.add(num)
        return False
