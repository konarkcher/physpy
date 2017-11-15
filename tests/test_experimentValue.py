from unittest import TestCase
import math

from physpy import ExperimentValue as Ev


class TestExperimentValue(TestCase):
    def test___add__(self):
        self.assertEqual(Ev(2, 1) + Ev(3, 1), Ev(5, math.sqrt(2)))
        self.assertEqual(Ev(2, 1) + 4, Ev(6, 1))

    def test___radd__(self):
        self.assertEqual(2 + Ev(3, 1), Ev(5, 1))

    def test___sub__(self):
        self.assertEqual(Ev(2, 1) - Ev(3, 1), Ev(-1, math.sqrt(2)))

    def test___rsub__(self):
        self.assertEqual(2 - Ev(3, 1), Ev(-1, 1))

    def test___mul__(self):
        ans = Ev(6, epsilon=math.sqrt(0.5**2 + (1 / 3)**2))
        self.assertEqual(Ev(2, 1) * Ev(3, 1), ans)

    def test___rmul__(self):
        self.assertEqual(2 * Ev(3, 1), Ev(6, epsilon=1 / 3))

    def test___truediv__(self):
        ans = Ev(2 / 3, epsilon=math.sqrt(0.5**2 + (1 / 3)**2))
        self.assertEqual(Ev(2, 1) / Ev(3, 1), ans)

    def test___rtruediv__(self):
        self.assertEqual(2 / Ev(3, 1), Ev(2 / 3, epsilon=1 / 3))

    def test___pow__(self):
        self.assertEqual(Ev(3, 1)**2, Ev(3**2, epsilon=(1 / 3) * 2))

    def test___neg__(self):
        self.assertEqual(-Ev(2, 3), Ev(-2, 3))

    def test___pos__(self):
        self.assertEqual(Ev(2, 1), Ev(2, 1))

    def test___abs__(self):
        self.assertEqual(abs(Ev(-2, 1)), Ev(2, 1))
        self.assertEqual(abs(Ev(2, 1)), Ev(2, 1))
