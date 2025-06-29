from typing import List

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        temp_set = set()
        for i in nums:
            if i in temp_set:
                return True
            else:
                temp_list.add(i)
        return False
