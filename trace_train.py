import trace_access
import accbmpbar
import csv
import sys
import conf

class TraceTrain(trace_access.TraceAccess):
    def gen_train_data(self):
        if conf.path_out is None:
            outf = sys.stdout
        else:
            outf = open(conf.path_out, 'a')
        if conf.no_csv:
            self.__write_as_human_readable(outf)
        else:
            self.__write_csv(outf)

    def __write_csv(self, outf):
        writer = csv.writer(outf, delimiter = ',')
        for ctx in self.contexts:
            accesses = self.__get_context_accesses(ctx)

            bmpbar = accbmpbar.AccBmpBar(self.lba_max, accesses)
            for accbmp in bmpbar:
                writer.writerow(accbmp.score.getScoreVec() + accbmp.bitmap())

    def __write_as_human_readable(self, outf):
        for ctx in self.contexts:
            accesses = self.__get_context_accesses(ctx)

            bmpbar = accbmpbar.AccBmpBar(self.lba_max, accesses)
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
