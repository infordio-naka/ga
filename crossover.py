#coding: utf-8

import os
import copy
import numpy        as np
import numpy.random as npr
from individual  import Individual
from population  import Population

class Crossover(object):
    """
    Crossover Class

    Crossover Algorithm
    * One point
    * Two points
    * Random points
    """
    @classmethod
    def onePoint(self, parents, n, gene_size, crate):
        """
        One point crossover

        [imagine]
        parent1: [0, 1, 1]
                            => crossover => child: [1(p1), 0(p2), 0(p2)]
        parent2: [1, 1, 0] 
        
        [example]
        Crossover.Onepoint(list.parents, 5) => [crossover the parents for individuals size]

        :param list[Individual] parents: Selected parents
        :param int n: Size of individuals
        :param int gene_size: Size of gene
        :param int crate:     Probability of crossover
        :returns: Children
        :rtype:   list[Individual]
        """
        children = []
        idx      = [i for i in range(gene_size)]
        for i in range(n):
            child = Individual()
            parent1, parent2 = npr.choice(parents, 2, replace=False)
            gene1 = copy.copy(parent1.getGene())
            gene2 = parent2.getGene()
            point = npr.choice(idx, 1)[0]
            if (crate>npr.random()):
                gene1[point:] = gene2[point:]
            child.setGene(gene1)
            children.append(child)
        return (children)

    @classmethod
    def twoPoints(self, parents, n, gene_size, crate):
        """
        Two points crossover

        [imagine]
        parent1: [0, 1, 1, 1]
                               => crossover => child: [0(p1), 1(p2), 0(p2), 1(p1)]
        parent2: [1, 1, 0, 1]

        [example]
        Crossover.Twopoints(list.parents) => [crossover the parents for individuals size]

        :param list[Individual] parents: Selected parents
        :param int n: Size of individuals
        :param int gene_size: Size of gene
        :param int crate:     Probability of crossover
        :returns: Children
        :rtype:   list[Individual]
        """
        children = []
        idx      = [i for i in range(gene_size)]
        for i in range(n):
            child  = Individual()
            parent1, parent2 = npr.choice(parents, 2, replace=False)
            gene1  = copy.copy(parent1.getGene())
            gene2  = parent2.getGene()
            points = npr.choice(idx, 2)
            points.sort()

            if (crate>npr.random()):
                gene1[points[0]:points[1]+1] = gene2[points[0]:points[1]+1]
            child.setGene(gene1)
            children.append(child)
        return (children)

    @classmethod
    def randomPoints(self, parents, n, gene_size, crate):
        """
        Random points crossover

        [imagine]
        parent1: [0, 1, 1, 1]
                               => crossover => child: [1(p2), 1(p1), 1(p1), 1(p2)]
        parent2: [1, 1, 0, 1]

        [example]
        Crossover.Twopoints(list.parents) => [crossover the parents for individuals size]

        :param list[Individual] parents: Selected parents
        :param int n: Size of individuals
        :param int gene_size: Size of gene
        :param int crate:     Probability of crossover
        :returns: Children
        :rtype:   list[Individual]
        """
        children = []
        idx      = [i for i in range(gene_size)]
        n_random = npr.randint(1, gene_size+1)
        for i in range(n):
            child  = Individual()
            parent1, parent2 = npr.choice(parents, 2, replace=False)
            gene1  = copy.copy(parent1.getGene())
            gene2  = parent2.getGene()
            points = npr.choice(idx, n_random, replace=False)

            if (crate>npr.random()):
                for j in points:
                    gene1[j] = gene2[j]
            child.setGene(gene1)
            children.append(child)
        return (children)

if __name__ == "__main__":
    from readDataset import readDataset
    from individual  import Individual
    from select      import Select
    dataset = readDataset("./dataset/binary.txt")
    population = Population()
    for i in range(5):
        ind = Individual()
        ind.createGene(dataset, 10)
        population.addInd(ind)

    def evaluate(ind):
        fitness = sum(ind)
        return (fitness)

    population.calcFitness(evaluate)
    population.show()
    parents  = Select.Tournament(population, 5, 3, "max")
    for ind in parents:
        ind.show()
    print("Onepoint")
    children = Crossover.onePoint(parents, 5, 10, 0.7)
    for ind in children:
        ind.show()
    print("Twopoints")
    children = Crossover.twoPoints(parents, 5, 10, 0.7)
    for ind in children:
        ind.show()
    print("Randompoints")
    children = Crossover.randomPoints(parents, 5, 10, 0.7)
    for ind in children:
        ind.show()
