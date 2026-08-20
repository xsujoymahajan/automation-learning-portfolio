"""Hardwareunabhängige Tests für Version 1."""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from temperature_control import DEFAULT_SETPOINT_C, fan_is_on, format_control_state


class FanControlTests(unittest.TestCase):
    def test_fan_is_off_below_setpoint(self) -> None:
        self.assertFalse(fan_is_on(29.9, 30.0))

    def test_fan_is_on_at_setpoint(self) -> None:
        self.assertTrue(fan_is_on(30.0, 30.0))

    def test_custom_setpoint_is_used(self) -> None:
        self.assertTrue(fan_is_on(20.0, 18.0))
        self.assertFalse(fan_is_on(17.9, 18.0))

    def test_invalid_values_are_rejected(self) -> None:
        for invalid_value in ("warm", math.nan, math.inf):
            with self.subTest(invalid_value=invalid_value):
                with self.assertRaises(ValueError):
                    fan_is_on(invalid_value)

    def test_output_contains_control_state(self) -> None:
        output = format_control_state(31.0, DEFAULT_SETPOINT_C)
        self.assertIn("Temperatur: 31.0 °C", output)
        self.assertIn("Sollwert: 30.0 °C", output)
        self.assertIn("Lüfter: AN", output)


if __name__ == "__main__":
    unittest.main()
