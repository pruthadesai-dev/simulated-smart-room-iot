import json
import random
import time
from datetime import datetime

import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)
client.loop_start()

print("Publishing SIMULATED readings. Press Ctrl+C to stop.")

try:
    while True:
        data = {
            "timestamp": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "simulated": True,
            "temperature": round(random.uniform(20, 35), 1),
            "humidity": round(random.uniform(35, 75), 1),
            "light": random.randint(50, 800)
        }

        payload = json.dumps(data)
        result = client.publish(
            "smartroom/readings", payload, qos=1
        )
        result.wait_for_publish(timeout=5)

        if result.is_published():
            print("Sent:", payload)
        else:
            print("Message delivery not confirmed.")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nSimulation stopped.")

finally:
    client.disconnect()
    client.loop_stop()	