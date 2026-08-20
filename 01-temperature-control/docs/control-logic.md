# Regelungslogik

## Version 1: Ein/Aus-Regelung

Die Simulation vergleicht die gemessene Temperatur mit einem Sollwert:

| Bedingung | Simulierter Lüfter |
| --- | --- |
| Temperatur < Sollwert | AUS |
| Temperatur ≥ Sollwert | AN |

Der Standardsollwert ist 30 °C, kann aber beim Programmstart verändert werden.

Das ist eine einfache Schwellenwertsteuerung. Der Code nutzt keine Hardware, keine Messwerte eines echten Sensors und keine PID-Regelung.

## Version 2: Hysterese (geplant)

Direkt am Sollwert kann eine Ein/Aus-Regelung bei schwankender Temperatur häufig schalten. Eine Hysterese würde zwei Grenzen verwenden und den letzten Zustand speichern:

- Lüfter einschalten, wenn die Temperatur die obere Grenze erreicht.
- Lüfter eingeschaltet lassen, bis die Temperatur unter die untere Grenze fällt.

Diese Version ist bewusst noch nicht im Programm umgesetzt. Sie ist ein nächster Lernschritt, nachdem Version 1 verstanden und bei Bedarf mit einer sicheren Testumgebung ausprobiert wurde.

## Tests

Die Tests prüfen die reine Entscheidungslogik, einschließlich der Grenze am Sollwert und ungültiger Eingaben. Sie ersetzen keinen Hardware-, Sicherheits- oder Praxistest.
