class Arc:
    def __init__(self, _s_line):
        self.__init = 0
        self.__arc = 0
        self.__fin = 0

        self.create_arc(_s_line)

    def create_arc(self, _s_line):
        s_line = _s_line
        s_line = s_line.split(' ')

        try:
            self.__init = s_line[0]
            self.__arc = s_line[1]
            self.__fin = s_line[2]
        except IndexError:
            raise Exception("Erreur dans l'arc")

    @property
    def init(self):
        return self.__init

    @property
    def arc(self):
        return self.__arc

    @arc.setter
    def arc(self, arg):
        self.__arc = arg

    @property
    def fin(self):
        return self.__fin


