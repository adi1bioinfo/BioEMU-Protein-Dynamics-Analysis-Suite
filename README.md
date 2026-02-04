# BioEMU Analysis Suite: Comprehensive Protein Dynamics Analysis

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


**A complete, production-ready analysis suite for protein molecular dynamics simulations with support for both BioEMU and classical all-atom MD trajectories**

[Quick Start](#quick-start) • [Features](#features) • [Installation](#installation) • [Documentation](#documentation) • [Examples](#examples) • [Publications](#publications)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Why BioEMU?](#why-bioemu)
- [Directory Structure](#directory-structure)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Available Analyses](#available-analyses)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)

---

## Overview

The **BioEMU Analysis Suite** is a comprehensive toolkit for analyzing protein molecular dynamics simulations from multiple methodologies. This suite supports analysis of trajectories from [BioEMU](https://github.com/your-bioemu-repo) simulations, classical all-atom molecular dynamics (using GROMACS, AMBER, NAMD), and other MD engines.

By combining analyses from different methodologies, researchers can leverage the computational efficiency of coarse-grained approaches while maintaining the atomic detail provided by classical simulations. This integrated framework enables a more comprehensive understanding of protein dynamics across multiple scales.

---

## Why BioEMU?

This suite is designed to integrate **BioEMU**—a state-of-the-art generative deep learning model—with classical MD workflows.

### The Power of BioEMU
BioEMU rapidly samples thousands of physically-plausible protein conformations from sequence input, bypassing the need for long, resource-intensive molecular dynamics simulations.

| Feature | Classical MD | BioEMU |
|---------|--------------|--------|
| **Time to Conformers** | Weeks to months | Minutes to hours |
| **Sample Diversity** | Limited by sampling time | Diverse equilibrium ensembles |
| **Computational Cost** | HPC-required | Single GPU workstation |
| **Best For** | Detailed atomic interactions | Large-scale ensemble generation |

### Integrated Workflow
1. **Generate** ensemble with BioEMU (hours)
2. **Analyze** with this suite (minutes)
3. **Identify** interesting conformations
4. **Validate** with classical MD (optional)
5. **Publish** results

For more details on setting up BioEMU, please refer to the [official BioEMU repository](https://github.com/Standard-Deviations/BioEMU).

---

## Directory Structure

The project is organized for clarity and maintainability:

```text
BioEMU-Protein-Dynamics-Analysis-Suite/
├── src/
│   └── bioemu_analysis/       # Core analysis modules
│       ├── trajectory_loader.py
│       ├── analysis_functions.py
│       ├── visualization.py
│       └── __init__.py
├── examples/                  # Examples & Unified Guide
│   ├── kdel_analysis/         # Ready-to-run KDEL example
│   └── README.md              # Examples & Analysis Guide
├── results/                   # Output directory
├── Comprehensive_Analysis.ipynb  # MAIN ANALYSIS NOTEBOOK
├── pyproject.toml             # Project configuration
├── tests/                     # Automated tests
├── README.md                  # This file
├── LICENSE                    # MIT License
└── .gitignore
```

---

## Key Features

### ✨ Comprehensive Analysis Suite

1. **Structural Dynamics**: RMSD, RMSF, Inter-helical distance & angle
2. **Solvation Analysis**: SASA, Pore hydration, Water bridges
3. **Interaction Analysis**: Hydrogen bond detection, Minimum distances, Contact analysis
4. **Advanced Features**: Multi-system comparison, Publication-quality plots, Statistical summaries

### 🎯 Design Philosophy

- **Flexible**: Works with any protein (GPCR, Ion Channel, Aquaporin, etc.)
- **Accessible**: No coding required - single configuration dictionary
- **Robust**: Handles GROMACS, AMBER, MDTraj-compatible formats
- **Publication-Ready**: High-resolution plots, statistics, error estimation

---

## Installation

### Quick Installation

```bash
# 1. Clone the repository
git clone https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite.git
cd BioEMU-Protein-Dynamics-Analysis-Suite

# 2. Install package in editable mode
pip install -e .

# 3. (Optional) Enable BioEMU MD relaxation
pip install "bioemu[md]>=1.0.0"

# 4. Verify installation
python -c "import MDAnalysis as mda; import bioemu; print('✓ Installation successful')"
```

For advanced installation options, check `pyproject.toml`.

---

## Quick Start

### Option 1: Run the Example (Ready-to-Go)
We provide a 10ns simulation of the **KDEL Receptor** so you can test the suite immediately.

1.  Open `Comprehensive_Analysis.ipynb` in Jupyter.
2.  In the **Configuration** cell, import the example config:
    ```python
    import sys
    sys.path.append('./examples/kdel_analysis')
    from kdel_config import CONFIG
    ```
3.  Run all cells to generate plots in `results/`.

### Option 2: Analyze Your Own Data
1.  Edit the `CONFIG` dictionary in the notebook to point to your files:
    ```python
    CONFIG = {
        "protein_name": "My Protein",
        "output_dir": "./results",
        "systems": {
            "wild_type": {
                "label": "My BioEMU Ensemble",
                "topology": "/path/to/my_system/structure.pdb",
                "trajectory": "/path/to/my_system/ensemble.xtc",
                "color": "#FF6B6B",
            }
        },
        # ...
    }
    ```

---

## Available Analyses

| Analysis | Description | Use Case |
|----------|-------------|----------|
| **RMSD** | Root Mean Square Deviation | Stability check, equilibration time |
| **RMSF** | Root Mean Square Fluctuation | Identification of flexible loops/regions |
| **Inter-Helical** | Distance & Angle | Domain dynamics, conformational changes |
| **SASA** | Solvent Accessible Surface Area | Buried vs. exposed residues, hydration |
| **Pore Hydration** | Water occupancy in cavities | Channel/transporter gating mechanisms |
| **Water Bridges** | Water-mediated contacts | Stability mechanisms |
| **Contacts** | Min Distance / H-Bonds | Interaction networks, salt bridges |

---

## Documentation

- **[examples/README.md](examples/README.md)**: Detailed guide on running examples and interpreting analysis plots (RMSD, SASA, etc.).
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Guide for developers.

For BioEMU installation, please refer to the official [BioEMU Repository](https://github.com/microsoft/bioemu).

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Citation

If you use this analysis suite in your research, please cite:

```bibtex
@article{lin2024scalable,
  title={Scalable emulation of protein equilibrium ensembles},
  author={Lin, Ze and Frey, Nathaniel C. and others},
  journal={Nature Methods},
  year={2024}
}

@software{bioemu_analysis_2026,
  author = {Laddha, Aditi},
  title = {BioEMU Analysis Suite: Comprehensive Protein Dynamics Analysis},
  year = {2026},
  url = {https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the structural biology community**

⭐ **If you find this useful, please star this repository!** ⭐

</div>
