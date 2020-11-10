from accbmpcol import AccBmpCol

class AccBmp:
    def __init__(self, width, height):
        self.is_empty = True
        self.width = width
        self.height = height
        self.acc_bmp = []
        self.score = None

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

    def bitmap(self):
        bmp = []
        for c in self.acc_bmp:
            bmp += c.bitmap()
        return bmp

    def __str__(self):
        s = self.__str_bar()
        for r in range(0, self.height):
            s += '|'
            for c in range(0, self.width):
                s += str(self.acc_bmp[c].bmp_col[r])
            s += '|'
            if not self.bmpcol_score is None:
                s += str(self.bmpcol_score.bmp_col[r])
            s += '\n'
        s += self.__str_bar()
        return s

    def __str_bar(self):
        s = '+'
        for c in range(0, self.width):
            s += '-'
        return s + "+\n"
