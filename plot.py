import matplotlib.pyplot as plt

def plot(ta, conf):
    if not conf.display_difflba:
        plot_access(ta, conf)
    else:
        plot_difflba(ta, conf)

    plt.show()

def __plot_normalized_access(ta, conf):
    ts_start = ta.accesses[0].ts
    ts_range = ta.accesses[-1].ts - ts_start
    lba_range = ta.lba_max - ta.lba_min
    for acc in ta.accesses:
        x = int((acc.ts - ts_start) / ts_range * conf.grid_nx)
        y = int((acc.lba - ta.lba_min) / lba_range * conf.grid_ny)
        if acc.is_read:
            color = 'red'
        else:
            color = 'blue'
        plt.scatter(x, y, c = color)

def __plot_access(ta, conf):
    xr = []
    yr = []
    xw = []
    yw = []
    for acc in ta.accesses:
        if acc.is_read:
            xr.append(acc.timestamp)
            yr.append(acc.lba)
        else:
            xw.append(acc.timestamp)
            yw.append(acc.lba)
    plt.scatter(xr, yr, c = 'red')
    plt.scatter(xw, yw, c = 'blue')

def plot_access(ta, conf):
    if conf.grid_nx > 0:
        __plot_normalized_access(ta, conf)
    else:
        __plot_access(ta, conf)

def plot_difflba(ta, conf):
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

    if not conf.writeonly:
        plt.plot(xr, yr, c='red', marker='x')
    if not conf.readonly:
        plt.plot(xw, yw, c='blue', marker='x')
