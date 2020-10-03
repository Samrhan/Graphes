import os
from graphe import Graph


class Main:
    def __init__(self):
        self.graph = 0

        while self.graph == 0:
            self.graph_number = self.ask_user()
            # Création du graphe
            try:
                self.graph = Graph(self.graph_number)
            except Exception as error:
                print(error.args[0])

        print(self.graph)

    def ask_user(self):
        """Saisie utilisateur"""

        n_graph = self.get_graph_number()
        correct_answer = False
        answer = -1

        while not correct_answer:
            # On boucle tant que l'utilisateur entre des valeurs incorrectes
            try:
                # utiliser int() directement sur la saisie évite la vulnérabilité de la fonction input
                answer = int(input(f"Choisissez le numéro du graphe (1-{n_graph})"))
                if answer <= 0 or answer > n_graph:
                    # On lève une erreur si l'utilisateur entre un numéro incorrect
                    raise ValueError
                else:
                    correct_answer = True

            except ValueError:
                print(f"Entrez un chiffre entre 1 et {n_graph} !")

        return answer

    @staticmethod
    def get_graph_number():
        return len(os.listdir('graphes'))


Main()
