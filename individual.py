#coding: utf-8

import os
import numpy        as np
import numpy.random as npr

class Individual(object):
    """
    Individual Class

    example: individual = [0, 1, 0, ... , 0]
    """
    def __init__(self):
        self.gene = []
        self.fit  = None

    def createGene(self, dataset, gene):
        """
        Create gene with dataset

        :param list[] dataset: prepared dataset
        :param int gene: Size of gene
        :returns: gene
        :rtype:   list[int]

        """
        for i in npr.choice(dataset, gene):
            self.gene.append(i)
        self.gene = np.asarray(self.gene)

    def setGene(self, gene):
        """
        Set gene

        :param gene: gene
        """
        self.gene = gene
        
    def getGene(self):
        """
        :returns: gene
        :rtype:   list[int]
        """
        return (self.gene)

    def setFitness(self, fit):
        """
        Set fitness

        :param fit: fitness
        """
        self.fit = fit

    def getFitness(self):
        """
        Get fitness

        :returns: fitness
        :rtype:   int
        """
        return (self.fit)
    
    def show(self):
        """
        This individual show infomation
        """
        print(self)
        print("\tgene    is ", self.gene)
        print("\tfitness is ", self.fit)

if __name__ == "__main__":
    from readDataset import readDataset
    dataset = readDataset("./dataset/binary.txt")
    individual = Individual()
    for i in range(5):
        individual.createGene(dataset, 10)
    individual.show()
