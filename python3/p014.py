class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        first_word = strs[0]

        for index in range(len(first_word)):
            for current_word in strs[1:]:

                if index + 1 > len(current_word):
                    return longest

                if current_word[index] != first_word[index]:
                    return longest

            longest += first_word[index]

        return longest