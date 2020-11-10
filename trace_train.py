import trace_access
import accbmpbar
import csv
import sys

class TraceTrain(trace_access.TraceAccess):
    def __init__(self, conf):
        super().__init__(conf)
        self.conf = conf

    def gen_train_data(self):
        if self.conf.lba_max == 0:
            self.conf.lba_max = self.lba_max
        if self.conf.path_out is None:
            outf = sys.stdout
        else:
            outf = open(self.conf.path_out, 'w')
        if self.conf.no_csv:
            self.__write_as_human_readable(outf)
        else:
            self.__write_csv(outf)

    def __write_csv(self, outf):
        writer = csv.writer(outf, delimiter = ',')
        for ctx in self.contexts:
            accesses = self.__get_context_accesses(ctx)
            
            bmpbar = accbmpbar.AccBmpBar(self.conf, accesses)
            for accbmp in bmpbar:
                writer.writerow(accbmp.score.getScoreVec() + accbmp.bitmap())

    def __write_as_human_readable(self, outf):
        for ctx in self.contexts:
            accesses = self.__get_context_accesses(ctx)

            bmpbar = accbmpbar.AccBmpBar(self.conf, accesses)
            for accbmp in bmpbar:
                outf.write(str(accbmp.score))
                outf.write('\n')
                outf.write(str(accbmp))

    def __get_context_accesses(self, ctx):
        accesses = []
        for acc in self.accesses:
            if acc.context == ctx:
                accesses.append(acc)
        return accesses
