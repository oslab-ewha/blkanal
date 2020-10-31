import matplotlib.pyplot as plt

def scatter(acc, color):
    marker = ([ (-1, 0), (1, 0), (1, acc.nblks), (-1, acc.nblks) ], 0)
    plt.scatter(acc.timestamp, acc.lba, marker = marker, c = color)

def plot(ta, args):
    if not args.display_difflba:
        plot_access(ta, args)
    else:
        plot_difflba(ta, args)

    plt.show()

def plot_access(ta, args):
    for acc in ta.accesses:
        if args.pidonly >= 0:
            if args.pidonly != acc.pid:
                continue

        if acc.is_read:
            if not args.writeonly:
                scatter(acc, 'red')
        else:
            if not args.readonly:
                scatter(acc, 'blue')

def plot_difflba(ta, args):
    xr = []
    yr = []
    xw = []
    yw = []
    for acc in ta.accesses:
        if acc.is_read:
            xr.append(acc.timestamp)
            yr.append(acc.diff_lba)
        else:
            xw.append(acc.timestamp)
            yw.append(acc.diff_lba)

    if not args.writeonly:
        plt.plot(xr, yr, c='red', marker='x')
    if not args.readonly:
        plt.plot(xw, yw, c='blue', marker='x')
