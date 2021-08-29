import numpy as np
import sobol


def test_rightmost_zero():
    assert sobol.rightmost_zero(0) == 0  # 0
    assert sobol.rightmost_zero(1) == 1  # 1
    assert sobol.rightmost_zero(2) == 0  # 10
    assert sobol.rightmost_zero(3) == 2  # 11
    assert sobol.rightmost_zero(4) == 0  # 100
    assert sobol.rightmost_zero(5) == 1  # 101
    assert sobol.rightmost_zero(6) == 0  # 110
    assert sobol.rightmost_zero(7) == 3  # 111
    assert sobol.rightmost_zero(8) == 0  # 1000
    assert sobol.rightmost_zero(9) == 1  # 1001
    assert sobol.rightmost_zero(1023) == 10  # 1111111111
    assert sobol.rightmost_zero(1024) == 0  # 10000000000
    assert sobol.rightmost_zero(1025) == 1  # 10000000001


def test_sample():
    # function test
    x = sobol.sample(dimension=30, n_points=100, skip=10000)
    assert x.shape == (100, 30)

    # repeated calls
    x1 = sobol.sample(dimension=100, n_points=10, skip=0)
    x2 = sobol.sample(dimension=100, n_points=10, skip=0)
    np.testing.assert_allclose(x1, x2)

    # skip ahead
    x1 = sobol.sample(dimension=5, n_points=110, skip=0)[100:]
    x2 = sobol.sample(dimension=5, n_points=10, skip=100)
    np.testing.assert_allclose(x1, x2)
