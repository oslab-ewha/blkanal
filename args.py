import sys
import getopt

readonly = False
writeonly = False
plotting_mode = False
pidonly = -1

def parseArgs():
    global      path, readonly, writeonly, plotting_mode, pidonly

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:RWpP:")
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
        elif o == '-P':
            pidonly = int(a)

    if len(args) < 1:
        return False

    path = args[0]
    return True
