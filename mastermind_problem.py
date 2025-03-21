# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm

class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def __init__(self, match):
        # Initialization of the problem's parameters
        self._list_possible_cases = mm.get_possible_colors()
        self._len_chrom = match.secret_size()
        self._duplicate_genes = True
        self._threshold_fitness = match.max_score()
        self._max_generation = 50
        self._pop_size = 50

    # Definition of the fitness function that depends on the problem
    def fitness(self, chromosome):
        return match.rate_guess(chromosome)
    
    # Definition of the random generator function that depends on the problem
    def generer_random(self):
        return match.generate_random_guess()


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    print(
        f"Best guess {mm.encode_guess(solver.get_best_individual().chromosome)} {solver.get_best_individual()}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
