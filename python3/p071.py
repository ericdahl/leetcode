class Solution:
    def simplifyPath(self, path: str) -> str:

        path = [ part for part in path.split("/") if part ]

        new_parts = []
        num_double_dots = 0

        for part in reversed(path):

            if part == ".":
                continue

            if part == "..":
                num_double_dots += 1
                continue

            if num_double_dots > 0:
                num_double_dots -= 1
                continue

            new_parts.insert(0, part)

        return "/" + "/".join(new_parts)
