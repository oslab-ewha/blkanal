import conf

class ConfBlkAnal(conf.Conf):
    def __init__(self, usage):
        conf.plotting_mode = False
        conf.display_difflba = False
        conf.nblks_plotting_mode=False
        conf.grid_nx = 0
        conf.grid_ny = 0
        conf.ts_unit = -1

        super().__init__('pDzr', usage)

    def handleOpt(self, o, a):
        if o == '-p':
            conf.plotting_mode = True
        elif o == '-D':
            conf.display_difflba = True
        elif o == '-r':
            conf.nblks_plotting_mode=True
            conf.plotting_mode = True
