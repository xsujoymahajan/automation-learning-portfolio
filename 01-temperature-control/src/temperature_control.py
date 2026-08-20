"""Einfache Ein/Aus-Temperaturregelung (Version 1).

Diese Datei simuliert nur eine Entscheidung für einen Lüfter. Sie steuert keine
echte Hardware.
"""

from __future__ import annotations

import math

DEFAULT_SETPOINT_C = 30.0


def validate_temperature(value: float, name: str = "Temperatur") -> float:
    """Gibt einen endlichen Zahlenwert zurück oder löst ValueError aus."""
    try:
        number = float(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{name} muss eine Zahl sein.") from error

    if not math.isfinite(number):
        raise ValueError(f"{name} muss endlich sein.")

    return number


def fan_is_on(temperature_c: float, setpoint_c: float = DEFAULT_SETPOINT_C) -> bool:
    """Entscheidet Version 1: ab dem Sollwert ist der Lüfter AN."""
    temperature_c = validate_temperature(temperature_c, "Temperatur")
    setpoint_c = validate_temperature(setpoint_c, "Sollwert")
    return temperature_c >= setpoint_c


def format_control_state(temperature_c: float, setpoint_c: float) -> str:
    """Erstellt eine gut lesbare Ausgabe für die Simulation."""
    state = "AN" if fan_is_on(temperature_c, setpoint_c) else "AUS"
    return (
        f"Temperatur: {temperature_c:.1f} °C\n"
        f"Sollwert: {setpoint_c:.1f} °C\n"
        f"Lüfter: {state}"
    )


def read_number(prompt: str, default: float | None = None) -> float:
    """Liest eine Zahl ein; bei leerer Eingabe wird optional ein Standard genutzt."""
    raw_value = input(prompt).strip()
    if raw_value == "" and default is not None:
        return default
    return validate_temperature(raw_value)


def main() -> None:
    """Startpunkt für die Konsolensimulation."""
    try:
        temperature_c = read_number("Temperatur in °C: ")
        setpoint_c = read_number(
            f"Sollwert in °C [{DEFAULT_SETPOINT_C:g}]: ", DEFAULT_SETPOINT_C
        )
    except ValueError as error:
        print(f"Eingabefehler: {error}")
        return

    print()
    print(format_control_state(temperature_c, setpoint_c))


if __name__ == "__main__":
    main()
