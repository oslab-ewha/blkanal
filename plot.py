import matplotlib.pyplot as plt
import conf

def plot(ta):
    global      __ax

    fig, __ax = plt.subplots()
    __ax.set_xlabel('Time(sec)', fontweight = 'bold')
    if conf.lba_start != 0 or conf.lba_end != -1:
        plt.ylim([conf.lba_start, conf.lba_end])
    elif conf.ts_unit > 0 and conf.grid_ny > 0:
        plt.xlim([-0.1, conf.grid_nx + 0.1])
        plt.ylim([-0.1, conf.grid_ny + 0.1])
    if not conf.display_difflba:
        plot_access(ta)
    else:
        plot_difflba(ta)

    __ax.legend()
    plt.show()

def __scatter(x, y, n, is_read):
    if is_read:
        color = 'red'
        fin_color='coral'
        label = 'read'
    else:
        color = 'blue'
        fin_color='purple'
        label = 'write'
    if conf.nblks_plotting_mode:
    	length=[y[i]+n[i]-1 for i in range(len(y))]
    	plt.scatter(x, y, c = color, label = label+' (start point)')
    	plt.scatter(x, length, c = fin_color, label=label+' (end point)')
    else:
    	plt.scatter(x, y, c = color, label = label)
    
def __plot_normalized_access(ta):
    xr = []
    yr = []
    xw = []
    yw = []
    ts_start = ta.accesses[0].ts
    if conf.ts_unit <= 0:
        ts_range = ta.accesses[-1].ts - ts_start
    else:
        ts_range = conf.ts_unit * conf.grid_nx
    if conf.lba_max == 0:
        lba_range = ta.lba_max - ta.lba_min
    else:
        lba_range = conf.lba_max

    for acc in ta.accesses:
        if lba_range == 0:
            continue
        if acc.ts >= ts_start + ts_range:
            break
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
    yrb= []
    xw = []
    yw = []
    ywb= []
    for acc in ta.accesses:
        if acc.is_read:
            xr.append(acc.timestamp)
            yr.append(acc.lba)
            yrb.append(acc.nblks)
        else:
            xw.append(acc.timestamp)
            yw.append(acc.lba)
            ywb.append(acc.nblks)
    __scatter(xr, yr, yrb, True)
    __scatter(xw, yw, ywb, False)

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
