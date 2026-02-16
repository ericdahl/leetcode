class TweetCounts:

    FREQ_MAP = {"minute": 60, "hour": 60*60, "day": 60*60*24}
    def __init__(self):
        self.tweets = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        increment = TweetCounts.FREQ_MAP[freq]
        result = [0] * ((endTime - startTime) // increment + 1)
        tl = self.tweets[tweetName]
        for t in tl:
            if t < startTime:
                continue
            if t > endTime:
                break
            result[(t - startTime) // increment] += 1

        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)