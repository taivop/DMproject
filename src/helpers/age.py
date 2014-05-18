


class Age():

    binEdges = [20,30,40,50,60,70,80]
    maxAge = 115

    agesToBins = None
    binsToAges = None

    def __init__(self):
        self.agesToBins = dict()
        self.binsToAges = dict()
        self.makeAgeBins()


    def getBinFromAge(self, age):
        return self.agesToBins[age]

    def getAgeRangeFromBin(self, bin):
        return self.binsToAges[bin]

    def makeAgeBins(self):
        for i in range(0,116):
            if i < 20:
                self.agesToBins[i] = 0
            elif i >= 80:
                self.agesToBins[i] = 6
            else:
                self.agesToBins[i] = (i // 10) - 1

        for i in range(0, len(self.binEdges)):
            e = self.binEdges
            if i == 0:
                s = "[0,{0})".format(e[0])
            elif i == len(self.binEdges) - 1:
                s = "[{0},{1}]".format(e[i], self.maxAge)
            else:
                s = "[{0},{1})".format(e[i], e[i+1])

            self.binsToAges[i] = s