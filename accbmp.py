from accbmpcol import AccBmpCol
from accbit import AccBit

class AccBmp:
    def __init__(self, width, height):
        self.is_empty = True
        self.width = width
        self.height = height
        self.acc_bmp = []

    def append(self, bmp_col):
        if bmp_col is None:
            bmp_col = AccBmpCol(0, self.height)
        else:
            if not bmp_col.is_empty:
                self.is_empty = False

        self.acc_bmp.append(bmp_col)

    def is_valid(self):
        if self.is_empty:
            return False
        if self.acc_bmp[-1].is_empty:
            return False
        return True

    def getSeqScore(self, bmp_col):
        return self.acc_bmp[-1].getSeqScore(bmp_col)

    def bitmap(self):
        bmp = []
        for c in self.acc_bmp:
            bmp += c.bmp_col
        return bmp

    def __str__(self):
        s = self.__str_bar()
        for r in range(0, self.height):
            s += '|'
            for c in range(0, self.width):
                bitval = self.acc_bmp[c].bmp_col[r]
                if bitval > 0:
                    s += str(AccBit(bitval))
                else:
                    s += ' '
            s += '|\n'
        s += self.__str_bar()
        return s

    def __str_bar(self):
        s = '+'
        for c in range(0, self.width):
            s += '-'
        return s + "+\n"
