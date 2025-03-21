# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    _list_possible_cases = []
    _len_chrom = 0
    _duplicate_genes = False
    _threshold_fitness = 0
    _max_generation = 0
    _pop_size = 0
    
    def fitness(self, chromosome: list):
        pass

    def generer_random(self):
        pass



class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem
        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self):
        """ Initialize the population with pop_size random Individuals """
        for i in range(self._problem._pop_size):
            chromosome = self._problem.generer_random()
            random.shuffle(chromosome)
            fitness = self._problem.fitness(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        # We get rid of the x less adapted individuals
        x = int(self._selection_rate * len(self._population))
        self._population.sort(reverse=True)
        self._population[(len(self._population)-x):] = []

        # We recreate x new individuals based on 2 survivors (the parents)
        for i in range(x):
            # We choose 2 non identical parents randomly
            number1 = random.randrange(0, x)
            number2 = random.randrange(0, x)
            while (number1 == number2):
                number2 = random.randrange(0, x)
            parent1 = self._population[number1]
            parent2 = self._population[number2]

            # Case where the genes can be duplicated
            if (self._problem._duplicate_genes):
                new_chrom = [random.choice([parent1.chromosome[i], parent2.chromosome[i]]) for i in range(self._problem._len_chrom)]
                # There is a probability of mutation for the new individual
                if (random.random() < self._mutation_rate):
                    valid_genes = self._problem._list_possible_cases
                    new_gene = random.choice(valid_genes)
                    new_chrom[random.randrange(0, len(new_chrom))] = new_gene

            # Case where the genes cannot be duplicated (no mutation possible here)
            else:
                new_chrom = [random.choice(parent1.chromosome[i], parent2.chromosome[i]) for i in range(self._problem.len_chrom)]
                available_genes = set(parent1.chromosome + parent2.chromosome)
                seen = set()
                for i in range(len(new_chrom)):
                    if new_chrom[i] in seen:
                        replacement_gene = random.choice(available_genes)
                        while replacement_gene in seen:
                            replacement_gene = random.choice(available_genes)
                        new_chrom[i] = replacement_gene
                    else:
                        seen.add(new_chrom[i])

            # We evaluate the fitness of the new child and add it to the population
            child_fitness = self._problem.fitness(new_chrom)
            child = Individual(new_chrom, child_fitness)
            self._population.append(child)

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        for i in range(len(self._population)):
            print(f"Individu {i} : {self._population[i]}, fitness : {self._population[i].fitness}")

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse=True)
        return self._population[0]

    def evolve_until(self):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        i = 0
        while (i < self._problem._max_generation and self.get_best_individual().fitness < self._problem._threshold_fitness):
            print(f"Generation {i}")
            self.show_generation_summary()
            self.evolve_for_one_generation()
            i += 1
