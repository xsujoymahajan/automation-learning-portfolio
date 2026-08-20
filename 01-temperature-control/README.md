# Temperaturregelung

Ein kleines Lernprojekt für die Automatisierungstechnik. Das Projekt zeigt eine einfache **Ein/Aus-Regelung** als Python-Simulation. Es steuert keine echte Hardware.

## Lernziel

Ich übe hier:

- eine Temperatur als Eingabe zu verarbeiten,
- einen einstellbaren Sollwert zu verwenden,
- eine klare Schaltentscheidung zu treffen,
- Programmcode mit automatisierten Tests zu prüfen.

## Projektstand

### Version 1: Ein/Aus-Regelung — umgesetzt

Der Lüfter ist der simulierte Aktor:

- Temperatur **größer oder gleich** Sollwert → Lüfter **AN**
- Temperatur **kleiner** Sollwert → Lüfter **AUS**

Der Standardsollwert ist 30 °C. Beim Start kann ein anderer Sollwert angegeben werden.

### Version 2: Hysterese — geplant, noch nicht umgesetzt

In einer späteren Version soll eine Hysterese verhindern, dass der Lüfter bei Temperaturen direkt am Sollwert ständig zwischen AN und AUS umschaltet. Dafür wird zusätzlich der vorherige Schaltzustand benötigt.

### Spätere Erweiterungen

- simulierte Temperaturverläufe und Protokollierung,
- Anbindung an einen echten Sensor und einen geeigneten Mikrocontroller,
- sichere Ansteuerung eines echten Aktors nach eigener Prüfung,
- PID-Regelung als fortgeschrittenes, späteres Lernthema.

Diese Erweiterungen sind nicht gebaut oder getestet.

## Struktur

```text
01-temperature-control/
├── README.md
├── src/
│   └── temperature_control.py
├── docs/
│   └── control-logic.md
├── tests/
│   └── test_temperature_control.py
└── images/
    └── .gitkeep
```

## Ausführen

Im Projektordner:

```bash
python src/temperature_control.py
```

Beispiel:

```text
Temperatur in °C: 31
Sollwert in °C [30]: 
Temperatur: 31.0 °C
Sollwert: 30.0 °C
Lüfter: AN
```

## Tests ausführen

Die Tests sind hardwareunabhängig und prüfen nur die Python-Logik:

```bash
python -m unittest discover -s tests
```

## Hinweis zu Hardware und Sicherheit

Dieses Repository dokumentiert aktuell eine Software-Simulation. Es gibt keine Behauptung über einen aufgebauten oder getesteten Hardware-Prototypen. Bei späterer Hardwarearbeit müssen Stromversorgung, Schutzschaltungen, sichere Ausgänge und die jeweilige Dokumentation separat geplant und geprüft werden.
