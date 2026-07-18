# %% [markdown]
# # Topic 6: The HTTP Protocol Playground
# In this playground, you will learn how to interact with the raw HTTP layer.
# You will extract request headers, set custom response headers, and work with cookies.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import FastAPI, Response, Header, Cookie, status
from fastapi.testclient import TestClient
import json

# %%
# 2. APPLICATION SETUP
app = FastAPI(title="HTTP Deep Dive Service")

# %% [markdown]
# ## Accessing Headers and Cookies
# FastAPI allows you to inject headers and cookies directly into your route functions
# by declaring them as parameters. FastAPI automatically handles case conversion
# (e.g., `User-Agent` becomes the parameter `user_agent`).

# %%
# 3. ROUTE DEFINITIONS

@app.get("/api/v1/inspect")
def inspect_http(
    user_agent: str = Header(None),            # Extracts 'User-Agent'
    x_api_key: str = Header(None),             # Extracts 'X-API-Key'
    session_token: str = Cookie(None)          # Extracts cookie named 'session_token'
):
    return {
        "message": "HTTP details successfully extracted",
        "extracted_headers": {
            "User-Agent": user_agent,
            "X-API-Key": x_api_key
        },
        "extracted_cookies": {
            "session_token": session_token
        }
    }

# %% [markdown]
# ## Setting Response Headers and Cookies
# To modify the response (e.g., adding custom headers, caching directives, or cookies),
# you can inject the `Response` object into your function.

# %%
@app.get("/api/v1/generate-headers")
def generate_headers(response: Response):
    # 1. Set a custom tracking header
    response.headers["X-Request-ID"] = "req_abc123xyz"
    
    # 2. Set a caching header (Cache this response for 60 seconds)
    response.headers["Cache-Control"] = "public, max-age=60"
    
    # 3. Set a cookie (HttpOnly for security!)
    response.set_cookie(
        key="session_token",
        value="token_secret_value_999",
        httponly=True,
        max_age=3600 # 1 hour expiry
    )
    
    return {"message": "Custom headers and cookies have been injected into the response."}

# %%
# 4. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Sending Custom Headers and Cookies
# Let's send a request containing a custom header and cookie, and verify our endpoint extracts them.

# %%
headers_to_send = {
    "User-Agent": "ConsolePlaygroundClient/1.0",
    "X-API-Key": "my-secret-key-123"
}
cookies_to_send = {
    "session_token": "cookie-abc"
}

response = client.get("/api/v1/inspect", headers=headers_to_send, cookies=cookies_to_send)
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 2: Reading Response Headers and Cookies
# Let's hit the `/generate-headers` endpoint and inspect the headers and cookies returned by our server.

# %%
response = client.get("/api/v1/generate-headers")

print("--- Response Headers ---")
for key, val in response.headers.items():
    print(f"{key}: {val}")

print("\n--- Response Cookies ---")
print(dict(response.cookies))
