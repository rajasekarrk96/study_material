# Web Architecture And Protocols

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 50 Minutes (15m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: None
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain the Client-Server model and trace the full lifecycle of a web Request-Response cycle.
2. Analyze HTTP/HTTPS protocols, headers, request methods, and status codes using Chrome DevTools and `cURL`.
3. Differentiate between Web Servers (Nginx/Apache) and Application Servers (Gunicorn/Uvicorn).
4. Trace step-by-step Domain Name System (DNS) resolution from browser cache to Root, TLD, and Authoritative Name Servers.
5. Deconstruct Universal Resource Identifiers (URIs) into Scheme, Host, Port, Path, Query Parameters, and Anchors.

---

---

To complete the practical exercises in this lesson, ensure you have the following tools installed on your workstation:

```bash
# Verify cURL installation
curl --version

# Verify Python installation (for running a local HTTP server)
python --version
```

> [!NOTE]
> All modern operating systems (Windows 10/11, macOS, Linux) include `curl` by default. Google Chrome or Firefox with built-in Developer Tools (F12) is required.

---

---

### 3.1 Client-Server Architecture
The foundational paradigm of the World Wide Web is the **Client-Server Architecture**. In this architecture:
- **Client (User Agent)**: Initiates communications by sending a request for resources (HTML pages, JSON APIs, media assets). Examples include web browsers, mobile apps, or IoT edge nodes.
- **Server**: Listens continuously on dedicated network ports (Port 80 for HTTP, Port 443 for HTTPS), processes client requests, applies security authentication, executes business logic, and returns a structured response payload.

### 3.2 The Request-Response Cycle
Every interaction on the web operates on a stateless Request-Response loop built on top of the **TCP/IP network protocol stack**:
1. **TCP Connection Setup (3-Way Handshake)**: `SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`.
2. **TLS Handshake (HTTPS only)**: Negotiates cipher suites, exchanges cryptographic keys, and validates TLS certificates.
3. **HTTP Request Transmission**: Client sends request line, headers, and optional body.
4. **Server Processing**: Web server routes request to application handlers or static storage.
5. **HTTP Response Return**: Server responds with status code, response headers, and content payload.
6. **Connection Termination / Keep-Alive**: Connection closes or stays open for subsequent pipelined requests.

### 3.3 HTTP vs HTTPS Protocols
- **HTTP (Hypertext Transfer Protocol)**: An application-layer protocol that transmits data in plaintext over TCP Port 80. Susceptible to eavesdropping and Man-in-the-Middle (MitM) attacks.
- **HTTPS (HTTP Secure)**: Encapsulates HTTP payloads within **TLS (Transport Layer Security)** encryption over TCP Port 443. Provides:
  - **Confidentiality**: Symmetric encryption (AES-128/256) protects data in transit.
  - **Integrity**: Message Authentication Codes (HMAC) prevent data tampering.
  - **Authentication**: Digital certificates issued by Certificate Authorities (CAs) verify server identity.

### 3.4 HTTP Request Methods (Verbs)
HTTP defines standardized semantics for client actions:

| Method | Idempotent | Safe | Primary Purpose | Example Use Case |
| :--- | :---: | :---: | :--- | :--- |
| **GET** | Yes | Yes | Retrieve resource representations without side-effects. | Fetching `index.html` |
| **POST** | No | No | Submit data to be processed; creates new resources. | Submitting a registration form |
| **PUT** | Yes | No | Completely replace a target resource payload. | Updating entire user profile |
| **PATCH** | No | No | Apply partial modifications to a resource. | Updating user status flag |
| **DELETE** | Yes | No | Remove specified resource target. | Deleting a sensor reading |
| **OPTIONS**| Yes | Yes | Query permitted HTTP methods for a resource (CORS). | Pre-flight security check |
| **HEAD** | Yes | Yes | Fetch HTTP response headers only (no payload body). | Checking asset last-modified date |

> [!IMPORTANT]
> **Idempotency**: An HTTP method is idempotent if executing it multiple times produces the exact same server state as executing it once. `GET`, `PUT`, and `DELETE` are idempotent; `POST` is not.

### 3.5 HTTP Status Codes Classification
Status codes are 3-digit integers returned by servers to indicate request outcomes:

```
1xx Informational ──► 100 Continue, 101 Switching Protocols
2xx Success       ──► 200 OK, 201 Created, 204 No Content
3xx Redirection   ──► 301 Moved Permanently, 302 Found, 304 Not Modified
4xx Client Error  ──► 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests
5xx Server Error  ──► 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout
```

### 3.6 Web Servers vs Application Servers
- **Web Server (e.g., Nginx, Apache, Caddy)**: Optimized for handling high-concurrency static assets (HTML, CSS, images), SSL/TLS termination, reverse proxying, load balancing, and rate limiting.
- **Application Server (e.g., Gunicorn, Uvicorn, Tomcat, Node.js)**: Executes dynamic application runtime code (Python, Java, JavaScript), interacts with databases, and executes business logic.

```
[ Browser Client ] ──(HTTPS)──► [ Nginx Web Server ] ──(Unix Socket / Reverse Proxy)──► [ Gunicorn App Server ] ──► [ Database ]
```

### 3.7 Identifiers: URI, URL, and URN
- **URI (Uniform Resource Identifier)**: The umbrella super-class identifying any resource.
- **URL (Uniform Resource Locator)**: Specifies the location and protocol to retrieve a resource.  
  *Syntax*: `scheme://username:password@host:port/path?query#fragment`
- **URN (Uniform Resource Name)**: Identifies a resource by name in a persistent namespace without specifying location. Example: `urn:isbn:978-0131103627`.

### 3.8 Domain Name System (DNS) Resolution Tracing
DNS maps human-readable domain names (`example.com`) to machine-routable IP addresses (`93.184.216.34` / `2606:2800:220:1:248:1893:25c8:1946`).

```
Browser Cache ──► OS Resolver Cache ──► Router Cache ──► ISP Recursive Resolver
                                                                  │
┌─────────────────────────────────────────────────────────────────┘
├─► Root Name Server (.) ──────────► Returns TLD Server (.com)
├─► TLD Name Server (.com) ────────► Returns Authoritative Server
└─► Authoritative Server (ns1) ────► Returns IPv4 (A) / IPv6 (AAAA) Record
```

---

---

### DNS Resolution & HTTP Request Sequence
```mermaid
sequenceDiagram
    autonumber
    participant Client as Browser (Client)
    participant DNS as Recursive DNS Resolver
    participant WebServer as Nginx Web Server
    participant AppServer as Flask App Server

    Client->>DNS: Query A Record for example.com
    DNS-->>Client: Return IP Address 93.184.216.34
    Note over Client,WebServer: TCP 3-Way Handshake & TLS 1.3 Handshake
    Client->>WebServer: GET /api/v1/telemetry HTTP/1.1 (Headers + Auth Token)
    WebServer->>AppServer: WSGI Dispatch Request
    AppServer-->>WebServer: Return JSON Payload + HTTP 200 OK
    WebServer-->>Client: HTTP/1.1 200 OK (Content-Type: application/json)
```

---

---

### 5.1 Deconstructing Raw HTTP/1.1 Request and Response Payload

#### Raw Client Request
```http
GET /api/v1/sensors/temp-01 HTTP/1.1
Host: api.iotplatform.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0.0.0
Accept: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Cache-Control: no-cache
Connection: keep-alive

```

#### Raw Server Response
```http
HTTP/1.1 200 OK
Date: Tue, 28 Jul 2026 15:50:00 GMT
Server: nginx/1.24.0
Content-Type: application/json; charset=utf-8
Content-Length: 87
Connection: keep-alive
Access-Control-Allow-Origin: *
Strict-Transport-Security: max-age=31536000; includeSubDomains

{
  "sensor_id": "temp-01",
  "temperature_celsius": 24.5,
  "status": "online",
  "timestamp": 1785253800
}
```

### 5.2 Command Line Inspection with cURL

```bash
# 1. Inspect HTTP Response Headers (-I flag)
curl -I https://jsonplaceholder.typicode.com/posts/1

# 2. Verbose Trace including DNS, TLS Handshake, and Headers (-v flag)
curl -v https://jsonplaceholder.typicode.com/posts/1

# 3. Sending a POST Request with JSON Body (-X POST, -H header, -d body)
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "IoT Sensor Event", "body": "Temperature threshold exceeded", "userId": 1}'
```

---

---

### Case Study: High-Throughput IoT Gateway Architecture
In production enterprise IoT platforms (such as AWS IoT Core or Siemens MindSphere):
- **Microcontrollers & Edge Nodes** send rapid status telemetry using lightweight `POST` or MQTT calls.
- **Nginx Reverse Proxies** process incoming HTTPS connections at the edge, performing SSL decryption and rate-limiting abusive IP addresses.
- Requests are proxied internally via unix sockets to **FastAPI / Flask Application Instances** scale-balanced across Gunicorn worker threads.

> [!TIP]
> Always enable HTTP/2 or HTTP/3 on Nginx proxies to allow header compression (HPACK) and multiplexing over a single TCP connection, reducing IoT gateway CPU load by up to 40%.

---

---

### Task: Inspect Web Request Lifecycle using Chrome DevTools & Python

#### Step 1: Start a Local HTTP Web Server
Open your terminal and launch a local web server using Python:

```bash
python -m http.server 8000
```
*Output*: `Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...`

#### Step 2: Inspect Requests via Chrome DevTools
1. Open Google Chrome and press `F12` (or `Ctrl+Shift+I` / `Cmd+Option+I`) to open Developer Tools.
2. Click on the **Network** tab.
3. Check the **Disable cache** checkbox.
4. Navigate to `http://localhost:8000` in the Chrome address bar.

#### Step 3: Analyze Network Tab Metrics
1. Click on `localhost` in the Name panel.
2. Under **Headers**:
   - Verify Request URL (`http://localhost:8000/`)
   - Verify Request Method (`GET`)
   - Verify Status Code (`200 OK`)
3. Under **Waterfall**:
   - Hover over the timeline to inspect **DNS Lookup**, **Initial Connection**, and **Waiting for server response (TTFB - Time to First Byte)**.

---

---

| Symptom / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`405 Method Not Allowed`** | Client sent HTTP method (e.g., `POST`) to an endpoint that only handles `GET`. | Update backend router decorators or change client request method to match endpoint specification. |
| **`502 Bad Gateway`** | Nginx reverse proxy cannot communicate with upstream Gunicorn/Uvicorn app server. | Check if Python application service is running (`systemctl status gunicorn` or check socket file permissions). |
| **`CORS Error (Access-Control-Allow-Origin missing)`** | Browser blocked cross-origin JavaScript request because server lacks CORS headers. | Configure web server or API middleware to output `Access-Control-Allow-Origin: *` or specific client domain. |
| **`ERR_CERT_COMMON_NAME_INVALID`** | SSL/TLS certificate domain mismatch or self-signed certificate untrusted by browser. | Issue valid SSL certificate using Let's Encrypt / Certbot or import CA root certificate. |

---

---

- **Use Persistent Connections**: Include `Connection: keep-alive` in HTTP/1.1 headers to reuse existing TCP connections.
- **Implement Strict Transport Security (HSTS)**: Send `Strict-Transport-Security: max-age=31536000; includeSubDomains` header to force browsers to always use HTTPS.
- **Leverage 304 Not Modified**: Use `ETag` and `If-None-Match` headers to allow browsers to serve cached assets without re-downloading payloads.
- **Set Explicit Status Codes**: Never return `200 OK` with an error message payload (`{"error": "Unauthorized"}`); always send proper semantic HTTP status codes (`401 Unauthorized`).

---

---

### Q1: What happens under the hood when you type `https://example.com` into a browser address bar and press Enter?
**Answer**:
1. **URL Parsing**: Browser parses scheme (`https`), host (`example.com`), and default port (`443`).
2. **DNS Resolution**: Checks Browser cache $\rightarrow$ OS cache $\rightarrow$ Router $\rightarrow$ ISP Recursive DNS (queries Root, TLD, Authoritative NS) to resolve IP address.
3. **TCP 3-Way Handshake**: Client sends `SYN`, Server returns `SYN-ACK`, Client completes with `ACK` to open TCP socket.
4. **TLS 1.3 Handshake**: Client and Server exchange key shares, validate SSL certificate, and establish encrypted session keys.
5. **HTTP GET Request**: Browser sends GET request with headers (`Host`, `User-Agent`, `Accept`).
6. **Server Processing & Response**: Nginx / App server processes request and returns `200 OK` with HTML body.
7. **DOM Construction & Rendering**: Browser parses HTML, builds DOM/CSSOM, executes JavaScript, and paints the page.

### Q2: What is the technical difference between HTTP `POST`, `PUT`, and `PATCH` methods?
**Answer**:
- `POST` is **non-idempotent** and creates a new resource under a target parent collection. Sending the same POST payload 5 times creates 5 distinct database records.
- `PUT` is **idempotent** and performs a complete replacement of the target resource. If the resource exists, it is completely overwritten; if not, it is created.
- `PATCH` is **non-idempotent** (though can be designed idempotently) and applies partial modifications to an existing resource without touching unspecified fields.

---

---

```json
{
  "quiz_title": "Lesson 1.1 Web Architecture & Protocols Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which HTTP method is defined as idempotent and safe for fetching data without modifying server state?",
      "options": ["POST", "GET", "PATCH", "DELETE"],
      "correct_answer_index": 1,
      "explanation": "GET is both safe (read-only) and idempotent (multiple identical calls produce the same result)."
    },
    {
      "question_id": "Q2",
      "type": "multiple_choice",
      "question_text": "What HTTP status code range indicates a client-side syntax or authentication error?",
      "options": ["2xx", "3xx", "4xx", "5xx"],
      "correct_answer_index": 2,
      "explanation": "4xx status codes (such as 400 Bad Request, 401 Unauthorized, 404 Not Found) denote client-side errors."
    },
    {
      "question_id": "Q3",
      "type": "multiple_choice",
      "question_text": "In DNS resolution hierarchy, which server provides the ultimate authoritative IP record for a specific domain name?",
      "options": ["Root Name Server", "TLD Name Server", "Authoritative Name Server", "ISP Recursive Resolver"],
      "correct_answer_index": 2,
      "explanation": "The Authoritative Name Server holds the actual DNS record mappings (A, AAAA, CNAME) for the domain."
    },
    {
      "question_id": "Q4",
      "type": "multiple_choice",
      "question_text": "What server layer is primarily responsible for SSL/TLS termination, reverse proxying, and serving static assets?",
      "options": ["Application Server (Gunicorn)", "Web Server (Nginx)", "Database Server (MySQL)", "DNS Server"],
      "correct_answer_index": 1,
      "explanation": "Web servers like Nginx are optimized for handling high-concurrency connections, static files, and reverse proxying."
    },
    {
      "question_id": "Q5",
      "type": "multiple_choice",
      "question_text": "Which URI component specifies the exact path to a resource on a server?",
      "options": ["Scheme", "Host", "Path", "Query Parameter"],
      "correct_answer_index": 2,
      "explanation": "In 'http://example.com/api/v1/data', '/api/v1/data' is the Path identifying the specific endpoint."
    }
  ]
}
```

---

---

### Objective
Write a Python script using the native `urllib.request` library (or `requests`) that queries the public REST API `https://jsonplaceholder.typicode.com/posts/1`, extracts HTTP response status code, content-type header, and prints the parsed JSON title.

### Starter Code
```python
import json
import urllib.request

url = "https://jsonplaceholder.typicode.com/posts/1"

# TODO: Create a Request object with custom User-Agent header
# TODO: Open URL connection using urllib.request.urlopen
# TODO: Extract and print HTTP Status Code and Content-Type header
# TODO: Parse and print JSON payload 'title' field
```

### Success Criteria
- Script executes cleanly without external non-standard dependencies.
- Output displays `Status Code: 200`.
- Successfully extracts and prints the title field from the returned JSON dictionary.

---

---

**Front**: What default network ports are used for unencrypted HTTP and encrypted HTTPS traffic?
**Back**: HTTP uses TCP Port 80; HTTPS uses TCP Port 443.
<!-- flashcard:end -->

**Front**: What is the difference between an Idempotent HTTP method and a Safe HTTP method?
**Back**: A Safe method does not modify server state (read-only, e.g., GET). An Idempotent method can modify state, but repeated requests produce the exact same outcome as a single request (e.g., PUT, DELETE).
<!-- flashcard:end -->

**Front**: What DNS record type maps a domain name to an IPv4 address?
**Back**: An 'A' record maps a domain name to a 32-bit IPv4 address (AAAA records map to 128-bit IPv6 addresses).
<!-- flashcard:end -->

---

---

### Key Takeaways
- **Client-Server Architecture**: Web apps communicate via stateless Request-Response cycles over TCP/IP sockets.
- **HTTP Semantics**: Use `GET` for fetching, `POST` for creating, `PUT` for replacing, `PATCH` for partial updates, and `DELETE` for removal.
- **DNS Hierarchy**: Resolution flows through Browser Cache $\rightarrow$ OS Cache $\rightarrow$ Recursive Resolver $\rightarrow$ Root $\rightarrow$ TLD $\rightarrow$ Authoritative Server.
- **Web vs App Server**: Nginx handles proxying/TLS/static files; Gunicorn/FastAPI executes dynamic code logic.

### Quick Syntax & Command Cheat Sheet

```bash
# Quick HTTP Requests with cURL
curl -I https://example.com                       # Head request (Headers only)
curl -v https://example.com                       # Verbose trace
curl -X DELETE https://api.example.com/items/42   # Send DELETE request

# Start instant HTTP server in current directory
python -m http.server 8000
```

### Official References
- [W3C HTTP/1.1 Specification (RFC 7231)](https://datatracker.ietf.org/doc/html/rfc7231)
- [MDN Web Docs: An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)

---
