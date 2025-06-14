class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def valid_continuation(d):
            return d >= 2**7 and d <= 2**7 + 2**6

        i = 0
        while i < len(data):
            d = data[i]
            if d < 2**7:
                i += 1
                continue

            d_bin = bin(d)[2:]
            print(f"d_bin={d_bin}")
            if d_bin.startswith('110'):
                if i > len(data) - 1 or  not valid_continuation(data[i + 1]):
                    return False
                i += 2
            elif d_bin.startswith('1110'):
                if i > len(data) - 2 or not valid_continuation(data[i + 1]) or not valid_continuation(data[i + 2]):
                    return False
                i += 3
            elif d_bin.startswith('11110'):
                if i > len(data) - 3 or not valid_continuation(data[i + 1]) or not valid_continuation(data[i + 2]) or not valid_continuation(data[i + 3]):
                    return False
                i += 4
            else:
                return False

        return True