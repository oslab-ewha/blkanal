import csv
import logger

class TraceData:
    def __init__(self):
        self.lines = 0

    def load(self, path):
        try:
            f = open(path, "r")
        except IOError:
            logger.error("csv file not found: {}".format(path))
            return False

        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if row[3] == 'I':
                self.lines += 1
                self.parseLine(row)

        return True

    def parseLine(self, row):
        pass
