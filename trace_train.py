import trace_access
import accbmpbar
import csv
import sys

class TraceTrain(trace_access.TraceAccess):
    def __init__(self, conf):
        super().__init__(conf)

    def gen_train_data(self, conf):
        if conf.lba_max == 0:
            conf.lba_max = self.lba_max
        if conf.path_out is None:
            outf = sys.stdout
        else:
            outf = open(conf.path_out, 'w')

        writer = csv.writer(outf, delimiter = ',')
        for ctx in self.contexts:
            accesses = self.__get_context_accesses(ctx)
            
            bmpbar = accbmpbar.AccBmpBar(accesses, conf.ts_intv, conf.lba_max, conf.width, conf.height)
            for score, accbmp in bmpbar:
                writer.writerow([score] + accbmp.bitmap())

    def __get_context_accesses(self, ctx):
        accesses = []
        for acc in self.accesses:
            if acc.context == ctx:
                accesses.append(acc)
        return accesses
