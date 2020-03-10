# Sobol
Pythonic implementation of the Sobol quasi-random sequence for generating super-uniformly distributed points in 1-40 dimensions.

This is rewrite of the [python version](https://people.sc.fsu.edu/~jburkardt/py_src/sobol/sobol.html) by John Burkardt which was written in a hilariously Fortran-like way, making it a bit hard to understand.

### Usage 
```python
import sobol
sobol.sample(n_dim=3, n_points=5)
```
yields
```python
array([[0.5  , 0.5  , 0.5  ],
       [0.75 , 0.25 , 0.75 ],
       [0.25 , 0.75 , 0.25 ],
       [0.375, 0.375, 0.625],
       [0.875, 0.875, 0.125]])
```