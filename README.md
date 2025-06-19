# Genetic Algorithm for Function Maximization

This project implements a Genetic Algorithm (GA) to find the maximum value of the function F(x) = x² over the interval [0, 31]. Each possible solution is represented as a 5-bit binary string.

## Problem Description

The goal is to find the maximum value of F(x) = x² where x is in the range [0, 31] using a Genetic Algorithm approach. The implementation allows users to customize various GA parameters and termination conditions.

### Features

- Binary string representation (5 bits)
- Customizable population size
- Multiple crossover options
  - One-point crossover
  - Two-point crossover
- Different mutation types
  - Bit flip mutation
  - Swap mutation
- Flexible termination conditions
  - No improvement for x iterations
  - Predefined number of iterations

## Usage

The program accepts the following input parameters:

1. `p`: Population size
2. `c`: Crossover type
   - 0: One-point crossover (default)
   - 1: Two-point crossover
3. `m`: Mutation type
   - 0: Bit flip mutation (default)
   - 1: Swap mutation
4. `t`: GA termination condition
   - 0: No improvement for x iterations
   - 1: Predefined iterations
5. `x`: Number of iterations without improvement (when t=0)
6. `i`: Number of predefined iterations (when t=1)

### Example Inputs

1. Example with predefined iterations:
```
p=10, c=0, m=1, t=1, i=100
```
This sets:
- Population size: 10
- One-point crossover
- Swap mutation
- Terminates after 100 iterations

2. Example with no-improvement condition:
```
p=5, c=1, m=0, t=0, x=10
```
This sets:
- Population size: 5
- Two-point crossover
- Bit flip mutation
- Terminates if no improvement for 10 iterations

## Output

The program outputs the highest fitness value solution when the termination condition is met. The solution includes:
- The binary string representation
- The corresponding decimal value
- The fitness value (x²)

## Implementation Details

- Each individual in the population is represented by a 5-bit binary string
- The search space covers integers from 0 to 31
- The fitness function F(x) = x² is used to evaluate solutions
- No external GA libraries (like PyGAD) are used in this implementation

## Note

This implementation is a pure Python solution without using any specialized genetic algorithm libraries, focusing on the fundamental concepts of genetic algorithms including:
- Population initialization
- Selection
- Crossover
- Mutation
- Termination conditions
