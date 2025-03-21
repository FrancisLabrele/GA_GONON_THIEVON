# GA_GONON_THIEVON

A Python implementation of genetic algorithms to solve optimization problems:

1. The Traveling Salesperson Problem (TSP)
2. The Mastermind game
3. General optimization problems

## Lab work Structure

- `ga_solver.py` - Core genetic algorithm implementation with `GASolver` and `GAProblem` classes
- `tsp_problem.py` - TSP solver using genetic algorithm 
- `cities.py` - Utilities for TSP including city loading and path visualization
- `mastermind.py` - Mastermind game implementation
- `mastermind_problem.py` - Mastermind solver using genetic algorithm


## How to use the genetic algorithm

In the files `tsp_problem.py` and `mastermind_problem.py`, we use a specialized class for the problems that inherits from the GAProblem class. We just need to define its parameters. Once this specific GAProblem class is defined, we simply use GASolver on it to solve the problem using the genetic algorithm.

To see the result, you can just run `tsp_problem.py` and `mastermind_problem.py` and see how it works. Moreover, this implementation allows you to change the parameters to optimize the algorithm for the specific problem (changing the size of the population, the maximum number of generation etc.). With that, you can solve basically all the problems that can be solved by a genetic algorithm just by defining them very quickly by inheriting the class GAProblem.