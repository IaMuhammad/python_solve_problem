import itertools


class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        return itertools.chain.from_iterable(([nums[i + 1]] * nums[i]) for i in range(0, len(nums), 2))