class Solution:

    @staticmethod
    def cmp_custom(x: str, y: str) -> str:
        xy = x + y
        yx = y + x
        return (xy > yx) - (xy < yx)

    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(n) for n in nums]
        str_nums = sorted(str_nums, key=cmp_to_key(Solution.cmp_custom), reverse=True)

        result =  "".join(str_nums)
        if result[0] == "0" :
            return "0"
        return result