# Firebase SDK in Python

> **Course**: Firebase | **Module**: Firebase Introduction | **Difficulty**: beginner

---

Using Pyrebase and Firebase Admin SDKs in Python for IoT gateway data ingestion and analytics.

---



---

Python gateways aggregate local sensor data (via MQTT/Zigbee) and push structured data to Firebase.

---

Pyrebase Data Push:
db.child('telemetry').push({'temp': 22.4})

---

### Streaming Real-Time Updates in Python

```python
def stream_handler(message):
    print('Data changed:', message['data'])

my_stream = db.child('controls').stream(stream_handler)
```

---

Blocking main execution thread while waiting for network responses.

---

**Q1: Difference between `.set()` and `.push()` in Firebase?**
A: `.set()` overwrites data at path; `.push()` appends unique timestamped child node.

---



---



---



---



---
