import unittest

from Game.Card.VictoryPoints.Test.fixed_points_test import suite as fixed_points_suite

suites = [fixed_points_suite]
suite = unittest.TestSuite(suites)