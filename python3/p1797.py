class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and currentTime < self.tokens[tokenId]:
            self.tokens[tokenId] = currentTime + self.ttl


    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for expiration in self.tokens.values():
            if currentTime < expiration:
                c += 1
        return c



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)