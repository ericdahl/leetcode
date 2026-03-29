class Codec:

    def __init__(self):
        self.d = {}

    @staticmethod
    def _generate():
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))

    def _generateNew(self):
        tiny = Codec._generate()
        while tiny in self.d:
            tiny = self._generate()
        return tiny

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # no dedup here; users should have privacy in this enterprise solution
        tiny = self._generateNew()
        self.d[tiny] = longUrl
        return f"https://tinyurl.com/{tiny}"


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        tiny = shortUrl.removeprefix("https://tinyurl.com/")
        return self.d[tiny]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))