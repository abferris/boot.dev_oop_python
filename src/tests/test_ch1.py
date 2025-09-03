print('running ch1 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch1 import *

class Ch1Test(Tests):
    def test_destroy_walls(self):
        test_cases = [
            ([0, 20, 30], [20, 30]),
            ([10, 0, 40, 0], [10, 40]),
            ([], []),
            ([3, 2, 0, 3, 0, 0], [3, 2, 3]),
        ]
        self.run_cases(destroy_walls,test_cases)

    def test_fight_soldiers(self):
        test_cases = [
            (
                {"damage": 10, "attacks_per_second": 3},
                {"damage": 20, "attacks_per_second": 1},
                "soldier 1 wins",
            ),
            (
                {"damage": 50, "attacks_per_second": 1},
                {"damage": 50, "attacks_per_second": 2},
                "soldier 2 wins",
            ),
            (
                {"damage": 1, "attacks_per_second": 1},
                {"damage": 2, "attacks_per_second": 1},
                "soldier 2 wins",
            ),
            (
                {"damage": 100, "attacks_per_second": 2},
                {"damage": 50, "attacks_per_second": 4},
                "both soldiers die",
            ),
        ]
        self.run_cases(fight_soldiers,test_cases)