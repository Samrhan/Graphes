class Graph:
    def __init__(self, _num_graph):
        self.num_graph = _num_graph
        self.file_name = f"graphes/{self.num_graph}.txt"

        # Propriétés du graphe
        self.n_sommets = 0
        self.n_arcs = 0

        self.read_file()

    def read_file(self):
        with open(self.file_name) as file:
            line = file.readline()
            n = 0
            while line:
                if n == 0:
                    try:
                        self.n_sommets = int(line)
                    except ValueError:
                        print("Erreur à la première ligne")
                if n == 1:
                    try:
                        self.n_arcs = int(line)
                    except ValueError:
                        print("Erreur à la deuxième ligne")

                line = file.readline()
                n += 1
