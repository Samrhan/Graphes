from arc import Arc

class Graph:
    """Classe représentant un graphe"""

    def __init__(self, _num_graph):
        self.num_graph = _num_graph
        self.file_name = f"graphes/{self.num_graph}.txt"

        # Propriétés du graphe
        self.n_sommets = 0
        self.n_arcs = 0
        self.l_arcs = []

        try:
            self.read_file()
        except Exception as error:
            raise Exception(error.args[0])

        for i in self.l_arcs:
            print(i.arc)

    def read_file(self):
        """Lecture d'un fichier stockant un graphe"""

        with open(self.file_name) as file:
            line = file.readline()
            n = 0
            # Lecture des lignes une par une, en sécurisant les entrées
            while line:
                if n == 0:
                    try:
                        self.n_sommets = int(line)
                    except ValueError:
                        raise Exception("Erreur lors de la lecture de la première ligne")
                elif n == 1:
                    try:
                        self.n_arcs = int(line)
                    except ValueError:
                        raise Exception("Erreur lors de la lecture de la deuxième ligne")
                else:
                    try:
                        self.l_arcs.append(Arc(line[0:-2]))
                    except Exception as error:
                        raise Exception(f"{error.args[0]} ligne {n}")

                line = file.readline()
                n += 1
