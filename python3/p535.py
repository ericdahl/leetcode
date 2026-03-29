class Codec:

    def __init__(self):
        self.d = {}
        self.i = 0

    @staticmethod
    def _generate():
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))

    def _generateNew(self):
        tiny = Codec._generate()
        while tiny in self.d:
            tiny = self._generate()
        return f"https://tinyurl.com/{tiny}"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny = self._generateNew()
        self.d[tiny] = longUrl
        return tiny


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))