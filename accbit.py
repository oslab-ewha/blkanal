class AccBit:
    def __init__(self, *args):
        if len(args) == 1:
            self.val = args[0]
        else:
            self.val = self.__getval(args[0], args[1])

    def __getval(self, is_read, is_hit):
        val = 0
        if is_read:
            val |= 1
            if is_hit:
                val |= 4
        else:
            val |= 2
            if is_hit:
                val |= 8
        return val

    def __str__(self):
        return hex(self.val).lstrip('0x')
