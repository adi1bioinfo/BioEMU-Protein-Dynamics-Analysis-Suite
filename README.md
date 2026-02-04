# BioEMU Analysis Suite: Comprehensive Protein Dynamics Analysis

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Stars](https://img.shields.io/github/stars/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite)](https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite)

**A complete, production-ready analysis suite for protein molecular dynamics simulations with support for both BioEMU and classical all-atom MD trajectories**

[Quick Start](#quick-start) • [Features](#features) • [Installation](#installation) • [Documentation](#documentation) • [Examples](#examples) • [Publications](#publications)

</div>

## About the Author

**Aditi Laddha — Computational Structural Biologist & Data Scientist**

Aditi is a computational structural biologist and data scientist with expertise in protein dynamics, molecular simulation analysis, and reproducible data workflows. She develops end-to-end analysis pipelines that combine trajectory processing, statistical modeling, and machine learning to extract biologically meaningful insights from simulation data.

**Core Competencies:**
- **Domain:** Protein dynamics, structural bioinformatics, molecular simulations
- **Languages & Tools:** Python, GROMACS, MDAnalysis, MDTraj, NumPy, pandas, SciPy, Matplotlib, Seaborn
- **Machine Learning & Data Science:** scikit-learn, PyTorch (applied to molecular features), feature engineering, statistical modeling
- **Reproducibility & DevOps:** Git, Docker, Conda, CI/CD, automated testing, documentation

**Selected Contributions:**
- Developed the `BioEMU Analysis Suite` for multi-method trajectory analysis and reproducible reporting
- Built publication-quality visualizations and performance-optimized analysis pipelines for large trajectories

**Contact & Profile:**
- GitHub: https://github.com/adi1bioinfo
- Email: adi1bioinfo@gmail.com

---

## Table of Contents

- [Overview](#overview)
- [Simulation Methodologies Supported](#simulation-methodologies-supported)
- [Multi-Method Analysis Framework](#multi-method-analysis-framework)
- [BioEMU Integration](#bioemu-integration)
- [Quick Installation](#quick-installation)
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

### Integrated Multi-Method Approach

This toolkit was developed to facilitate comparative analysis between complementary simulation approaches:
- **BioEMU simulations**: Coarse-grained approach for exploring conformational spaces and functional dynamics
- **Classical all-atom MD (GROMACS)**: Detailed atomic-level simulations for validation and mechanistic insights

By combining analyses from both methodologies, researchers can leverage the computational efficiency of coarse-grained approaches while maintaining the atomic detail provided by classical simulations. This integrated framework enables more comprehensive understanding of protein dynamics across multiple scales.

---

## Simulation Methodologies Supported

### Classical All-Atom Molecular Dynamics

Traditional molecular dynamics simulations (GROMACS, AMBER, NAMD) provide:
- **Atomic-level detail**: Explicit representation of all atoms
- **Well-established methods**: Extensive validation and benchmarking
- **Mechanistic insights**: Detailed understanding of molecular interactions
- **Publication acceptance**: Widely recognized in the research community

### Coarse-Grained Approaches (BioEMU)

Coarse-grained simulation strategies offer:
- **Computational efficiency**: Reduced system size enables longer simulations or faster turnaround
- **Conformational sampling**: Ability to explore larger conformational spaces
- **Functional dynamics**: Identification of large-scale motions and transitions
- **Complementary perspective**: Different view of the same biological system

### Comparative Analysis

This suite is designed for researchers who use **both** methodologies:

```
Use Classical All-Atom MD for:
✓ Detailed atomic interactions
✓ Water-mediated effects
✓ Precise interaction networks
✓ Fine-grained mechanistic understanding

Use Coarse-Grained Methods (BioEMU) for:
✓ Rapid exploration of conformational space
✓ Large-scale functional motions
✓ Extended timescale simulations
✓ Hypothesis generation and screening
```

By analyzing trajectories from both approaches with identical metrics, researchers can gain complementary insights into protein behavior.

---

---

## Directory Structure

The project is organized for clarity and maintainability:

```
BioEMU-Protein-Dynamics-Analysis-Suite/
├── installation/              # Installation & environment setup
│   ├── INSTALL.md            # Consolidated installation guide
│   ├── requirements.txt       # Pip dependencies
│   └── environment.yml        # Conda environment
│
├── src/
│   └── analysis/              # Core analysis modules (python package)
│       ├── __init__.py
│       ├── trajectory_loader.py
│       ├── analysis_functions.py
│       └── visualization.py
│
├── scripts/                   # Utility scripts and setup
│   ├── setup.py
│   └── __init__.py
│
├── docs/
│   ├── API_REFERENCE.md       # API documentation
│   ├── ANALYSIS_GUIDE.md      # Detailed analysis workflows
│   ├── TROUBLESHOOTING.md     # Common issues & solutions
│   ├── GETTING_STARTED.md     # Step-by-step tutorials
│   ├── bioemu_installation/   # BioEMU-specific guides
│   │   └── BIOEMU_SETUP_GUIDE.md
│   └── reference/             # Additional reference documentation
│       ├── BIOEMU_INTEGRATION_GUIDE.md
│       ├── CONFIG_QUICK_REFERENCE.md
│       └── ...
│
├── examples/                  # Example workflows & configurations
│   ├── case_studies/
│   └── ...
│
├── archive/                   # Legacy content
│   └── notebooks/             # Archived notebooks
│
├── data/                      # Sample data (if included)
├── results/                   # Output results directory
├── README.md                  # This file
├── GETTING_STARTED.md         # Quick start guide
├── LICENSE                    # MIT License
└── .gitignore                 # Git ignore rules
```

**Key folders:**
- **`installation/`**: Everything needed to set up your environment (pip or conda)
- **`src/analysis/`**: Core Python analysis package (importable as `from src.analysis import ...`)
- **`docs/`**: User guides, API reference, and troubleshooting
- **`examples/`**: Ready-to-run analysis templates
- **`archive/`**: Legacy notebooks (preserved for reference)

---

## Multi-Method Analysis Framework

This suite enables integrated analysis of trajectories from multiple simulation approaches, allowing you to:
- **Apply consistent metrics** across different simulation methodologies
- **Compare results** from coarse-grained and all-atom simulations
- **Extract complementary insights** from different levels of molecular detail
- **Generate publication-quality comparisons** with identical analysis parameters

### Research Context

This toolkit has been developed and tested across diverse protein systems. The suite enables researchers to:
- Perform comprehensive analyses on MD trajectories from various sources
- Compare results across different simulation approaches
- Extract biological insights from different levels of molecular detail
- Generate publication-quality visualizations and statistics

---

## BioEMU Integration

This suite now provides **seamless integration with BioEMU** for analyzing AI-generated protein ensembles alongside classical simulations.

### What is BioEMU?

**BioEMU** is a state-of-the-art generative deep learning model that rapidly samples thousands of physically-plausible protein conformations from sequence input, bypassing the need for long, resource-intensive molecular dynamics simulations.

| Feature | Classical MD | BioEMU |
|---------|--------------|--------|
| **Time to Conformers** | Weeks to months | Minutes to hours |
| **Sample Diversity** | Limited by sampling time | Diverse equilibrium ensembles |
| **Computational Cost** | HPC-required | Single GPU workstation |
| **Best For** | Detailed atomic interactions | Large-scale ensemble generation |

### BioEMU Workflow with This Suite

```
1. Generate ensemble with BioEMU (hours)
   ↓
2. Analyze with this suite (minutes)
   ↓
3. Identify interesting conformations
   ↓
4. Validate with classical MD (optional)
   ↓
5. Publication-ready results
```

### Quick Start: Analyzing BioEMU Output

```python
CONFIG = {
    "protein_name": "My Protein",
    "systems": {
        "bioemu": {
            "topology": "./bioemu_structure.pdb",
            "trajectory": "./bioemu_ensemble.xtc",
            "label": "BioEMU 100 samples",
        },
    },
    "analyses": {
        "rmsd_rmsf": True,      # Ensemble diversity
        "sasa": True,           # Surface exposure
        "hydrogen_bonds": True, # Persistent interactions
        "pore_hydration": True, # (for channels)
    }
}
```

### Key Analyses for BioEMU Data

- **RMSD/RMSF**: Identify conformational diversity and flexible regions
- **SASA**: Explore variable surface exposure across ensemble
- **Hydrogen Bonds**: Detect stabilizing interactions
- **Pore Hydration**: Analyze water dynamics in functional cavities
- **Inter-Helical Dynamics**: Track relative domain motions

### Learn More

See **[BIOEMU_SETUP_GUIDE.md](docs/BIOEMU_SETUP_GUIDE.md)** for:
- BioEMU installation instructions
- Detailed conformer generation workflow
- Comparative analysis strategies (BioEMU vs Classical MD)
- Troubleshooting and advanced usage

---

## Key Features

### ✨ Comprehensive Analysis Suite

1. **Structural Dynamics**
   - RMSD (Root Mean Square Deviation) - overall stability
   - RMSF (Root Mean Square Fluctuation) - per-residue flexibility
   - Inter-helical distance & angle - relative domain motion

2. **Solvation Analysis**
   - SASA (Solvent Accessible Surface Area) - hydration patterns
   - Pore hydration - water occupancy in functional cavities
   - Water bridges - direct and water-mediated contacts

3. **Interaction Analysis**
   - Hydrogen bond detection & persistence
   - Minimum distances (protein-residue/functional group interactions)
   - Contact analysis - inter-residue proximity networks

4. **Advanced Features**
   - Multi-system comparative analysis
   - Publication-quality plots (300 DPI)
   - Statistical summaries & CSV export
   - Memory-efficient processing
   - No hardcoded paths (fully configurable)

### 🎯 Design Philosophy

- **Flexible**: Works with any protein (GPCR, Ion Channel, Aquaporin, etc.)
- **Accessible**: No coding required - single configuration dictionary
- **Robust**: Handles GROMACS, AMBER, MDTraj-compatible formats
- **Publication-Ready**: High-resolution plots, statistics, error estimation
- **Reproducible**: Fully documented, version-controlled analysis

---

## Installation

### Option 1: Conda (Recommended)

```bash
# Clone the repository
git clone https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite.git
cd BioEMU-Protein-Dynamics-Analysis-Suite

# Create and activate conda environment
conda create -n bioemu-analysis python=3.10
conda activate bioemu-analysis

# Install from requirements
pip install -r installation/requirements.txt
```

### Option 2: Pip with Virtual Environment

```bash
# Clone the repository
git clone https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite.git
cd BioEMU-Protein-Dynamics-Analysis-Suite

# Create virtual environment
python3 -m venv bioemu-env
source bioemu-env/bin/activate  # On Windows: bioemu-env\Scripts\activate

# Install dependencies
pip install -r installation/requirements.txt
```

### Option 3: Docker (Fully Isolated)

```bash
docker build -t bioemu-analysis .
docker run -it -v $(pwd):/workspace bioemu-analysis
```

### Verification

```bash
python -c "import mdtraj, MDAnalysis; print('✓ All dependencies installed')"
```

---

## Quick Start

### 1. Prepare Your Data

Organize simulation files:

```
your_project/
├── analysis_notebook.ipynb
└── data/
    ├── system_apo/
    │   ├── structure.gro         # or .pdb, .tpr
    │   └── trajectory.xtc         # or .dcd, .h5
    └── system_bound/
        ├── structure.gro
        └── trajectory.xtc
```

### 2. Open the Analysis Notebook

```bash
jupyter notebook Comprehensive_Analysis.ipynb
```

### 3. Configure (Cell 1)

Edit the configuration dictionary with your system information:

```python
CONFIG = {
    "protein_name": "My Protein",
    "output_dir": "./results",
    
    "systems": {
        "apo": {
            "label": "Apo State",
            "topology": "./data/system_apo/structure.gro",
            "trajectory": "./data/system_apo/trajectory.xtc",
            "color": "#FF6B6B",
        },
        "bound": {
            "label": "Ligand Bound",
            "topology": "./data/system_bound/structure.gro",
            "trajectory": "./data/system_bound/trajectory.xtc",
            "color": "#4169E1",
        },
    },
    
    # Optional: Define secondary structure (helices)
    "secondary_structure": {
        "helices": [(3, 26, 'H1'), (34, 52, 'H2')],
        "strands": [],
    },
    
    # Analysis parameters
    "analyses": {
        "rmsd_rmsf": {"enabled": True, "stride": 1},
        "sasa": {"enabled": True, "stride": 10},
        "hydrogen_bonds": {"enabled": True, "distance_cutoff": 3.5},
        "water_bridges": {"enabled": True},
        "inter_helical": {"enabled": True},
        "pore_hydration": {"enabled": True},
    }
}
```

### 4. Run the Analysis

Execute cells sequentially to generate:
- Trajectory stability plots
- Per-residue flexibility maps
- Solvation analysis
- Interaction networks
- Publication-ready figures

### 5. Review Results

```
results/
├── rmsd_rmsf/
├── sasa_analysis/
├── hydrogen_bonds/
├── water_bridges/
├── inter_helical_dynamics/
└── summary_report.html
```

---

## Available Analyses

### 1. **RMSD (Root Mean Square Deviation)**
Measures how much the structure deviates from the initial frame.
- **Use for**: Overall stability, equilibration time
- **Output**: Time series plot + statistics

### 2. **RMSF (Root Mean Square Fluctuation)**
Per-residue flexibility analysis.
- **Use for**: Identifying flexible loops, stable domains
- **Output**: Per-residue plot with secondary structure

### 3. **Inter-Helical Distance & Angle**
Track relative positioning and rotation of helical domains.
- **Use for**: Domain dynamics, conformational changes
- **Output**: Distance/angle time series + final distributions

### 4. **SASA (Solvent Accessible Surface Area)**
Hydration patterns across the protein surface.
- **Use for**: Identifying buried/exposed residues
- **Output**: Per-residue SASA time series

### 5. **Pore Hydration**
Water occupancy in functional cavities.
- **Use for**: Ion channel/transporter gating mechanisms
- **Output**: Hydration density maps + water occupancy statistics

### 6. **Water Bridges**
Direct and water-mediated interactions.
- **Use for**: Stability mechanisms, functional interactions
- **Output**: Bridge occupancy summary (direct + mediated)

### 7. **Minimum Distance**
Closest approach between residues/functional groups.
- **Use for**: Interaction network mapping
- **Output**: Distance matrix + contact heatmaps

### 8. **Hydrogen Bonds**
Persistent H-bonds between residues.
- **Use for**: Stabilizing interactions, salt bridges
- **Output**: Occupancy table + temporal persistence plots

---

## Documentation

| Document | Purpose |
|----------|---------|
| [installation/INSTALL.md](installation/INSTALL.md) | Detailed setup instructions (conda/pip/Docker) |
| [docs/ANALYSIS_GUIDE.md](docs/ANALYSIS_GUIDE.md) | Complete guide to all 7 analyses |
| [docs/reference/CONFIG_QUICK_REFERENCE.md](docs/reference/CONFIG_QUICK_REFERENCE.md) | Configuration templates for common proteins |
| [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Common issues & solutions |
| [API_REFERENCE.md](docs/API_REFERENCE.md) | Python function documentation |

---

## Repository Structure

```
BioEMU-Protein-Dynamics/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── setup.py                           # Package installation
│
├── Comprehensive_Analysis.ipynb       # Main analysis notebook
│
├── docs/
│   ├── INSTALLATION.md                # Setup guide
│   ├── ANALYSIS_GUIDE.md              # Detailed analysis explanations
│   ├── QUICK_REFERENCE.md             # Configuration templates
│   ├── TROUBLESHOOTING.md             # FAQ & fixes
│   └── API_REFERENCE.md               # Function documentation
│
├── examples/
│   ├── kdel_comparison/               # KDEL receptor example
│   │   ├── config.py
│   │   ├── data/
│   │   └── results/
│   ├── gpcr_variants/                 # GPCR variant screening
│   └── ion_channel/                   # Ion channel gating dynamics
│
├── utils/
│   ├── __init__.py
│   ├── trajectory_loader.py           # File I/O handling
│   ├── analysis_functions.py          # Core analysis algorithms
│   ├── visualization.py               # Plotting utilities
│   └── statistics.py                  # Statistical calculations
│
├── data/                              # Sample data (if included)
│   ├── README.md
│   └── sample_systems/
│
└── .gitignore                         # Git ignore rules
```

---

## Requirements

### Minimum System Requirements
- **Python**: 3.8 or higher
- **RAM**: 4 GB (8+ GB recommended for large trajectories)
- **Disk**: 2 GB for dependencies + space for trajectory files
- **OS**: Linux, macOS, or Windows

### Python Dependencies

See [requirements.txt](requirements.txt) for complete list. Key packages:

- **MDAnalysis** (≥2.0): Trajectory analysis
- **MDTraj** (≥1.9): Structure analysis, SASA calculation
- **NumPy** (≥1.20): Numerical computation
- **Pandas** (≥1.3): Data manipulation
- **Matplotlib** (≥3.4): Plotting
- **Seaborn** (≥0.11): Statistical visualization
- **SciPy** (≥1.7): Scientific computing

### Optional Dependencies

- **Jupyter** (for notebook execution)
- **Plotly** (for interactive plots)
- **Pytest** (for testing)

---

## Examples

### Running on BioEMU Output

```python
CONFIG = {
    "protein_name": "GPCR",
    "systems": {
        "bioemu_sim": {
            "topology": "./bioemu_output/structure.gro",
            "trajectory": "./bioemu_output/trajectory.xtc",
            "label": "BioEMU 5μs",
        },
        "gromacs_validation": {
            "topology": "./gromacs_output/structure.gro",
            "trajectory": "./gromacs_output/trajectory.xtc",
            "label": "GROMACS 100ns",
        },
    }
}
```

### Running on Classical MD (GROMACS)

```python
CONFIG = {
    "protein_name": "Ion Channel",
    "systems": {
        "open_state": {
            "topology": "./simulations/open/em.tpr",
            "trajectory": "./simulations/open/production.xtc",
        },
        "closed_state": {
            "topology": "./simulations/closed/em.tpr",
            "trajectory": "./simulations/closed/production.xtc",
        },
    }
}
```

### Analyzing Multiple Variants

```python
CONFIG = {
    "protein_name": "KDELR Variants",
    "systems": {
        f"variant_{i}": {
            "topology": f"./variants/var{i}/structure.gro",
            "trajectory": f"./variants/var{i}/trajectory.xtc",
        }
        for i in range(1, 5)
    }
}
```

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution
- Additional analysis methods
- Performance optimizations
- Documentation improvements
- Example configurations
- Bug reports and fixes

---

## Citation

If you use this analysis suite in your research, please cite:

```bibtex
@software{bioemu_analysis_2026,
  author = {Laddha, Aditi},
  title = {BioEMU Analysis Suite: Comprehensive Protein Dynamics Analysis},
  year = {2026},
  url = {https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite}
}
```

### Related Publications

If you use BioEMU simulations, please also cite the original BioEMU paper:

```bibtex
@article{lin2024scalable,
  title={Scalable emulation of protein equilibrium ensembles},
  author={Lin, Ze and Frey, Nathaniel C. and others},
  journal={Nature Methods},
  year={2024}
}
```

Additionally, consider citing relevant software used in conjunction:
- GROMACS (if using classical MD trajectories)
- MDAnalysis (for trajectory analysis)
- NumPy, SciPy, Matplotlib (for numerical computing and visualization)

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## FAQ

**Q: Can I use this with AMBER simulations?**  
A: Yes! The notebook accepts any format supported by MDAnalysis (AMBER, NAMD, etc.).

**Q: How long does analysis take?**  
A: Depends on trajectory size. Typical 100 ns trajectory: 5-30 minutes. Larger trajectories can be analyzed in chunks.

**Q: Do I need GROMACS installed?**  
A: No. This suite reads GROMACS output files but doesn't require GROMACS installation.

**Q: Can I modify the analysis code?**  
A: Absolutely! Code is fully documented and modular. See [API_REFERENCE.md](docs/API_REFERENCE.md).

**Q: How do I cite this in a publication?**  
A: See the [Citation](#citation) section above.

---

## Support

- 📖 Check [documentation](docs/)
- 🔍 Search [issues](https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite/issues)
- 💬 Open a [discussion](https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite/discussions)

---

## Acknowledgments

We thank the open-source scientific computing community, particularly the developers of MDAnalysis, GROMACS, NumPy, and SciPy for enabling this toolkit.

---

<div align="center">

**Made with ❤️ for the structural biology community**

⭐ If you find this useful, please star this repository!

</div>
