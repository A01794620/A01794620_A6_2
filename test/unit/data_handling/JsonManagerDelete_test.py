import unittest
import sys
from pathlib import Path

_parent_dir = Path(__file__).parent.parent.parent.parent.resolve()
sys.path.insert(0, str(_parent_dir))
from data_handling.JsonManager import JsonManager
from abstraction.AbstractionType import AbstractionType
from setting.Setting import Setting


class JsonManagerTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_assert_alpha_true_delete_data(self):
        for abs_type in AbstractionType:
            self.assertTrue(JsonManager.delete_data(abs_type, Setting.SYNTHETIC_DATA_UUID),
                                msg=f"Testing if data can be removed in {abs_type}")

    def test_assert_beta_false_delete_data(self):
        for abs_type in AbstractionType:
            self.assertFalse(JsonManager.delete_data(abs_type, Setting.SYNTHETIC_DATA_UUID),
                                msg=f"Testing if data can not be removed in {abs_type}")


if __name__ == '__main__':
    unittest.main()