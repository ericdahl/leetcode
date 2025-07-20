class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookies = len(s)
        satisfied_children = 0
        cookie_index = 0

        for child_requirement in g:
            while cookie_index < cookies:
                cookie_size = s[cookie_index]
                cookie_index += 1
                if cookie_size >= child_requirement:
                    satisfied_children += 1
                    break

        # kids should be happy with carrots
        return satisfied_children