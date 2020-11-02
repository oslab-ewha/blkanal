import matplotlib.pyplot as plt

def plot(ta, args):
    if not args.display_difflba:
        plot_access(ta, args)
    else:
        plot_difflba(ta, args)

    plt.show()

def __plot_normalized_access(ta, args):
    ts_start = ta.accesses[0].ts
    ts_range = ta.accesses[-1].ts - ts_start
    lba_range = ta.lba_max - ta.lba_min
    for acc in ta.accesses:
        x = int((acc.ts - ts_start) / ts_range * args.grid_nx)
        y = int((acc.lba - ta.lba_min) / lba_range * args.grid_ny)
        if acc.is_read:
            color = 'red'
        else:
            color = 'blue'
        plt.scatter(x, y, c = color)

def __plot_access(ta, args):
    for acc in ta.accesses:
        if acc.is_read:
            color = 'red'
        else:
            color = 'blue'
        marker = ([ (-1, 0), (1, 0), (1, acc.nblks), (-1, acc.nblks) ], 0)
        plt.scatter(acc.timestamp, acc.lba, marker = marker, c = color)

def plot_access(ta, args):
    if args.grid_nx > 0:
        __plot_normalized_access(ta, args)
    else:
        __plot_access(ta, args)

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
