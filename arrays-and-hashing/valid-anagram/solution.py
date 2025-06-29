from typing import List

class isAnagram(string_one: str, string_two: str ) -> bool:
    counting_one, counting_two = {}

    if len(string_one) != len(string_two):
        return False

    for i in string_one:
        counting_one[i] = 1 + counting_one.get(i,0)
        
    for i in string_two:
        counting_two[i] = 1 + counting_two.get(i,0)

    if counting_one == counting_two:
        return True
    else:
        return False
'''
we can also take advantage of class Counter from collections,
that do the same that we try to achieve above but works faster
'''
from collections import Counter
class isAnagramTwo(string_one: str, string_two: str ) -> bool:
    counting_one, counting_two = {}

    if Counter(string_one) == Counter(string_two):
        return True
    else:
        return False