def calc():
    u = [1]

    for i in range(1, 31):
        for j in combinations_with_replacement([2,3,5], i):
            u.append(prod(j))

    u.sort()
    return u

try:
    u
except NameError:
    u = calc()


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return u[n - 1]
