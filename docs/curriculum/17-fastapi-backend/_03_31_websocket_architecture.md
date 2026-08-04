# WebSocket Architecture

> **Course**: Fastapi | **Module**: Advanced Features | **Difficulty**: advanced

---

### 1. Basic WebSocket Endpoint
```python
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo [{client_id}]: {data}")
    except WebSocketDisconnect:
        print(f"Client {client_id} disconnected")
```

### 2. Connection Manager (Broadcast)
```python
class ConnectionManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active.remove(ws)

    async def broadcast(self, message: str):
        for connection in self.active:
            await connection.send_text(message)

    async def send_to(self, ws: WebSocket, message: str):
        await ws.send_text(message)

manager = ConnectionManager()

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            msg = await websocket.receive_text()
            await manager.broadcast(f"[broadcast] {msg}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A user left")
```

### 3. Sending JSON
```python
await websocket.send_json({"type": "message", "data": "hello"})
data = await websocket.receive_json()
```

### 4. WebSocket Authentication
```python
@app.websocket("/ws-auth")
async def ws_auth(websocket: WebSocket, token: str = Query(...)):
    user = verify_token(token)
    if not user:
        await websocket.close(code=1008)
        return
    await websocket.accept()
    ...
```

---

Build a real-time chat application with rooms: users join by room name, messages broadcast only within rooms, user join/leave notifications, and token-based auth.

---
