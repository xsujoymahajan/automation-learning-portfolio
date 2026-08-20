# Automated Conveyor

PLC-based learning project for an automated conveyor sequence.

## Project structure

| Path | Contents |
| --- | --- |
| `IO_TABLE.txt.txt` | Input/output assignment notes. |
| `SEQUENCE.txt.txt` | Intended operating sequence; ready to be completed as the control flow is defined. |
| `PLC/` | PLC project source, configuration, program units, device definitions, and build output. |
| `PLC/project.json` | PLC project manifest. |

## Suggested development checklist

- [ ] Define sensors, actuators, addresses, and safe states in the IO table.
- [ ] Describe the normal start/run/stop sequence in `SEQUENCE.txt.txt`.
- [ ] Add fault conditions and the expected recovery behavior.
- [ ] Test the logic in simulation before connecting hardware.
- [ ] Record tested behavior and any required wiring changes here.

## Safety note

For any physical conveyor, include an emergency-stop path and make sure the PLC logic defaults outputs to a safe state when a fault, stop command, or communication loss occurs.
