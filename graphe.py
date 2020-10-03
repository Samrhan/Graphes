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

        self.m_adjacence = []
        self.m_valeur = []

        self.gen_m_adjacence()
        self.gen_m_valeur()

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
                        self.l_arcs.append(Arc(line[0:-1]))
                    except Exception as error:
                        raise Exception(f"{error.args[0]} ligne {n}")

                line = file.readline()
                n += 1

    def gen_m_adjacence(self):
        """Génération de la matrice d'adjacence"""

        # Initialisation du tableau
        for i in range(self.n_sommets):
            self.m_adjacence.append([])
            for j in range(self.n_sommets):
                self.m_adjacence[i].append(0)

        for i in self.l_arcs:
            self.m_adjacence[i.init][i.fin] = 1

    def gen_m_valeur(self):
        """Génération de la matrice des valeurs"""

        # Initialisation du tableau
        for i in range(self.n_sommets):
            self.m_valeur.append([])
            for j in range(self.n_sommets):
                self.m_valeur[i].append('*')

        for i in self.l_arcs:
            self.m_valeur[i.init][i.fin] = i.value

    def stringify_mat(self, _m):

        beautiful = "\t"

        for i in range(self.n_sommets):
            beautiful += f"{i}\t"
        beautiful += '\n'

        for i in range(self.n_sommets):
            beautiful += f"{i} "
            for j in range(self.n_sommets):
                beautiful += f"\t{_m[i][j]}"
            beautiful += '\n'
        return beautiful

    def __repr__(self):
        """Surcharge de l'affichage"""
        to_print = "----- Matrice d'adjacence -----\n\n"
        to_print += self.stringify_mat(self.m_adjacence)
        to_print += "\n\n----- Matrice des valeurs -----\n\n"
        to_print += self.stringify_mat(self.m_valeur)

        return to_print
