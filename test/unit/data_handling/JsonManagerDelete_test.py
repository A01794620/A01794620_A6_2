"""
JsonManagerDelete Unit Test
"""
import unittest
import sys
from pathlib import Path

from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from setting.Setting import Setting

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))


class JsonManagerTest(unittest.TestCase):
    """
    JsonManagerDelete Unit Test
    """
    def setUp(self):
        pass

    def test_assert_alpha_true_delete_data(self):
        for abs_type in AbstractionType:
            self.assertTrue(JsonManager.delete_data(
                            abs_type,
                            Setting.SYNTHETIC_DATA_UUID),
                            msg=f"Testing if data can "
                                f"be removed in {abs_type}")

    def test_assert_beta_false_delete_data(self):
        for abs_type in AbstractionType:
            self.assertFalse(JsonManager.delete_data(abs_type,
                                                     Setting.SYNTHETIC_DATA_UUID),  # noqa: E501
                             msg=f"Testing if data "
                                 f"can not be removed"
                                 f" in {abs_type}")


if __name__ == '__main__':
    unittest.main()
