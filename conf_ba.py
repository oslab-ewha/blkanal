from conf import Conf

class ConfBlkAnal(Conf):
    def __init__(self, usage):
        self.plotting_mode = False
        self.display_difflba = False
        self.grid_nx = 0
        self.grid_ny = 0

        super().__init__('pG:D', usage)

    def handleOpt(self, o, a):
        if o == '-p':
            self.plotting_mode = True
        elif o == '-D':
            self.display_difflba = True
        elif o == '-G':
            self.__parse_scatter_dim(a)

    def __parse_scatter_dim(self, dim):
        if ':' in dim:
            nx, ny = dim.split(sep=':', maxsplit=1)
            self.grid_nx = int(nx)
            self.grid_ny = int(ny)
