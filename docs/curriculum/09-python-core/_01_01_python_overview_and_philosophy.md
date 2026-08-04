# Python Overview and Philosophy

> **Course**: Core Python | **Module**: Setup and Overview | **Difficulty**: beginner

---

Python is a **high-level, interpreted, dynamically typed** programming language created by Guido van Rossum (1991). It emphasises **readability** and expressiveness over verbosity.

> "There should be one — and preferably only one — obvious way to do it." — The Zen of Python

---

```python
import this  # Prints The Zen of Python
```

Key principles:
- **Beautiful is better than ugly** — code should be readable
- **Explicit is better than implicit** — no magic unless necessary
- **Simple is better than complex** — prefer straightforward solutions
- **Readability counts** — code is read more often than written

---

| Version | Key Features | Status |
|---|---|---|
| Python 2.x | Old syntax, `print` statement | EOL 2020 |
| Python 3.6 | f-strings, secrets module | EOL |
| Python 3.10 | Match/case (structural pattern matching) | EOL |
| Python 3.11 | 60% faster, better error messages | Supported |
| Python 3.12 | Type aliases, f-string improvements | Active LTS |
| Python 3.13 | Free-threaded mode (no GIL) | Latest |

---

| Domain | Tools |
|---|---|
| Web Development | Flask, FastAPI, Django |
| Data Science | NumPy, Pandas, Matplotlib |
| Machine Learning | scikit-learn, TensorFlow, PyTorch |
| Automation / Scripting | subprocess, pathlib, os |
| Embedded / IoT | MicroPython, CircuitPython |
| DevOps | Ansible, Fabric, boto3 |

---

| Interpreter | Language | Use Case |
|---|---|---|
| **CPython** | C | Default, most compatible |
| PyPy | Python + JIT | Speed-critical scripts |
| MicroPython | C | Microcontrollers |
| Jython | Java | JVM integration |
| GraalPy | GraalVM | Polyglot projects |

---

1. Run `python --version` and `python -c "import this"`
2. Open the REPL and evaluate: `2**32`, `"hello"*3`, `type(3.14)`
3. Write a one-liner that prints the first 10 Fibonacci numbers

---
