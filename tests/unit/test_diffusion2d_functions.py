"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
from unittest import TestCase

class TestSolver(TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        self.solver.initialize_domain(20.0,10.0,0.1,0.1)
        self.assertEqual(self.solver.nx, 200)
        self.assertEqual(self.solver.ny, 100)


    def test_initialize_physical_parameters(self):

        self.solver.initialize_domain(10.0,10.0,0.1,0.1)
        self.solver.dx = 1.0
        self.solver.dy = 1.0
        self.solver.initialize_physical_parameters(4.0,300.0,700.0)
        self.assertEqual(self.solver.dt, 1.0/4.0/4.0)

    def test_set_initial_condition(self):
        self.solver.T_cold = 1.0
        self.solver.T_hot = 2.0
        self.solver.dx = 0.1
        self.solver.dy = 0.1
        self.solver.nx = 100
        self.solver.ny = 100
        u = self.solver.set_initial_condition()
        self.assertEqual(u[50,50],2.0)
