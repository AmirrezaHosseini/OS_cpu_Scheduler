class task:
    def __init__(self, task, burstTime):
        self.task = task
        self.bursTime = burstTime

    def setState(self, state):
        self.state = state

    def getName(self):
        return self.task

    def getburstTime(self):
        return self.burstTime

    def setTask(self, task):
        self.task = task

    def setburstTime(self, time):
        self.bursTime = time

    def toString(self):
        return (f"task{self.task}")
