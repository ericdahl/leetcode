class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = Counter(digits)
        result = []

        for d1 in range(1, 10):
            if d1 not in c:
                continue
            for d2 in range(0, 10):
                if d2 not in c:
                    continue
                for d3 in range(0, 10, 2):
                    if d3 not in c:
                        continue

                    c2 = Counter([d1,d2,d3])
                    if c2 & c == c2:
                        result.append(d1 * 100 + d2 * 10 + d3)
        return result




        
