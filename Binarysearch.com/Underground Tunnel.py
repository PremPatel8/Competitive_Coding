from collections import defaultdict

# Your code took 86 milliseconds — faster than 7.45% in Python
class UndergroundTunnel:

    def __init__(self):
        self.userTime = defaultdict(int)
        self.stationDict = defaultdict(lambda: defaultdict(set))

    def checkIn(self, userId, station, timestamp):
        self.userTime[userId] = timestamp
        currentCheckInstation = self.stationDict[station]
        # print(f"checkIn station before = {currentCheckInstation}")
        currentCheckInstation["checkin"].add(userId)
        # print(f"checkIn station after = {currentCheckInstation}")

    def checkOut(self, userId, station, timestamp):
        self.userTime[userId] = abs(timestamp-self.userTime[userId])
        currentCheckOutStation = self.stationDict[station]
        # print(f"checkOut station before = {currentCheckOutStation}")
        currentCheckOutStation["checkout"].add(userId)
        # print(f"checkOut station after = {currentCheckOutStation}")

    def averageTime(self, start, end):
        # print(f"self.stationDict = {self.stationDict}")
        # print(f"self.userTime = {self.userTime}")
        concernedUsers = self.stationDict[start]["checkin"].intersection(
            self.stationDict[end]["checkout"])

        totalTime = 0

        for user in concernedUsers:
            totalTime += self.userTime[user]

        return totalTime/len(concernedUsers)


# Your code took 57 milliseconds — faster than 53.19% in Python
class UndergroundTunnel:
    def __init__(self):
        self.users = {}
        self.stats = {}

    def checkIn(self, userId, station, timestamp):
        self.users[userId] = (station, timestamp)

    def checkOut(self, userId, station, timestamp):
        checkInStation, checkInTime = self.users[userId]
        travelTime = (timestamp - checkInTime)
        totalTime, userCnt = self.stats.get((checkInStation, station), (0, 0))
        self.stats[(checkInStation, station)] = (totalTime + travelTime, userCnt + 1)

    def averageTime(self, start, end):
        totalTime, userCnt = self.stats[(start, end)]
        return totalTime / userCnt