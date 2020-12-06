import matplotlib.pyplot as plt
import conf

def plot(ta):
    global      __ax

    fig, __ax = plt.subplots()
    __ax.set_xlabel('Time(sec)', fontweight = 'bold')
    if conf.lba_start != 0 or conf.lba_end != -1:
        plt.ylim([conf.lba_start, conf.lba_end])
    if not conf.display_difflba:
        plot_access(ta)
    else:
        plot_difflba(ta)

    __ax.legend()
    plt.show()

def __scatter(x, y, is_read):
    if is_read:
        color = 'red'
        label = 'read'
    else:
        color = 'blue'
        label = 'write'
    plt.scatter(x, y, c = color, label = label)

def __plot_normalized_access(ta, conf):
    xr = []
    yr = []
    xw = []
    yw = []
    ts_start = ta.accesses[0].ts
    ts_range = ta.accesses[-1].ts - ts_start
    lba_range = ta.lba_max - ta.lba_min
    for acc in ta.accesses:
        x = int((acc.ts - ts_start) / ts_range * conf.grid_nx)
        y = int((acc.lba - ta.lba_min) / lba_range * conf.grid_ny)
        if acc.is_read:
            xr.append(x); yr.append(y)
        else:
            xw.append(x); yw.append(y)
    __scatter(xr, yr, True)
    __scatter(xw, yw, False)

def __plot_access(ta):
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
    __scatter(xr, yr, True)
    __scatter(xw, yw, False)

def plot_access(ta):
    global      __ax

    if conf.grid_nx > 0:
        __ax.set_ylabel('LBA(Normalized)', fontweight = 'bold')
        __plot_normalized_access(ta)
    else:
        __ax.set_ylabel('LBA', fontweight = 'bold')
        __plot_access(ta)

def __plot(x, y, is_read):
    if is_read:
        color = 'red'
        label = 'read'
    else:
        color = 'blue'
        label = 'write'
    plt.plot(x, y, c=color, marker='x', label = label)

def plot_difflba(ta):
    __ax.set_ylabel('LBA difference', fontweight = 'bold')
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
        __plot(xr, yr, True)
    if not conf.readonly:
        __plot(xw, yw, False)
