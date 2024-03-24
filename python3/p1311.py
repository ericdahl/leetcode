class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        seen = set([id])
        targets = set([id])
        while level > 0:
            next_targets = set()
            for target in targets:
                next_targets |= (set(friends[target]) - seen)

            targets = next_targets
            seen |= targets
            level -= 1

        targets_watched = Counter()
        for target in targets:
            for video in watchedVideos[target]:
                targets_watched[video] += 1

        # sort by frequency then name
        s = list(targets_watched.items())
        s.sort(key = lambda x: (x[1], x[0]))
        return [v[0] for v in s]
