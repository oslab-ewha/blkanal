from accbmpcol import AccBmpCol
from accbmp import AccBmp
from acchist import AccessHist

class AccBmpBar:
    def __init__(self, conf, accesses):
        self.ts_intv = conf.ts_intv
        self.lbamax = conf.lba_max
        self.width = conf.width
        self.height = conf.height

        self.__bmp_cols = []
        self.__build(accesses)

    def __build(self, accesses):
        if len(accesses) == 0:
            return

        acchist = AccessHist(self.ts_intv * self.width)

        ts_start = int(accesses[0].ts / self.ts_intv) * self.ts_intv
        ts_end = ts_start + self.ts_intv
        bmp_col = AccBmpCol(self.lbamax, self.height)
        
        for acc in accesses:
            accbit = acchist.append(acc)
            while acc.ts >= ts_end:
                ts_start = ts_end
                ts_end += self.ts_intv
                self.__bmp_cols.append(bmp_col)
                bmp_col = AccBmpCol(self.lbamax, self.height)
            bmp_col.setBitByLba(acc.lba, accbit)

        if not bmp_col.is_empty:
            self.__bmp_cols.append(bmp_col)

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
                acc_bmp.bmpcol_score = self.__bmp_cols[self.__index + self.width - 1]
                acc_bmp.score = acc_bmp.bmpcol_score.score
                if acc_bmp.score.count > 0:
                    return acc_bmp
