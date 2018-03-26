# Simple Genetic Algorithm

[![Build Status](https://travis-ci.org/gbroques/simple-genetic-algorithm.svg?branch=master)](https://travis-ci.org/gbroques/simple-genetic-algorithm)

A simple genetic algorithm that uses crossover and mutation to solve the *onemax* problem.

In evolutionary computation, the *onemax problem* is where you evolve binary strings by maximizing the amount of 1's in each string.

For example, given a set of binary strings of length 5, the goal is to evolve strings that look like `11111`, where each possible position contains a 1.

## How to Run
Run with Python 3 or greater.

`python main.py`

## Minimum Population Size
The following is a table demonstrating the minimum population size to find the global optimum for a given string size.

| String Size | Minimum Population Size |
|-------------|-------------------------|
| 20          | 8                       |
| 50          | 12 - 14                 |
