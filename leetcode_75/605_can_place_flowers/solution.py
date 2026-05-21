class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # complex solve
        # results = {}
        # for candy in candies:
        #     results[candy] = False
        # sorted_candies = sorted(candies)
        # for candy in sorted_candies:
        #     # check greatest
        #     if candy + extraCandies >= sorted_candies[-1]:
        #         results[candy] = True
        # easy, O(n)
        max_candy = max(candies)
        return [candy + extraCandies >= max_candy for candy in candies]