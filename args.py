import sys
import getopt

readonly = False
writeonly = False

def parseArgs():
    global      path, readonly, writeonly

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:RW")
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

    if len(args) < 1:
        return False

    path = args[0]
    return True
