import numpy as np
import numpy.testing
import sobol
import torch


def test_bit_lo0():
    assert sobol.bit_lo0(0) == 0  # 0
    assert sobol.bit_lo0(1) == 1  # 1
    assert sobol.bit_lo0(2) == 0  # 10
    assert sobol.bit_lo0(3) == 2  # 11
    assert sobol.bit_lo0(4) == 0  # 100
    assert sobol.bit_lo0(5) == 1  # 101
    assert sobol.bit_lo0(6) == 0  # 110
    assert sobol.bit_lo0(7) == 3  # 111
    assert sobol.bit_lo0(8) == 0  # 1000
    assert sobol.bit_lo0(9) == 1  # 1001
    assert sobol.bit_lo0(1023) == 10  # 1111111111
    assert sobol.bit_lo0(1024) == 0  # 10000000000
    assert sobol.bit_lo0(1025) == 1  # 10000000001


def test_sample():
    # test against pytorch's SobolEngine
    x1 = sobol.sample(n_dim=1111, n_points=100, skip=0)
    x2 = torch.quasirandom.SobolEngine(dimension=1111, seed=0).draw(100)
    np.testing.assert_allclose(x1, x2)
