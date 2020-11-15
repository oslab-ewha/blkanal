from accbmpcol import AccBmpCol
from accbmp import AccBmp
from acchist import AccessHist
import conf

class AccBmpBar:
    def __init__(self, lba_max, accesses):
        if conf.lba_max == 0:
            self.lbamax = lba_max
        else:
            self.lbamax = conf.lba_max
        self.__bmp_cols = []
        self.__bmp_cols_score = []
        self.__build(accesses)

    def __build(self, accesses):
        if len(accesses) == 0:
            return

        acchist = AccessHist(conf.ts_intv)
        acchist_score = AccessHist(conf.ts_intv * conf.width)

        ts_start = int(accesses[0].ts / conf.ts_intv) * conf.ts_intv
        ts_end = ts_start + conf.ts_intv
        bmp_col = AccBmpCol(self.lbamax, conf.height)
        bmp_col_score = AccBmpCol(self.lbamax, conf.height)

        for acc in accesses:
            accbit = acchist.append(acc)
            accbit_score = acchist_score.append(acc)
            while acc.ts >= ts_end:
                ts_start = ts_end
                ts_end += conf.ts_intv
                self.__bmp_cols.append(bmp_col)
                self.__bmp_cols_score.append(bmp_col_score)
                bmp_col = AccBmpCol(self.lbamax, conf.height)
                bmp_col_score = AccBmpCol(self.lbamax, conf.height)
            bmp_col.setBitByLba(acc.lba, accbit)
            bmp_col_score.setBitByLba(acc.lba, accbit_score)

        if not bmp_col.is_empty:
            self.__bmp_cols.append(bmp_col)
            self.__bmp_cols_score.append(bmp_col_score)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        while True:
            if self.__index >= len(self.__bmp_cols) - conf.width:
                raise StopIteration

            acc_bmp = AccBmp(conf.width, conf.height)
            acc_bmp_score = AccBmp(conf.width, conf.height)
            for i in range(self.__index, self.__index + conf.width):
                if i < len(self.__bmp_cols):
                    acc_bmp.append(self.__bmp_cols[i])
                    acc_bmp_score.append(self.__bmp_cols_score[i])
                else:
                    acc_bmp.append(None)
                    acc_bmp_score.append(None)
            self.__index += 1
            if acc_bmp.is_valid():
                idx_forward = self.__index + conf.width - 1
                acc_bmp_score.bmpcol_forwards = self.__bmp_cols_score[idx_forward:idx_forward + conf.n_forwards - 1]
                acc_bmp_score.calcScore()
                if acc_bmp_score.score.count > 0:
                    acc_bmp.score = acc_bmp_score.score
                    return acc_bmp
