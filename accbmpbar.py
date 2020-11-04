from accbmpcol import AccBmpCol
from accbmp import AccBmp
from acchit import AccessHit

class AccBmpBar:
    def __init__(self, accesses, ts_intv, lbamax, width, height):
        self.ts_intv = ts_intv
        self.lbamax = lbamax
        self.width = width
        self.height = height

        self.__bmp_cols = []
        self.__build(accesses)

    def __build(self, accesses):
        if len(accesses) == 0:
            return

        acchit = AccessHit(self.ts_intv * self.width)

        ts_start = int(accesses[0].ts / self.ts_intv) * self.ts_intv
        ts_end = ts_start + self.ts_intv
        bmp_col = AccBmpCol(self.lbamax, self.height)
        
        for acc in accesses:
            is_hit = acchit.is_hit(acc)
            acchit.append(acc)
            while acc.ts >= ts_end:
                ts_start = ts_end
                ts_end += self.ts_intv
                self.__bmp_cols.append(bmp_col)
                bmp_col = AccBmpCol(self.lbamax, self.height)
            bmp_col.setLba(acc.lba, acc.is_read, is_hit)

        if not bmp_col.is_empty:
            self.__bmp_cols.append(bmp_col)

    def __get_seq_score(self):
        pass

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        while True:
            if self.__index >= len(self.__bmp_cols) - self.width:
                raise StopIteration

            acc_bmp = AccBmp(self.width, self.height)
            for i in range(self.__index, self.__index + self.width):
                if i < len(self.__bmp_cols):
                    acc_bmp.append(self.__bmp_cols[i])
                else:
                    acc_bmp.append(None)

            self.__index += 1
            if acc_bmp.is_valid():
                score = acc_bmp.getSeqScore(self.__bmp_cols[self.__index - 1 + self.width])
                return score, acc_bmp
