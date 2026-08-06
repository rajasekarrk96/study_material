# Reverse Proxy and Nginx Configuration

> **Course**: Flask | **Module**: Production Deployment | **Difficulty**: advanced

---

### 1. Nginx as Reverse Proxy for Flask
```nginx
# /etc/nginx/sites-available/myapp
upstream flask_app {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name myapp.com www.myapp.com;

    location / {
        proxy_pass http://flask_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /var/www/myapp/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    client_max_body_size 16M;
}
```

### 2. Gunicorn Configuration
```bash
# Install
pip install gunicorn

# Run
gunicorn -w 4 -b 127.0.0.1:8000 "app:create_app()"

# gunicorn.conf.py
workers = 4
worker_class = "gthread"
threads = 2
bind = "127.0.0.1:8000"
timeout = 120
keepalive = 5
accesslog = "/var/log/gunicorn/access.log"
errorlog  = "/var/log/gunicorn/error.log"
```

### 3. SSL/HTTPS with Let's Encrypt
```bash
# Certbot
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d myapp.com -d www.myapp.com
```

```nginx
server {
    listen 443 ssl http2;
    ssl_certificate     /etc/letsencrypt/live/myapp.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myapp.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```

### 4. Flask ProxyFix Middleware
```python
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app,
    x_for=1, x_proto=1, x_host=1, x_prefix=1)
```

### 5. Systemd Service
```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/var/www/myapp/venv/bin/gunicorn --config gunicorn.conf.py "app:create_app()"
Restart=always

[Install]
WantedBy=multi-user.target
```

---

Deploy a Flask app with Nginx + Gunicorn + HTTPS on a Ubuntu VPS. Configure static file serving, SSL, and verify headers with `curl -I`.

---
