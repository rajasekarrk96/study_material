"""
Learning OS — Sandbox Execution Service
Handles code compilation & execution via Judge0 API, with local subprocess fallback.
"""
import os
import subprocess
import tempfile
import requests
import logging

logger = logging.getLogger("learning_os.sandbox")

# Language mapping to Judge0 IDs
LANGUAGE_IDS = {
    "python": 71,      # Python (3.8.1)
    "javascript": 63,  # Node.js (12.14.0)
    "c": 50,           # GCC (9.2.0)
    "cpp": 54          # GCC (9.2.0)
}


class SandboxService:
    def __init__(self):
        self.api_url = os.environ.get("JUDGE0_API_URL", "https://api.judge0.com").rstrip("/")
        self.api_key = os.environ.get("JUDGE0_API_KEY", "")

    def execute_code(self, source_code: str, language: str, input_data: str = "") -> dict:
        """Executes code via Judge0 or falls back to local execution."""
        lang_id = LANGUAGE_IDS.get(language.lower())
        
        # If API key is present, try remote Judge0 execution
        if self.api_key and lang_id:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "X-RapidAPI-Key": self.api_key,
                    "X-RapidAPI-Host": "judge0-extra-ce.p.rapidapi.com"
                }
                payload = {
                    "source_code": source_code,
                    "language_id": lang_id,
                    "stdin": input_data
                }
                
                # Make wait=true request for synchronous results
                url = f"{self.api_url}/submissions?wait=true"
                response = requests.post(url, json=payload, headers=headers, timeout=10)
                if response.status_code == 201 or response.status_code == 200:
                    data = response.get_json() or response.json()
                    status_desc = data.get("status", {}).get("description", "").lower()
                    
                    return {
                        "status": "accepted" if "accepted" in status_desc else "wrong_answer",
                        "stdout": data.get("stdout") or "",
                        "stderr": data.get("stderr") or data.get("compile_output") or "",
                        "remote": True
                    }
            except Exception as e:
                logger.error(f"Remote Judge0 execution failed: {e}. Falling back to local execution.")

        # Fallback to local subprocess execution
        return self._execute_locally(source_code, language, input_data)

    def _execute_locally(self, source_code: str, language: str, input_data: str) -> dict:
        """Isolated local execution for Python (primary fallback)."""
        if language.lower() != "python":
            return {
                "status": "compile_error",
                "stdout": "",
                "stderr": f"Local execution is only supported for Python. Judge0 is required for {language}.",
                "remote": False
            }

        try:
            # Write code to temporary file
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w", encoding="utf-8") as f:
                f.write(source_code)
                temp_filename = f.name

            try:
                # Run the Python process safely with a timeout of 5 seconds
                proc = subprocess.run(
                    ["python", temp_filename],
                    input=input_data,
                    text=True,
                    capture_output=True,
                    timeout=5
                )
                
                status = "accepted" if proc.returncode == 0 else "runtime_error"
                return {
                    "status": status,
                    "stdout": proc.stdout,
                    "stderr": proc.stderr,
                    "remote": False
                }
            except subprocess.TimeoutExpired:
                return {
                    "status": "time_limit_exceeded",
                    "stdout": "",
                    "stderr": "Execution timed out (Limit: 5 seconds).",
                    "remote": False
                }
            finally:
                # Clean up temporary file
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
        except Exception as e:
            return {
                "status": "runtime_error",
                "stdout": "",
                "stderr": str(e),
                "remote": False
            }
