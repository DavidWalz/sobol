import numpy as np
import sobol
import torch


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
    # test against pytorch's SobolEngine
    x1 = sobol.sample(dimension=1111, n_points=100, skip=0)
    x2 = torch.quasirandom.SobolEngine(dimension=1111, seed=0).draw(100)
    np.testing.assert_allclose(x1, x2)
