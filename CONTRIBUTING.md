# Contributing to BioEMU Analysis Suite

First off, thank you for considering contributing to BioEMU Analysis Suite! It's people like you that make this such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [issue list](https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite/issues) as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**
* **Include your environment details** (OS, Python version, package versions)

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite/issues). When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior** and **the expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Follow the Python [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
* Include appropriate test cases
* Update documentation as needed
* End all files with a newline

---

## Development Setup

1. **Fork the repository** on GitHub

2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/your-username/BioEMU-Protein-Dynamics.git
   cd BioEMU-Protein-Dynamics
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv dev-env
   source dev-env/bin/activate
   ```

4. **Install development dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov black pylint
   ```

5. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

6. **Make your changes and test:**
   ```bash
   pytest
   ```

7. **Format your code:**
   ```bash
   black .
   ```

8. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add clear description of changes"
   git push origin feature/your-feature-name
   ```

9. **Submit a Pull Request** on GitHub

---

## Style Guide

### Python Code Style

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use `black` for code formatting:
  ```bash
  black your_file.py
  ```
* Use meaningful variable names
* Add docstrings to all functions and classes
* Maximum line length: 100 characters

### Docstring Format

```python
def analyze_trajectory(trajectory_file, selection="protein"):
    """
    Analyze molecular dynamics trajectory.
    
    Parameters
    ----------
    trajectory_file : str
        Path to trajectory file (.xtc, .dcd, etc.)
    selection : str, optional
        Atom selection string (default is "protein")
    
    Returns
    -------
    dict
        Analysis results with keys: 'rmsd', 'rmsf', 'sasa'
    
    Examples
    --------
    >>> results = analyze_trajectory('simulation.xtc')
    >>> print(results['rmsd'].shape)
    """
    pass
```

### Naming Conventions

* **Functions/Variables**: `snake_case`
* **Classes**: `PascalCase`
* **Constants**: `UPPER_SNAKE_CASE`
* **Private functions**: `_leading_underscore`

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=utils

# Run specific test file
pytest tests/test_analysis.py

# Run with verbose output
pytest -v
```

### Writing Tests

Create test files in `tests/` directory with `test_*.py` naming:

```python
import pytest
from utils.analysis import calculate_rmsd

def test_calculate_rmsd():
    """Test RMSD calculation."""
    # Your test code here
    result = calculate_rmsd(trajectory)
    assert result is not None
```

---

## Documentation

* Update [README.md](README.md) for major changes
* Update relevant docs in [docs/](docs/) folder
* Add docstrings to new functions
* Update [ANALYSIS_GUIDE.md](docs/ANALYSIS_GUIDE.md) for new analyses
* Update [API_REFERENCE.md](docs/API_REFERENCE.md) for new APIs

---

## Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add RMSD calculation for multi-system comparison

- Implement vectorized RMSD calculation
- Add unit tests
- Update documentation

Fixes #123
```

---

## Questions?

Feel free to open an issue or start a discussion on GitHub!

---

## Attribution

This CONTRIBUTING guide was adapted from [Atom's Contributing Guide](https://github.com/atom/atom/blob/master/CONTRIBUTING.md).

Thank you for contributing! 🎉
