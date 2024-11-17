class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^a-zA-Z ]', ' ', paragraph).lower().split(" ")


        banned_set = set(banned)
        for w in Counter(words).most_common():

            if w[0] and w[0] not in banned_set:
                return w[0]
