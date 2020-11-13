import conf

class ConfBlkAnal(conf.Conf):
    def __init__(self, usage):
        conf.plotting_mode = False
        conf.display_difflba = False
        conf.grid_nx = 0
        conf.grid_ny = 0

        super().__init__('pG:D', usage)

    def handleOpt(self, o, a):
        if o == '-p':
            conf.plotting_mode = True
        elif o == '-D':
            conf.display_difflba = True
        elif o == '-G':
            self.__parse_scatter_dim(a)

    def __parse_scatter_dim(self, dim):
        if ':' in dim:
            nx, ny = dim.split(sep=':', maxsplit=1)
            conf.grid_nx = int(nx)
            conf.grid_ny = int(ny)
