class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if flowerbed == [0]:
            flowerbed[0] = 1
            n -= 1

        if flowerbed[:2] == [0, 0]:
            flowerbed[0] = 1
            n -= 1

        if flowerbed[-2:] == [0, 0]:
            flowerbed[-1] = 1
            n -= 1

        (a,b,c) = (0,1,2)

        while c < len(flowerbed):

            if flowerbed[a:c+1] == [0,0,0]:
                flowerbed[b] = 1
                n -= 1

            a += 1
            b += 1
            c += 1

        return n <= 0
