class Twitter:

    def __init__(self):
        self.users: dict = defaultdict(set)
        self.tweets: dict = defaultdict(list)
        self.time: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.getTweets(userId)[:]

        followers = self.users[userId]

        for follower in followers:
            followerTweets = self.getTweets(follower)
            for tweet in followerTweets:
                tweets.append(tweet)
        tweets.sort(key=lambda tweet: -tweet[1])

        return [tweetId for tweetId, _ in tweets[:10]]

    def getTweets(self, userId: int) -> List[int]:
        tweets = []
        for tweet in self.tweets[userId]:
            tweets.append(tweet)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.users and followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)
