class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        transformations = set()

        for word in words:
            transformations.add("".join([codes[ord(c) - ord('a')] for c in word]))
        
        return len(transformations)
