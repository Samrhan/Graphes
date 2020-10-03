import os
from graphe import Graph


class Main:
    def __init__(self):
        self.graph_number = self.ask_user()
        self.graph = Graph(self.graph_number)

    def ask_user(self):
        n_graph = self.get_graph_number()
        correct_answer = False
        answer = -1
        while not correct_answer:
            try:
                answer = int(input(f"Choisissez le numéro du graphe (1-{n_graph})"))
                if answer <= 0 or answer > n_graph:
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
