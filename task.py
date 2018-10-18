import random


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getTimeStamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp