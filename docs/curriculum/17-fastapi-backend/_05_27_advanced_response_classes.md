---
id: "27"
title: "Advanced Response Classes"
course: "FastAPI"
module: 3
module_title: "Advanced Features"
lesson: 27
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["JSONResponse", "HTMLResponse", "PlainTextResponse", "RedirectResponse", "FileResponse", "StreamingResponse", "ORJSONResponse"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Response Class Variants
```python
from fastapi.responses import (
    JSONResponse, HTMLResponse, PlainTextResponse,
    RedirectResponse, FileResponse, StreamingResponse
)

@app.get("/html", response_class=HTMLResponse)
async def html():
    return "<h1>Hello</h1>"

@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello, plain world"

@app.get("/redirect")
async def redirect():
    return RedirectResponse(url="/new-location", status_code=302)

@app.get("/file")
async def file():
    return FileResponse("report.pdf", media_type="application/pdf",
                        filename="download.pdf")
```

### 2. Streaming Response
```python
import asyncio

async def generate():
    for i in range(100):
        yield f"chunk {i}\n".encode()
        await asyncio.sleep(0.01)

@app.get("/stream")
async def stream():
    return StreamingResponse(generate(), media_type="text/plain")
```

### 3. ORJSONResponse (faster)
```python
from fastapi.responses import ORJSONResponse
# pip install orjson

@app.get("/fast", response_class=ORJSONResponse)
async def fast():
    return {"data": list(range(1000))}
```

### 4. Custom Headers in Response
```python
@app.get("/custom-headers")
async def custom():
    content = {"message": "ok"}
    headers = {"X-Custom-Header": "value", "Cache-Control": "no-cache"}
    return JSONResponse(content=content, headers=headers)
```

## Lab
Build an export endpoint that: returns CSV for `?format=csv`, JSON for `?format=json`, triggers file download for `?format=excel` — all from the same data source.
