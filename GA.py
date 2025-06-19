# PYTHON CODE IMPLEMENTATION OF GENETIC ALGORITHM

# Question : To find max value of the function f(x) = x^2 using genetic algorithm

# Solution : 

import random

print("")
print("<<<<<<<<<<<<<< This code is prepared by Aryan sharma >>>>>>>>>>>>>>")

# Defining the fitness function

def fit(individual):
    x = int(individual, 2)
    return x**2


# Code for tournament selection

def tournament_selection(pln, k=2):
    return max(random.sample(pln, k), key=fit)


# Code for one point crossover

def onepoint_crossover(p1, p2):
    pt = random.randint(1, len(p1) - 1)
    c1 = p1[:pt] + p2[pt:]
    c2 = p2[:pt] + p1[pt:]
    return c1, c2


# Code for two point crossover

def twopoint_crossover(p1, p2):
    pt1 = random.randint(1, len(p1) - 1)
    pt2 = random.randint(1, len(p1) - 1)
    if pt2 < pt1:
        pt1, pt2 = pt2, pt1
    c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
    c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
    return c1, c2


# Code for bit flip mutation

def bit_flip_mutn(individual, pm=0.1):
    gene_mutation = ""
    for bt in individual:
        if random.random() < pm:
            gene_mutation += "0" if bt == "1" else "1"
        else:
            gene_mutation += bt
    return gene_mutation


# Code for swapping mutation

def swap_mutn(individual, pm=0.1):
    gene_mutation = list(individual)
    for i in range(len(gene_mutation)):
        if random.random() < pm:
            j = random.randint(0, len(gene_mutation) - 1)
            gene_mutation[i], gene_mutation[j] = gene_mutation[j], gene_mutation[i]
    return "".join(gene_mutation)


# Genetic Algorithm function

# WE CAN UPDATE THE VALUES HERE OF p, c, m, t.
# TESTING conditions - 
# Input example: p=10, c=0 (default), m=1 (swap mutation), t=1 (predefined
# iterations then i=100)
# example: p=5, c=1 (two point crossover), m=0 (default), t=0 (No
# improvement for x iteration then x=10)

def genetic_algorithm(p=5, c=0, m=0, t=10, x=10, i=100):

 # Creating the initial population


    pln = ["".join([random.choice(["0", "1"]) for _ in range(5)]) for _ in range(p)]
    best_individual = max(pln, key=fit)
    best_fitness = fit(best_individual)
    no_imp = 0
    for gen in range(i):


# Code for selecting the parents


        p1 = tournament_selection(pln)
        p2 = tournament_selection(pln)

# Code for crossover

        if c == 0:
            c1, c2 = onepoint_crossover(p1, p2)
        else:
            c1, c2 = twopoint_crossover(p1, p2)


# Code for mutation
        if m == 0:
            c1 = bit_flip_mutn(c1)
            c2 = bit_flip_mutn(c2)
        else:
            c1 = swap_mutn(c1)
            c2 = swap_mutn(c2)

# Code for evaluating fitness

        c1_fit = fit(c1)
        c2_fit = fit(c2)

# Code to replace the least fit solution
        if c1_fit > c2_fit:
            if c1_fit > fit(pln[-1]):
                pln[-1] = c1
        else:
            if c2_fit > fit(pln[-1]):
                pln[-1] = c2
        if fit(pln[-1]) > best_fitness:
            best_individual = pln[-1]
            best_fitness = fit(pln[-1])
            no_imp = 0
        else:
            no_imp += 1
# Code to check the termination condition
        if t == 0 and no_imp >= x:
            break
        elif t == 1 and gen == i - 1:
            break
    return best_individual, best_fitness

# FINAL RESULT i.e. the best individual or maximum value:

print(" ")
print("**************")
best_individual, best_fitness = genetic_algorithm(4, 0, 0, 0)
print("Best Individual:", best_individual)
print("Fitness:", best_fitness)
print("**************")
print(" ")