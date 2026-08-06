# Modules and Packages

> **Course**: Core Python | **Module**: Modules and Packages | **Difficulty**: intermediate

---

```python
import os                        # import whole module
import os.path                   # import sub-module
from os import getcwd, listdir   # import specific names
from os import *                 # import all (avoid!)
import numpy as np               # alias
from pathlib import Path as P    # alias for name

# Conditional import
try:
    import ujson as json
except ImportError:
    import json
```

---

```python
# __name__ — string name of current module
if __name__ == "__main__":
    # Runs only when script is executed directly, not imported
    main()

# __file__ — absolute path of module file
print(__file__)   # /path/to/mymodule.py

# __all__ — controls what `from module import *` exports
__all__ = ["PublicClass", "public_function"]
```

---

```
mypackage/
    __init__.py          # Makes folder a package
    core.py
    utils.py
    database/
        __init__.py
        models.py
        queries.py
```

```python
# mypackage/__init__.py
from .core import MainClass        # relative import
from .utils import helper_func
from .database.models import User

__version__ = "1.0.0"
__all__ = ["MainClass", "helper_func", "User"]
```

---

```python
# Inside mypackage/database/queries.py
from .models import User          # same package
from ..utils import helper_func   # parent package
from ..core import MainClass      # parent package
```

---

```python
import sys

# Python searches for modules in:
# 1. Current directory
# 2. PYTHONPATH env variable
# 3. Standard library
# 4. site-packages (installed packages)

print(sys.path)

# Add custom path at runtime
sys.path.insert(0, "/path/to/my/libraries")
```

---

```python
import importlib

# Import by string name
module = importlib.import_module("os.path")
func = getattr(module, "join")

# Reload a changed module (useful in development)
import my_module
importlib.reload(my_module)

# Plugin system
def load_plugin(name: str):
    return importlib.import_module(f"plugins.{name}")
```

---

1. Create a package `calculator` with `add`, `subtract`, `multiply` in separate modules
2. Implement a plugin system that loads modules by name from a `plugins/` directory
3. Write a `__init__.py` that lazy-imports submodules only on first attribute access

---
