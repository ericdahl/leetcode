class Solution:
    def compressedString(self, word: str) -> str:

        operations = []

        for c, g in groupby(word):
            c_len = sum(1 for _ in g) # count length of repeats

            while c_len > 9:
                operations += f"9{c}"
                c_len -= 9
            operations.append(f"{c_len}{c}")

        return "".join(operations)

