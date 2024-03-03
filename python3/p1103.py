class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        r = [0] * num_people
        i = 0
        incr = 1

        while candies > 0:
            r[i] += min(candies, incr)
            candies -= incr
            incr += 1
            i = (i + 1) % num_people

        return r
