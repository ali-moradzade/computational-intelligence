import copy
import random
import os

import numpy as np
import pandas as pd
from os.path import exists

from player import Player


# Roulette Wheel Selection
def rw(players, num_players):
    population_fitness = sum([player.fitness for player in players])
    population_probabilities = [player.fitness / population_fitness for player in players]

    return np.random.choice(players, size=num_players, p=population_probabilities).tolist()


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

        start += probability

    return samples


# Q Tournament, in case of 2: binary tournament
def q_tournament(players, q=2):
    random_player = np.random.choice(players, size=q)
    return max(random_player, key=lambda player: player.fitness)


result_file = 'generation_results.csv'


def save_fitness_results(min_fitness, average_fitness, max_fitness):
    if not exists(result_file):
        info = {
            'worst': [min_fitness],
            'avg': [average_fitness],
            'best': [max_fitness]
        }
        df = pd.DataFrame(info)

        # Saving the dataframe
        df.to_csv(result_file, index=False)
    else:
        df = pd.read_csv(result_file)

        # Adding our results to end of dataframe
        df.loc[len(df)] = [min_fitness, average_fitness, max_fitness]

        # Saving the dataframe
        df.to_csv(result_file, index=False)


mutation_threshold = 0.05
mutation_value = 0.2
crossover_threshold = 0.6


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"
        self.selection_mode = 'top-k'

        if exists(result_file):
            os.remove(result_file)

    def mutation(self, player):
        player = self.clone_player(player)
        probability = np.random.uniform(0, 1)

        if probability >= mutation_threshold:
            player.nn.w1 += np.random.normal(0, mutation_value, player.nn.w1.shape)
            player.nn.w2 += np.random.normal(0, mutation_value, player.nn.w2.shape)
            player.nn.b1 += np.random.normal(0, mutation_value, player.nn.b1.shape)
            player.nn.b2 += np.random.normal(0, mutation_value, player.nn.b2.shape)

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
            array1 = np.concatenate((layer1[:crossover_position], layer2[crossover_position:]), axis=0)
            array2 = np.concatenate((layer2[:crossover_position], layer1[crossover_position:]), axis=0)

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
        child1, child2 = self.crossover(parent1, parent2)

        # Mutation
        child1 = self.mutation(child1)
        child2 = self.mutation(child2)

        return child1, child2

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """

        # Additional: Learning curve
        min_fitness = min(player.fitness for player in players)
        average_fitness = sum([player.fitness for player in players]) / len(players)
        max_fitness = max(player.fitness for player in players)

        save_fitness_results(min_fitness, average_fitness, max_fitness)

        if self.selection_mode == 'top-k':
            sorted_players = sorted(players, key=lambda player: player.fitness, reverse=True)
            return sorted_players[:num_players]

        elif self.selection_mode == 'sus':
            return sus(players, num_players)

        elif self.selection_mode == 'rw':
            return rw(players, num_players)

        else:
            return players[:num_players]

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
            parents = []
            new_players = prev_players

            # Q Tournament
            for i in range(num_players):
                parents.append(q_tournament(prev_players))

            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[i + 1]
                child1, child2 = self.reproduction(parent1, parent2)
                new_players.append(child1)
                new_players.append(child2)

            new_players.sort(key=lambda x: x.fitness, reverse=True)
            new_players = new_players[: num_players]
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
