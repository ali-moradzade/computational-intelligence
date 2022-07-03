import copy
import random

import numpy as np
import pandas as pd
from os.path import exists

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


# Q Tournament, in case of 2: binary tournament
def q_tournament(players, num_players, q=2):
    selected_players = []
    for i in range(num_players):
        random_players = np.random.choice(players, size=q)
        selected_players.append(max(random_players, key=lambda player: player.fitness))

    return selected_players


result_file = 'generation_results.csv'


def save_fitness_results(max_fitness, min_fitness, average_fitness):
    if not exists(result_file):
        info = {
            'worst': [min_fitness],
            'avg': [average_fitness],
            'best': [max_fitness]
        }
        df = pd.DataFrame(info)

        # Saving the dataframe
        df.to_csv(result_file)
    else:
        df = pd.read_csv(result_file)

        # Adding our results to end of dataframe
        df.loc[len(df)] = [min_fitness, average_fitness, max_fitness]

        # Saving the dataframe
        df.to_csv(result_file)


# TODO: selected a proper values
mutation_threshold = 0.2
mutation_value = 5

crossover_threshold = 0.2


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def mutation(self, player):
        player = self.clone_player(player)
        probability = np.random.uniform(0, 1)

        w1 = player.nn.w1
        w2 = player.nn.w2
        b1 = player.nn.b1
        b2 = player.nn.b2

        if probability >= mutation_threshold:
            sign = random.choice([True, False])
            if sign:
                w1 += np.random.normal(0, mutation_value, w1)
                w2 += np.random.normal(0, mutation_value, w2)
                b1 += np.random.normal(0, mutation_value, b1)
                b2 += np.random.normal(0, mutation_value, b2)
            else:
                w1 -= np.random.normal(0, mutation_value, w1)
                w2 -= np.random.normal(0, mutation_value, w2)
                b1 -= np.random.normal(0, mutation_value, b1)
                b2 -= np.random.normal(0, mutation_value, b2)

        return player

    # One point crossover (in the middle)
    def crossover(self, parent1, parent2):
        probability = np.random.uniform(0, 1)

        child1 = self.clone_player(parent1)
        child2 = self.clone_player(parent2)

        if probability < crossover_threshold:
            return child1, child2

        for name, layer1, layer2 in [('w1', parent1.nn.w1, parent2.nn.w1), ('b1', parent1.nn.b1, parent2.nn.b1),
                                     ('w2', parent1.nn.w2, parent2.nn.w2), ('b2', parent1.nn.b2, parent2.nn.b2)]:
            crossover_position = layer1.shape[0] // 2
            array1 = np.concatenate(layer1[:crossover_position], layer2[crossover_position:], axis=0)
            array2 = np.concatenate(layer2[:crossover_position], layer1[crossover_position:], axis=0)

            if name == 'w1':
                child1.nn.w1 = array1
                child2.nn.w1 = array2
            elif name == 'b1':
                child1.nn.b1 = array1
                child2.nn.b1 = array2
            elif name == 'w2':
                child1.nn.w2 = array1
                child2.nn.w2 = array2
            elif name == 'b2':
                child1.nn.b2 = array1
                child2.nn.b2 = array2

        return child1, child2

    # Reproduction step
    def reproduction(self, parent1, parent2):
        # Crossover
        child1, child2 = crossover_threshold(parent1, parent2)

        # Mutation
        self.mutation(child1)
        self.mutation(child2)

        return child1, child2

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
