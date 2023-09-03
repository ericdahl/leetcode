class Twitter:

    def __init__(self):
        self.seq_id = 1
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.seq_id, tweetId))
        self.seq_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        # build up list of 10 most recent tweets from all following + self
        # not memory efficient at all
        # better to use a heapq ?
        s = []
        s += self.tweets[userId][-10:]
        for f in self.following[userId]:
            s += self.tweets[f][-10:]

        s.sort()
        return [t[1] for t in s[-10:]][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)