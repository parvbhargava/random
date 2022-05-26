import numpy as np


def random(mult=23923,
           mod=(2 ** 32) - 1,
           seed=1313223,
           size=1):
    """
    It genrates random numbers using LCG
    A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation.
    :param mult: Specify an multiplier
    :param mod: Specify an modulo
    :param seed: Give a random seed for the number
    :param size: The size of list of number you want
    :return: A random number
    """
    U = np.zeros(size)
    # we use a linear recurrence relation
    x = (seed * mult + 1) % mod
    U[0] = x / mod
    for i in range(1, size):
        x = (x * mult + 1) % mod
        U[i] = x / mod
    return U


def random_uniform(low=0,
                   high=1,
                   seed=3467239,
                   size=1):
    """
    Genrates uniformly random number between low and high limit
    :param low: The Lower limit of the number
    :param high: The Upper Limit of the number
    :param seed: The seed
    :param size: The size of list of number you want
    :return: An List of Random Numbers from Uniform Distibution
    """

    return low + (high - low) * random(seed=seed, size=size)
