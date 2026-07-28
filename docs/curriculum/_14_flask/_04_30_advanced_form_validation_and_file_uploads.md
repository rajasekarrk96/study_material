---
id: "04_30"
title: "Advanced Form Validation and File Uploads"
course: "Flask"
module: 4
module_title: "Advanced Flask Patterns"
lesson: 30
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["WTForms", "FileField", "validators", "secure-filename", "werkzeug", "file-size", "MIME-check", "multipart", "save"]
prerequisites: []
lab_required: true
---


# Advanced Form Validation and File Uploads

## Topics Covered

### 1. WTForms File Field
```python
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, validators

class UploadForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=2, max=50)])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
    ])
```

### 2. Secure File Handling
```python
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
MAX_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and            filename.rsplit('.', 1)[1].lower() in ALLOWED

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'error': 'No file'}, 400
    file = request.files['file']
    if file.filename == '':
        return {'error': 'Empty filename'}, 400
    if not allowed_file(file.filename):
        return {'error': 'File type not allowed'}, 415
    # Check file size
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    if size > MAX_SIZE:
        return {'error': 'File too large'}, 413
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return {'filename': filename}, 201
```

### 3. MIME Type Validation
```python
import magic  # python-magic

def validate_mime(file_stream):
    header = file_stream.read(2048)
    file_stream.seek(0)
    mime = magic.from_buffer(header, mime=True)
    return mime in ['image/jpeg', 'image/png', 'application/pdf']
```

### 4. Multiple File Uploads
```python
@app.route('/multi-upload', methods=['POST'])
def multi_upload():
    files = request.files.getlist('files[]')
    saved = []
    for file in files:
        if file and allowed_file(file.filename):
            fn = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, fn))
            saved.append(fn)
    return jsonify({'uploaded': saved})
```

### 5. Custom Validators
```python
from wtforms import ValidationError

def validate_image_size(form, field):
    if field.data:
        field.data.seek(0, 2)
        size = field.data.tell()
        field.data.seek(0)
        if size > 2 * 1024 * 1024:
            raise ValidationError('Image must be under 2MB')
```

## Lab Exercise
Build a profile photo upload system with: file type restriction, 5MB size limit, MIME validation, UUID-based filenames, and thumbnail generation with Pillow.
