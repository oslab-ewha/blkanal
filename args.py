import sys
import getopt

readonly = False
writeonly = False
plotting_mode = False
display_difflba = False
pidonly = -1
n_lookbacks = 1
ts_start = 0
ts_end = 10000000

def parse_ts_range(range):
    global      ts_start, ts_end

    if not '-' in range:
        ts_start = float(range)
    else:
        start, end = range.split(sep='-', maxsplit=1)
        ts_start = float(start)
        ts_end = float(end)

def parseArgs():
    global      path, readonly, writeonly, plotting_mode, display_difflba, pidonly, n_lookbacks

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:RWpP:Db:T:")
    except getopt.GetoptError:
        return False

    for o, a in opts:
        if o == '-h':
            usage()
            exit(1)
        if o == '-R':
            readonly = True
        elif o == '-W':
            writeonly = True
        elif o == '-p':
            plotting_mode = True
        elif o == '-b':
            n_lookbacks = int(a)
        elif o == '-D':
            display_difflba = True
        elif o == '-P':
            pidonly = int(a)
        elif o == '-T':
            parse_ts_range(a)

    if len(args) < 1:
        return False

    path = args[0]
    return True
