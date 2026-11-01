# Simulated Smart Room IoT Monitoring

A laptop-based IoT project using Python, Mosquitto MQTT and Node-RED to monitor simulated temperature, humidity and light readings.

All readings are simulated. No physical sensors are used.

## Features

- Simulated readings published every 2 seconds
- Live temperature, humidity and light gauges
- Temperature history chart showing the last 5 minutes
- High-temperature warning at 32°C or above
- Offline status after 10 seconds without readings
- Automatic return to online status when readings resume
- JSONL logging with a reception timestamp

## How It Works

Python publishes JSON readings to the MQTT topic `smartroom/readings`.
Mosquitto forwards these messages to Node-RED, which updates the dashboard, checks the temperature threshold, monitors incoming data and saves readings.

## Technologies

- Python and paho-mqtt
- Mosquitto MQTT broker
- Node-RED
- FlowFuse Dashboard 2

## Project Files

- `sensor_simulator.py`: simulated sensor publisher
- `SmartRoomIoT_flow.json`: exported Node-RED flow

## Setup

1. Install Python, Mosquitto, Node.js and Node-RED.
2. Start the local Mosquitto broker on port 1883.
3. In the project folder, create a Python environment:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install paho-mqtt==2.1.0
```

4. Start Node-RED:

```cmd
node-red
```

5. Open `http://localhost:1880`.
6. In Manage Palette, install `@flowfuse/node-red-dashboard`.
   The exported flow was built with version 1.34.1.
7. Import `SmartRoomIoT_flow.json`.
8. In the Save Readings node, change the filename to an absolute path on your computer. The exported flow uses:
   `C:/Users/admin/SmartRoomIoT/data/readings.jsonl`
9. Check that the MQTT broker is set to `localhost:1883`, then deploy.
10. Run the simulator:

```cmd
python sensor_simulator.py
```

11. Open the dashboard at `http://localhost:1880/dashboard/page1`.

Keep Node-RED and the simulator running in separate terminals.

## Manual Tests Completed

| Test | Observed result |
|---|---|
| Run simulator | Gauges and chart receive readings |
| Publish temperature of 33°C | High-temperature warning appears |
| Stop simulator | Offline status appears after 10 seconds |
| Restart simulator | Online status returns |
| Inspect log file | Readings are saved as individual JSON lines |

## Limitations

- Random values demonstrate the data pipeline rather than realistic room behaviour.
- Alert thresholds are demonstration settings.
- Offline means no recent readings; it does not identify the cause.
- Gauges retain their last readings while offline.
- Chart history is temporary; JSONL provides the saved record.
- MQTT authentication and TLS are not configured in this local demonstration.

## Dashboard Screenshot

<img width="463" height="384" alt="dashboard screen short" src="https://github.com/user-attachments/assets/68d01fd7-0d83-4c14-9750-faff080cb4da" />


## Future Improvements

- MQTT authentication and TLS
- Input validation
- Database storage
- Physical sensor integration
