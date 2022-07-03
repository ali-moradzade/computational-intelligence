import copy
import random

import numpy as np

from player import Player


# Roulette Wheel Selection
def rw(players, num_players):
    population_fitness = sum([player.fitness for player in players])
    population_probabilities = [player.fitness / population_fitness for player in players]

    return np.random.choice(players, size=num_players, p=population_probabilities)


# Stochastic Universal Sampling
def sus(players, num_players):
    population_fitness = sum([player.fitness for player in players])
    player_probability = [(player, player.fitness / population_fitness) for player in players]

    # N1 = len(players)
    N2 = num_players

    ruler_size = 1 - 1 / N2
    ruler = np.linspace(0, ruler_size, N2)

    random_num = random.uniform(0, 1 / N2)
    ruler = [probe + random_num for probe in ruler]

    samples = []

    start, end = 0, 0
    for player, probability in player_probability:
        end = start + probability

        for probe in ruler:
            if start < probe <= end:
                samples.append(player)

    return samples


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)

        # TODO (Additional: Learning curve)
        return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
            new_players = prev_players  # DELETE THIS AFTER YOUR IMPLEMENTATION
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
