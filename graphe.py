from arc import Arc
import copy


class Graph:
    """Classe représentant un graphe"""

    def __init__(self, _num_graph):
        self.num_graph = _num_graph
        self.file_name = f"graphes/B6_{self.num_graph}.txt"

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

        self.m_floyd_l = []
        self.m_floyd_p = []

        self.gen_m_adjacence()
        self.gen_m_valeur()

        self.floyd_warshall()

        self.circuit = self.circuit_detection()

    # print(self.path(0, 9))

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

        pretty_print = "\t"

        for i in range(self.n_sommets):
            pretty_print += f"{i}\t"
        pretty_print += '\n'

        for i in range(self.n_sommets):
            pretty_print += f"{i} "
            for j in range(self.n_sommets):
                pretty_print += f"\t{_m[i][j]}"
            pretty_print += '\n'
        return pretty_print

    def floyd_warshall(self):
        """Execute l'algorithme de Floyd-Warshall sur le graphe"""

        # Génération des matrices
        self.m_floyd_l = copy.deepcopy(self.m_valeur)
        for i, row in enumerate(self.m_floyd_l):
            self.m_floyd_p.append([])
            for j, val in enumerate(row):
                if i == j:
                    self.m_floyd_l[i][j] = 0
                    self.m_floyd_p[i].append(i)
                else:
                    if self.m_floyd_l[i][j] == '*':
                        self.m_floyd_l[i][j] = 10000
                self.m_floyd_p[i].append('*')
        for i in self.l_arcs:
            self.m_floyd_p[i.init][i.fin] = i.init

        # Algorithme de Floyd Warhsall
        for k in range(self.n_sommets):
            for j in range(self.n_sommets):
                for i in range(self.n_sommets):
                    if self.m_floyd_l[i][k] != 10000 and self.m_floyd_l[k][j] != 10000:
                        if self.m_floyd_l[i][k] + self.m_floyd_l[k][j] < self.m_floyd_l[i][j]:
                            self.m_floyd_l[i][j] = self.m_floyd_l[i][k] + self.m_floyd_l[k][j]
                            self.m_floyd_p[i][j] = self.m_floyd_p[k][j]

        for i in range(self.n_sommets):
            for j in range(self.n_sommets):
                if self.m_floyd_l[i][j] == 10000:
                    self.m_floyd_l[i][j] = '*'

    def circuit_detection(self):
        """Detection de circuit"""

        # Génération d'une matrice temporaire
        tmp = copy.deepcopy(self.m_adjacence)
        done = []
        todo = [i for i in range(self.n_sommets)]
        todo_prec = []
        stop_condition = True
        while stop_condition:
            todo_prec.clear()
            todo_prec = todo.copy()
            for i, sommet in enumerate(todo):
                pred = 0
                for j in range(self.n_sommets):
                    if tmp[j][sommet] == 1:
                        pred += 1

                if pred == 0:
                    done.append(sommet)

            for i, sommet in enumerate(done):
                for j in range(self.n_sommets):
                    tmp[j][sommet] = -1
                    tmp[sommet][j] = -1

            for i in done:
                if i in todo:
                    todo.remove(i)
            stop_condition = not todo_prec == todo
        if len(todo) > 0:
            return True
        else:
            return False

    def path(self, start, end):
        """Calcul du chemin le plus court, à l'aide de l'alorithme de Floyd-Warshall"""

        if self.m_floyd_p[start][end] == '*':
            return []
        else:
            chemin = [end]
            while start != end:
                end = self.m_floyd_p[start][end]
                chemin.append(end)
            chemin.reverse()
            return chemin

    def __repr__(self):
        """Surcharge de l'affichage"""
        to_print = "----- Matrice d'adjacence -----\n\n"
        to_print += self.stringify_mat(self.m_adjacence)
        to_print += "\n\n----- Matrice des valeurs -----\n\n"
        to_print += self.stringify_mat(self.m_valeur)
        to_print += "\n\n----- Floyd-Warshall Matrice L-----\n\n"
        to_print += self.stringify_mat(self.m_floyd_l)
        to_print += "\n\n----- Floyd-Warshall Matrice P-----\n\n"
        to_print += self.stringify_mat(self.m_floyd_p)
        to_print += "\n\nIl y a un ou plusieurs circuits absorbants\n\n" if self.circuit else "\n\nIl n'y a pas de circuit absorbant\n\n"
        return to_print

    @property
    def has_circuit(self):
        """Getter de si il y a un circuit"""
        return self.circuit

    @property
    def sommets(self):
        """Getter du nombre de sommet"""
        return self.n_sommets
