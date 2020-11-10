import os
from graphe import Graph


class Main:
    def __init__(self):
        correct_input = False
        self.graph_number = -1
        while self.graph_number != 0:
            while not correct_input:
                self.graph_number = self.ask_user()
                if self.graph_number == 0:
                    break
                # Création du graphe
                try:
                    graph = Graph(self.graph_number)
                    correct_input = True
                    print(graph)
                    if not graph.has_circuit:
                        valid_entries = False
                        while not valid_entries:
                            try:
                                n = ord(input("Voulez-vous calculer les chemins les plus courts ? (Y/N)"))
                                if n == 89 or n == 121:
                                    self.path(graph)
                                elif n == 110 or n == 78:
                                    valid_entries = True
                                else:
                                    raise TypeError
                            except TypeError:
                                continue
                except Exception as error:
                    # Permet de savoir où est l'erreur exactement, avec une hierarchie
                    print(error.args[0])
            correct_input = False

    def ask_user(self):
        """Saisie utilisateur"""

        n_graph = self.get_graph_number()
        correct_answer = False
        answer = -1

        while not correct_answer:
            # On boucle tant que l'utilisateur entre des valeurs incorrectes
            try:
                # utiliser int() directement sur la saisie évite la vulnérabilité de la fonction input
                answer = int(input(f"Choisissez le numéro du graphe (1-{n_graph}), 0 pour quitter\n"))
                if answer < 0 or answer > n_graph:
                    # On lève une erreur si l'utilisateur entre un numéro incorrect
                    raise ValueError
                else:
                    correct_answer = True

            except ValueError:
                print(f"Entrez un chiffre entre 1 et {n_graph} !")

        return answer

    def path(self, graph):
        correct_answer = False
        start = -1
        end = -1

        while not correct_answer:
            try:
                start = int(input(f"Choisissez le sommet de départ (0-{graph.sommets - 1})\n"))
                if start < 0 or start >= graph.sommets:
                    raise ValueError
                else:
                    correct_answer = True
            except ValueError:
                print(f"Entrez un chiffre entre 1 et {graph.sommets} !")
        correct_answer = False
        while not correct_answer:
            try:
                end = int(input(f"Choisissez le sommet d'arrivé (0-{graph.sommets - 1})\n"))
                if end < 0 or end >= graph.sommets:
                    raise ValueError
                else:
                    correct_answer = True
            except ValueError:
                print(f"Entrez un chiffre entre 0 et {graph.sommets} !")

        path = graph.path(start, end)
        pretty_print = "Chemin le plus court : "
        if path == []:
            pretty_print = "Il n'y a pas de chemin possible"
        else:
            for (i, sommet) in enumerate(path):
                if sommet != path[-1]:
                    pretty_print += f'{sommet} => '
                else:
                    pretty_print += f'{sommet}'
        print(pretty_print)

    @staticmethod
    def get_graph_number():
        return len(os.listdir('graphes'))

    def traces(self):
        for i in range(self.get_graph_number()):
            with open(f'traces/B6_{i + 1}.txt', 'w') as file:
                graph = Graph(i + 1)
                print(graph, file=file)
                if not graph.circuit :
                    for i in range(graph.sommets):
                        for j in range(graph.sommets):
                            if i != graph.sommets - j - 1:
                                path = graph.path(i, graph.sommets - j - 1)
                                pretty_print = f"Chemin le plus court de {i} vers {graph.sommets - j - 1} : "
                                if not path:
                                    pretty_print = f"Il n'y a pas de chemin possible de {i} vers {graph.sommets - j - 1}"
                                else:
                                    for (i, sommet) in enumerate(path):
                                        if sommet != path[-1]:
                                            pretty_print += f'{sommet} => '
                                        else:
                                            pretty_print += f'{sommet}'
                                print(pretty_print, file=file)


main = Main()
main.traces()
