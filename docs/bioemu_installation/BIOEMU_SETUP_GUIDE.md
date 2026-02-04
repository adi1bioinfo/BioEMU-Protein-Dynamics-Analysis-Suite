# BioEMU Setup & Integration Guide

## Overview

**BioEMU** (Biological Electromagnetic Unit) is a state-of-the-art generative deep learning model that rapidly samples thousands of physically-plausible protein conformations from sequence input, bypassing the need for long, resource-intensive molecular dynamics simulations.

This guide walks you through:
1. Installing BioEMU
2. Generating protein conformations
3. Analyzing BioEMU output with the BioEMU Analysis Suite
4. Comparing BioEMU results with classical MD

---

## Why BioEMU?

| Feature | Classical MD | BioEMU |
|---------|--------------|--------|
| **Time to Conformers** | Weeks to months | Minutes to hours |
| **Sample Diversity** | Limited by sampling time | Diverse equilibrium ensembles |
| **Computational Cost** | HPC-required | Single GPU workstation |
| **Application Scope** | Detailed atomic dynamics | Large-scale ensemble generation |

> **BioEMU bridges the divide between accuracy and scalability — unlocking dynamic views on protein function at a fraction of traditional costs and time.**

---

## Installation

### Prerequisites

- Python 3.8 or higher
- CUDA 11.0+ (for GPU acceleration, optional but recommended)
- ~5 GB disk space for BioEMU model

### Step 1: Create Environment

```bash
conda create -n bioemu_analysis python=3.10
conda activate bioemu_analysis
```

### Step 2: Install BioEMU and Dependencies

```bash
# Install BioEMU
pip install bioemu

# Optional: For MD relaxation capabilities
pip install bioemu[md]
```

### Step 3: Install Analysis Suite Dependencies

```bash
# From your BioEMU-Protein-Dynamics-Analysis-Suite directory
pip install -r requirements.txt
```

### Complete Requirements

Your environment now includes:
- **BioEMU**: Conformer generation
- **MDAnalysis**: Trajectory analysis
- **MDTraj**: Structure analysis and SASA calculation
- **NumPy, Pandas, SciPy**: Scientific computing
- **Matplotlib, Seaborn**: Visualization
- **Jupyter**: Interactive notebooks

---

## Generating Conformations with BioEMU

### Basic Usage

#### 1. Prepare Your Protein Sequence

Create a FASTA file with your protein sequence:

```fasta
>my_protein
MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPILSRVGDGTQDNLSGAEKAVQVKVKALPDAQFEVV
HSLAKWKRQTLGQHDFSAGEGLYTHMKALRPDEDRLSPLHSVYVDQWDWERVMGDGERQFSTLKSTVEAIWAGIKATEAAVSEEFGLAPFLPDQIHFVHSQELLSRYPDLDAKGRERAIAKDLGAVFLVGIGGKLSDGHRHDVRAPDYDDWSTPSELGHAGLNGDILVWNPVLEDAFELSSMGIRVDADTLKHQLALTGDEDRLELEWHQALLRGEMPQTIGGGIGQSRLTMLLLQLPHIGQVQAGVWPAAVRESVPSLL
```

#### 2. Generate Conformers

```python
import bioemu

# Initialize BioEMU
model = bioemu.BioEMU()

# Load sequence
sequence = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPILSRVGDGTQDNLSGAEK..."

# Generate conformations
ensemble = model.sample(sequence, num_samples=100)

# Save as trajectory
ensemble.save_xtc('conformations.xtc')
ensemble[0].save_pdb('structure.pdb')
```

#### 3. Using the Command Line

```bash
# Generate 100 conformations
bioemu sample --sequence protein.fasta --num_samples 100 --output output.xtc
```

---

## Analyzing BioEMU Output with This Suite

### Workflow: BioEMU → Analysis Suite

#### 1. Organize Your Data

```
your_project/
├── data/
│   ├── bioemu/
│   │   ├── structure.pdb          # Initial frame
│   │   └── trajectory.xtc         # BioEMU conformations
│   └── (optional) classical_md/
│       ├── structure.gro
│       └── trajectory.xtc
└── analysis_notebook.ipynb
```

#### 2. Configure the Analysis Suite

Open `Comprehensive_Analysis.ipynb` and edit Cell 1:

```python
CONFIG = {
    "protein_name": "My Protein",
    "output_dir": "./results",
    
    "systems": {
        "bioemu": {
            "label": "BioEMU Ensemble (100 samples)",
            "topology": "./data/bioemu/structure.pdb",
            "trajectory": "./data/bioemu/trajectory.xtc",
            "color": "#FF6B6B",
        },
        # Optional: Classical MD for comparison
        "gromacs": {
            "label": "GROMACS 100ns MD",
            "topology": "./data/classical_md/structure.gro",
            "trajectory": "./data/classical_md/trajectory.xtc",
            "color": "#4169E1",
        },
    },
    
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

#### 3. Run the Analysis

Execute the notebook cells sequentially to generate:
- Conformational diversity metrics (RMSD/RMSF)
- Structural stability analysis
- Per-residue flexibility patterns
- Solvation and hydration profiles
- Interaction networks
- Publication-ready figures

---

## Key Analyses for BioEMU Data

### 1. **RMSD (Root Mean Square Deviation)**
Measures conformational diversity in the BioEMU ensemble.
- **Interpretation**: Higher RMSD → Greater conformational sampling
- **Output**: Distribution of conformational states

### 2. **RMSF (Root Mean Square Fluctuation)**
Per-residue flexibility in the generated ensemble.
- **Interpretation**: Flexible regions capture functional motions
- **Output**: Flexibility profile identifying gating residues

### 3. **SASA (Solvent Accessible Surface Area)**
Hydration patterns across the conformational ensemble.
- **Interpretation**: Variable SASA → Dynamic surface exposure
- **Output**: Surface accessibility profiles

### 4. **Hydrogen Bonds**
Persistent interactions stabilizing the ensemble.
- **Interpretation**: Conserved H-bonds across conformations
- **Output**: Interaction network persistence

### 5. **Pore Hydration** (for channels/transporters)
Water occupancy in functional cavities across conformations.
- **Interpretation**: Variable hydration → Dynamic pore behavior
- **Output**: Hydration probability maps

---

## BioEMU vs Classical MD: Comparative Analysis

### When to Use BioEMU

✅ **Rapid ensemble generation**
✅ **Exploring conformational space**
✅ **Identifying functional motions**
✅ **Drug discovery screening**
✅ **Hypothesis generation**

### When to Use Classical MD

✅ **Detailed atomic interactions**
✅ **Water-mediated effects**
✅ **Precise kinetic information**
✅ **Validation of BioEMU findings**

### Recommended Workflow

```
1. Generate BioEMU ensemble (hours)
   ↓
2. Analyze with this suite (minutes)
   ↓
3. Identify interesting conformations/mechanisms
   ↓
4. Run targeted classical MD (days)
   ↓
5. Validate and cross-analyze both
   ↓
6. Publication-quality results
```

---

## Example: GPCR Analysis with BioEMU

### Workflow

```python
# 1. Generate GPCR ensemble with BioEMU
import bioemu
model = bioemu.BioEMU()
gpcr_sequence = "MNGTEGP..."  # Your GPCR sequence
ensemble = model.sample(gpcr_sequence, num_samples=500)
ensemble.save_xtc('gpcr_ensemble.xtc')
ensemble[0].save_pdb('gpcr_structure.pdb')

# 2. Analyze with the suite
# Use Comprehensive_Analysis.ipynb with:
CONFIG = {
    "protein_name": "GPCR",
    "systems": {
        "bioemu_ensemble": {
            "topology": "gpcr_structure.pdb",
            "trajectory": "gpcr_ensemble.xtc",
            "label": "BioEMU 500 conformations",
        }
    },
    "secondary_structure": {
        "helices": [(1, 35, 'TM1'), (45, 80, 'TM2'), ...],  # 7 TM helices
    }
}

# 3. Key Findings
# - RMSF identifies gating residues
# - Pore hydration reveals activation mechanisms
# - Inter-helical dynamics show conformational transitions
# - Flexible regions = allosteric sites
```

---

## Troubleshooting

### Issue: BioEMU model not found

```bash
# Download the model
bioemu download --model bioemu-1.0
```

### Issue: Out of memory with large ensembles

```python
# Analyze in chunks
stride = 10  # Analyze every 10th frame
ensemble_subset = ensemble[::stride]
```

### Issue: GPU not detected

```bash
# Install CUDA support
pip install bioemu[cuda]

# Verify GPU
python -c "import torch; print(torch.cuda.is_available())"
```

---

## Citation

If you use BioEMU with this analysis suite, please cite:

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

## Additional Resources

- [BioEMU GitHub Repository](https://github.com/microsoft/BioEmu) (when public)
- [BioEMU Paper - Nature Methods 2024](https://doi.org/10.1038/s41592-024-xxxxx)
- [Analysis Suite Documentation](./ANALYSIS_GUIDE.md)
- [Installation Guide](./INSTALLATION.md)

---

## Support & Contributions

For issues or questions:
- Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
- Open an [issue on GitHub](https://github.com/adi1bioinfo/BioEMU-Protein-Dynamics-Analysis-Suite/issues)
- See [Contributing Guidelines](../CONTRIBUTING.md)
