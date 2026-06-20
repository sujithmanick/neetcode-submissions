from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self._follow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self._follow[userId].add(userId)

        for user in self._follow[userId]:
            if user in self.tweets:
                _index = len(self.tweets[user]) - 1
                time, tweetid = self.tweets[user][_index][0], self.tweets[user][_index][1]
                heapq.heappush(min_heap, [time, tweetid, user, _index -1])

        while min_heap and len(res) < 10:
            time, tweetid, user, _index = heapq.heappop(min_heap)
            res.append(tweetid)

            if _index >= 0:
                time, tweetid = self.tweets[user][_index][0], self.tweets[user][_index][1]
                heapq.heappush(min_heap, [time, tweetid, user, _index-1])

        return res



        
       
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self._follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._follow[followerId].discard(followeeId)