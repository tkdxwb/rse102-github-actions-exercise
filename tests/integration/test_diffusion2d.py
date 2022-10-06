"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import math


def test_initialize_physical_parameters():
    solver = SolveDiffusion2D()
    solver.initialize_domain(20.0, 10.0, 0.1, 0.1)
    solver.initialize_physical_parameters(4.0)
    assert math.isclose(solver.dt, 0.000625)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
