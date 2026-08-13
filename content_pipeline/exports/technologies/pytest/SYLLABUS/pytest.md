# PyTest & Python Testing Practices — Master Syllabus

**Target Role:** Python Backend Engineer / QA Automation Engineer / Software Engineer in Test  
**Difficulty Level:** Beginner to Intermediate  
**Estimated Duration:** 12 Hours  
**Prerequisites:** foundations/core-python  
**Required Courses:** foundations/core-python  
**Optional Courses:** technologies/fastapi, technologies/flask  

---

## Study Flow

### Module 1 — PyTest Fundamentals & Test Discovery
1. **PyTest Architecture & Test Discovery** (File naming conventions `test_*.py`, function naming, assertion introspection)
2. **PyTest CLI Execution & Flags** (`-v`, `-s`, `-k` expression filtering, `-m` marker filtering, `--maxfail`, `-x` stop on first failure)
3. **Assertions & Exception Testing** (Native `assert`, formatted failure diffs, `pytest.raises`, testing exception messages with regex)

### Module 2 — PyTest Fixtures & Dependency Injection
1. **Fixture Architecture** (`@pytest.fixture`, setup and teardown via `yield` statements, fixture scopes: `function`, `class`, `module`, `session`)
2. **Fixture Composition & `autouse`** (Injecting fixtures into other fixtures, cascading dependency injection, automatic fixture execution)
3. **Fixture Factories & Parametrization** (Returning callable factory functions from fixtures, parameterized fixtures `params`)

### Module 3 — Parametrization & Custom Markers
1. **Function Parametrization** (`@pytest.mark.parametrize`, multi-argument parametrization, testing edge cases and boundary conditions)
2. **Built-in Markers** (`@pytest.mark.skip`, `@pytest.mark.skipif`, `@pytest.mark.xfail`)
3. **Custom Markers & Configuration** (Registering markers in `pytest.ini` / `pyproject.toml`, custom CLI options)

### Module 4 — Mocking, Monkeypatching & Async Testing
1. **Mocking Dependencies** (`unittest.mock.Mock`, `MagicMock`, `pytest-mock` wrapper `mocker`)
2. **Monkeypatching Configuration & Environment** (`monkeypatch.setenv`, `monkeypatch.setattr`, mocking API responses)
3. **Asynchronous Testing** (`pytest-asyncio`, testing async coroutines and async fixtures)

### Module 5 — Coverage Analysis, Plugins & CI Integration
1. **Code Coverage with `pytest-cov`** (Generating line and branch coverage reports, HTML coverage reports, fail-under threshold)
2. **PyTest Plugins Ecosystem** (`pytest-xdist` parallel test execution, `pytest-sugar`, `pytest-benchmark`)
3. **CI/CD Integration** (Running PyTest in GitHub Actions workflows, publishing test results)
