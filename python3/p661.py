class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def avg(img: List[List[int]], r: int, c: int) -> int:
            total = 0
            items = 0
            for r_i in range(max(0, r - 1), min(r + 2, len(img))):
                for c_i in range(max(0, c - 1), min(c + 2, len(img[0]))):
                    total += img[r_i][c_i]
                    items += 1
            return total // items

        result_img = [[None] * len(img[0]) for r in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[0])):
                result_img[r][c] = avg(img, r, c)

        return result_img