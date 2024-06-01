class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(list)

        # track each index by num value
        for i, n in enumerate(nums):
            d[n].append(i)

        count = 0
        for n in d:
            # could use nested for loop here, but combinations is cleaner and doesn't
            # require conditional extra logic
            for (x, y) in itertools.combinations(d[n], 2):
                if x * y % k == 0:
                    count += 1

        return count

            
