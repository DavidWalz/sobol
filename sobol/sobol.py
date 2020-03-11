import numpy as np


def rightmost_zero(n):
    """Position of the lowest 0-bit in the binary representation of integer `n`."""
    s = np.binary_repr(n)
    i = s[::-1].find("0")
    if i == -1:
        i = len(s)
    return i


def generator(dimension):
    """Generator for the Sobol sequence"""
    DIMS = 1111  # maximum number of dimensions
    BITS = 30  # maximum number of bits

    if not (1 <= dimension <= DIMS):
        raise ValueError("Sobol: dimension must be between 1 and %i." % DIMS)

    # initialize direction numbers
    V = np.zeros((DIMS, BITS), dtype=int)
    data = np.genfromtxt(__file__.replace(".py", "1111.tsv"), dtype=int)
    poly = data[:, 0]
    V[:, :13] = data[:, 1:14]
    V[0, :] = 1
    for i in range(1, dimension):
        m = len(np.binary_repr(poly[i])) - 1
        include = np.array([int(b) for b in np.binary_repr(poly[i])[1:]])
        for j in range(m, BITS):
            V[i, j] = V[i, j - m]
            for k in range(m):
                if include[k]:
                    V[i, j] = np.bitwise_xor(V[i, j], 2 ** (k + 1) * V[i, j - k - 1])
    V = V[:dimension] * 2 ** np.arange(BITS)[::-1]

    point = np.zeros(dimension, dtype=int)
    for i in range(2 ** BITS):
        point = np.bitwise_xor(point, V[:, rightmost_zero(i)])
        yield point / 2 ** BITS


def sample(dimension, n_points, skip=0):
    """Generate a Sobol point set.

    Parameters
    ----------
    dimension : int
        Number of dimensions
    n_points : int, optional
        Number of points to sample
    skip : int, optional
        Number of points in the sequence to skip, by default 0

    Returns
    -------
    array, shape=(n_points, dimension)
        Samples from the Sobol sequence.
    """
    sobol = generator(dimension)
    for i in range(skip):
        next(sobol)
    points = np.empty((n_points, dimension))
    for i in range(n_points):
        points[i] = next(sobol)
    return points
