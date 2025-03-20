# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities as ct
import random

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    def __init__(self):
        self._list_possible_cases = ct.default_road(ct.load_cities("cities.txt"))
        self._len_chrom = len(ct.default_road(ct.load_cities("cities.txt")))
        self._duplicate_genes = False
        self._threshold_fitness = 0
        self._max_generation = 2000

    def fitness(self, chromosome):
        return 1 / ct.road_length(ct.load_cities("cities.txt"), chromosome)
    
    def generer_random(self):
        return random.sample(ct.default_road(ct.load_cities("cities.txt")), len(ct.default_road(ct.load_cities("cities.txt"))))


if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = ct.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    ct.draw_cities(city_dict, solver.get_best_individual().chromosome)