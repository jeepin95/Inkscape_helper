#from inkscape_helper.Effect.Effect import Effect
from inkscape_helper.Ellipse import Ellipse
from inkscape_helper.Coordinate import Coordinate

from math import pi, atan
from __future__ import division

import unittest

# Helper function to avoid rounding errors
def pretty_close(a ,b, tolerance=1E-4):
    return abs(a - b) < tolerance  #TODO: current ellipse and bezier interpolation is always on the short side


class TestEllipse(unittest.TestCase):
    def setUp(self):
        self.circle = Ellipse(10, 10)

    def test_coordinate_at_theta(self):
        ell = Ellipse(12,8)
        self.assertEqual(ell.coordinate_at_theta(0), Coordinate(12, 0), 'coordinate at angle 0')
        self.assertTrue(Coordinate(0, 8).close_enough_to(ell.coordinate_at_theta(pi/2)), 'coordinate at angle pi/2')
        self.assertTrue(Coordinate(-12, 0).close_enough_to(ell.coordinate_at_theta(pi)), 'coordinate at angle pi')
        self.assertTrue(Coordinate(0, -8).close_enough_to(ell.coordinate_at_theta(3*pi/2)), 'coordinate at angle 3*pi/2')

    def test_circle(self):
        self.assertTrue(pretty_close(self.circle.circumference, 20 * pi), 'circumference circle')
        self.assertTrue(pretty_close(self.circle.dist_from_theta(0, pi), 10 * pi), 'arc length 0 -> pi')
        self.assertTrue(pretty_close(self.circle.dist_from_theta(3 * pi / 2, 0), 5 * pi), 'arc length 3 * pi / 2 -> 0')
        self.assertTrue(pretty_close(self.circle.theta_from_dist(0, 10 * pi), pi))

    def test_theta_at_angle(self):
        ell = Ellipse(20, 10)
        # straight angles
        self.assertEqual(ell.theta_at_angle(0), 0, 'theta at 0')
        self.assertEqual(ell.theta_at_angle(pi / 2), pi / 2, 'theta at 90')
        self.assertTrue(pretty_close(ell.theta_at_angle(pi), pi, 1e-15), 'theta at 180')
        self.assertEqual(ell.theta_at_angle(3 * pi / 2), 3 * pi / 2, 'theta at 270')
        # 45 degrees
        self.assertEqual(ell.theta_at_angle(pi / 4), atan(2), 'theta at 45')

    def test_curvature(self):
        ell = Ellipse(20, 10)
        self.assertEqual(ell.curvature(0), 1/5, 'curvature at 0')
        self.assertEqual(ell.curvature(pi / 2), 1/40, 'curvature at 90')
        self.assertEqual(ell.curvature(pi), 1/5, 'curvature at 180')
        self.assertEqual(ell.curvature(3 * pi / 2), 1/40, 'curvature at 270')

    def test_dist_from_theta(self):
        pass

    def test_theta_from_dist(self):
        pass
