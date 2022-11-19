class Solution:
    def findComplement(self, num: int) -> int:
        m = {
            '1': '0',
            '0': '1'
        }
        bstr = bin(num)[2:]
        complement_str = ''.join([m[c] for c in bstr])
        return int(complement_str, 2)

