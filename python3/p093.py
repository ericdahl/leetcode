class Solution:

    @staticmethod
    def is_valid_digits(digits: List[str]):
        for d in digits:
            if len(d) > 1 and d[0] == "0":
                return False

            if int(d) > 255:
                return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:

        matches = []

        # loop through each possible combination of digit lengths
        # that make up an IP address. E.g., (1,1,1,1) for 4 single
        # digits, or up to (3,3,3,3) for 4 groups of 3 digits
        for dl in product(range(1, 4), repeat=4):

            if sum(dl) != len(s):
                continue

            digits = [0, 0, 0, 0]

            digits[0] = s[0 : sum(dl[0:1])]
            digits[1] = s[sum(dl[0:1]) : sum(dl[0:2])]
            digits[2] = s[sum(dl[0:2]) : sum(dl[0:3])]
            digits[3] = s[sum(dl[0:3]) : ]

            if Solution.is_valid_digits(digits):
                matches.append(".".join(digits))

        return matches

