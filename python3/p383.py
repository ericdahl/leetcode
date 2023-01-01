class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        ransom_counter = Counter(ransomNote)

        magazine_counter.subtract(ransom_counter)

        return min(magazine_counter.values()) >= 0