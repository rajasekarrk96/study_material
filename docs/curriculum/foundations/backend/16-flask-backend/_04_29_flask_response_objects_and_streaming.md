---
id: "04_29"
title: "Flask Response Objects and Streaming"
course: "Flask"
module: 4
module_title: "Advanced Flask Patterns"
lesson: 29
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["Response", "make-response", "headers", "mimetype", "stream-with-context", "stream_template", "chunked", "SSE", "server-sent-events"]
prerequisites: []
lab_required: true
---


# Flask Response Objects and Streaming

## Topics Covered

### 1. Response Object Basics
- `make_response()` — creating custom response objects
- Setting headers: `response.headers['X-Custom'] = 'value'`
- Setting cookies: `response.set_cookie('key', 'val', httponly=True)`
- Status codes and MIME types
- `Response(content, status, headers, mimetype)`

### 2. Streaming Responses
```python
from flask import Response, stream_with_context
import time

def generate():
    for i in range(10):
        yield f"data: Line {i}\n\n"
        time.sleep(0.5)

@app.route('/stream')
def stream():
    return Response(stream_with_context(generate()),
                    mimetype='text/event-stream')
```

### 3. Server-Sent Events (SSE)
```python
@app.route('/events')
def events():
    def event_stream():
        while True:
            data = get_new_data()
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(1)
    return Response(event_stream(), mimetype='text/event-stream',
                    headers={'Cache-Control': 'no-cache',
                             'X-Accel-Buffering': 'no'})
```

### 4. File Streaming
```python
from flask import send_file, send_from_directory

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

# Stream large files
@app.route('/large-file')
def large():
    def generate_chunks():
        with open('large.bin', 'rb') as f:
            while chunk := f.read(8192):
                yield chunk
    return Response(generate_chunks(), mimetype='application/octet-stream')
```

### 5. JSON Responses
```python
from flask import jsonify
# Flask auto-serializes dicts in return
@app.route('/api/data')
def data():
    return {"key": "value"}, 200  # shorthand
    # OR
    return jsonify({"key": "value"})
```

## Lab Exercise
Build a live log streaming endpoint using SSE that tails a log file and pushes new lines to a browser client using `EventSource`.
