class Meter:
    def __init__(self, name):
        self.n = name
        self.l = 5

    def checkMeter(self):
        return self.l

    def add(self):
        if (self.checkMeter() < 5):
            self.l += 1

    def deplete(self):
        if (self.checkMeter() > 0):
            self.l -= 1
            
    def print(self):
        meter = self.n + ": "
        
        i = 0
        while (i < self.l):
            meter += "▮"
            i += 1
            
        return meter
