# Form Submissions and File Handling

> **Course**: Fastapi | **Module**: Advanced Features | **Difficulty**: intermediate

---

### 1. Form Data
```python
from fastapi import Form
# pip install python-multipart

@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    return {"username": username}
```

### 2. File Upload
```python
from fastapi import File, UploadFile

@app.post("/upload")
async def upload(file: UploadFile):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents),
            "content_type": file.content_type}
```

### 3. File + Form Together
```python
@app.post("/profile")
async def update_profile(
    username: Annotated[str, Form()],
    avatar: UploadFile,
):
    return {"username": username, "avatar": avatar.filename}
```

### 4. Multiple Files
```python
@app.post("/multi-upload")
async def multi(files: list[UploadFile]):
    return [{"name": f.filename, "type": f.content_type} for f in files]
```

### 5. File Size Limit
```python
@app.post("/safe-upload")
async def safe_upload(file: UploadFile):
    MAX = 5 * 1024 * 1024  # 5MB
    content = await file.read(MAX + 1)
    if len(content) > MAX:
        raise HTTPException(413, "File too large")
    # Save
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(content)
    return {"saved": file.filename}
```

---

Build a document upload endpoint that accepts: title (form), description (form), file (≤10MB, PDF/DOCX only). Save with UUID filename, return download URL.

---
