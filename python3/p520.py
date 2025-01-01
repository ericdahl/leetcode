class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1:
            return True

        first_cap = word[0].isupper()
        second_cap = word[1].isupper()

        if not first_cap and second_cap:
            return False

        all_lower = not first_cap and not second_cap
        all_upper = first_cap and second_cap
        title_case = first_cap and not second_cap

        for c in word[2:]:
            if c.isupper():
                if all_lower or title_case:
                    return False
            else: # lower
                if all_upper:
                    return False

        return True