class Arc:
    def __init__(self, _s_line):
        self.__init = 0
        self.__value = 0
        self.__fin = 0

        self.create_arc(_s_line)

    def create_arc(self, _s_line):
        """Création de l'arc"""
        s_line = _s_line
        s_line = s_line.split(' ')
        try:
            self.__init = int(s_line[0])
            self.__fin = int(s_line[1])
            self.__value = int(s_line[2])
        except (IndexError, ValueError):
            raise Exception("Erreur dans l'arc")

    @property
    def init(self):
        """Getter de __init"""
        return self.__init

    @property
    def value(self):
        """Getter de __value"""
        return self.__value

    @value.setter
    def value(self, arg):
        """Setter de __value"""
        self.__value = arg

    @property
    def fin(self):
        """Getter de __fin  """
        return self.__fin


