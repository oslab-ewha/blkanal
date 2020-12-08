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

        acchist = AccessHist(conf.ts_unit)
        acchist_score = AccessHist(conf.ts_unit * conf.grid_nx)

        ts_start = int(accesses[0].ts / conf.ts_unit) * conf.ts_unit
        ts_end = ts_start + conf.ts_unit
        bmp_col = AccBmpCol(self.lbamax, conf.grid_ny)
        bmp_col_score = AccBmpCol(self.lbamax, conf.grid_ny)

        for acc in accesses:
            accbit = acchist.append(acc)
            accbit_score = acchist_score.append(acc)
            while acc.ts >= ts_end:
                ts_start = ts_end
                ts_end += conf.ts_unit
                self.__bmp_cols.append(bmp_col)
                self.__bmp_cols_score.append(bmp_col_score)
                bmp_col = AccBmpCol(self.lbamax, conf.grid_ny)
                bmp_col_score = AccBmpCol(self.lbamax, conf.grid_ny)
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
            if self.__index >= len(self.__bmp_cols) - conf.grid_nx:
                raise StopIteration

            acc_bmp = AccBmp(conf.grid_nx, conf.grid_ny)
            acc_bmp_score = AccBmp(conf.grid_nx, conf.grid_ny)
            for i in range(self.__index, self.__index + conf.grid_nx):
                if i < len(self.__bmp_cols):
                    acc_bmp.append(self.__bmp_cols[i])
                    acc_bmp_score.append(self.__bmp_cols_score[i])
                else:
                    acc_bmp.append(None)
                    acc_bmp_score.append(None)
            self.__index += 1
            if acc_bmp.is_valid():
                idx_forward = self.__index + conf.grid_nx - 1
                acc_bmp_score.bmpcol_forwards = self.__bmp_cols_score[idx_forward:idx_forward + conf.n_forwards - 1]
                acc_bmp_score.calcScore()
                if acc_bmp_score.score.counts[0] + acc_bmp_score.score.counts[1] > 0:
                    acc_bmp.score = acc_bmp_score.score
                    return acc_bmp
