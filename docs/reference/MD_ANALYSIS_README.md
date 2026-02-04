# MD_Analysis_Protocol: Generalized Molecular Dynamics Analysis

A flexible, publication-ready Jupyter notebook for analyzing molecular dynamics simulations of **any protein** using GROMACS trajectories.

## Features

✅ **Protein-Agnostic**: Works with GPCR, Aquaporin, KDEL, ion channels, or any protein  
✅ **Multiple Analyses**: RMSD, RMSF, SASA, hydrogen bonding, contact analysis  
✅ **Comparative**: Analyze multiple simulation conditions (apo/bound, wild-type/mutant, etc.)  
✅ **Publication-Ready**: High-quality plots and statistics (DPI-300)  
✅ **Configurable**: Single configuration cell - no code editing needed  
✅ **Memory-Efficient**: Chunk-based processing for large trajectories  

## Installation

### Prerequisites

```bash
conda create -n md_analysis python=3.9
conda activate md_analysis
conda install -c conda-forge mdanalysis mdtraj pandas numpy matplotlib seaborn scikit-learn
```

Or use an existing conda environment:

```bash
conda install -c conda-forge mdanalysis mdtraj
```

### Get the Notebook

Clone or download `MD_Analysis_Protocol.ipynb` to your project directory.

## Quick Start

### 1. Prepare Your Data

Organize simulation files like this:

```
project_root/
├── MD_Analysis_Protocol.ipynb
└── data/
    ├── system_apo/
    │   ├── em.gro (or .pdb, .tpr)
    │   └── production.xtc
    └── system_bound/
        ├── em.gro
        └── production.xtc
```

### 2. Configure the Analysis

Open `MD_Analysis_Protocol.ipynb` and edit the **CONFIG** dictionary in Cell 2:

```python
CONFIG = {
    "protein_name": "My Protein",  # e.g., "β2-Adrenergic Receptor"
    "output_dir": "./analysis_results",
    
    "systems": {
        "apo": {
            "label": "Apo State",
            "topology": "./data/system_apo/em.gro",
            "trajectory": "./data/system_apo/production.xtc",
            "color": "#FF6B6B",
        },
        "bound": {
            "label": "Ligand Bound",
            "topology": "./data/system_bound/em.gro",
            "trajectory": "./data/system_bound/production.xtc",
            "color": "#4169E1",
        },
    },
    
    # Optional: Define secondary structure
    "secondary_structure": {
        "helices": [(3, 26, 'H1'), (34, 52, 'H2')],  # (start_res, end_res, name)
        "strands": [],
    },
}
```

### 3. Run the Analysis

Execute cells in order from top to bottom:

```
Cell 1: Configuration (with your edits)
Cell 2: Utility Functions
Cell 3: RMSD/RMSF Calculation
Cell 4: RMSD/RMSF Plots
Cell 5: SASA Analysis
Cell 6: Hydrogen Bonds
Cell 7: Contact Analysis
Cell 8: Summary Statistics
Cell 9: Final Report
```

### 4. Review Results

All outputs saved to `./analysis_results/`:

```
analysis_results/
├── rmsd_rmsf/
│   ├── rmsd_comparison.png
│   ├── rmsf_comparison.png
│   ├── rmsd_all_systems.csv
│   └── rmsf_all_systems.csv
├── sasa/
│   ├── system_apo_sasa.csv
│   └── system_bound_sasa.csv
├── hbonds/
│   ├── system_apo_hbonds.csv
│   └── system_bound_hbonds.csv
├── contacts/
│   ├── system_apo_contacts.csv
│   └── system_bound_contacts.csv
└── summary_statistics.csv
```

## Configuration Guide

### Protein Name
```python
"protein_name": "GPCR"  # Used in plot titles and reports
```

### Systems Definition

Each system requires:
- **label**: Display name for plots
- **topology**: Path to structure file (.gro, .pdb, .tpr)
- **trajectory**: Path to trajectory file (.xtc, .dcd, .trr, etc.)
- **color**: Hex color for plotting (e.g., "#FF6B6B")

Example with 4 systems:

```python
"systems": {
    "wt_apo": {
        "label": "WT Apo",
        "topology": "./data/wt_apo/em.gro",
        "trajectory": "./data/wt_apo/prod.xtc",
        "color": "#FF6B6B",
    },
    "wt_bound": {
        "label": "WT Bound",
        "topology": "./data/wt_bound/em.gro",
        "trajectory": "./data/wt_bound/prod.xtc",
        "color": "#FF8C00",
    },
    "mutant_apo": {
        "label": "Mutant Apo",
        "topology": "./data/mut_apo/em.gro",
        "trajectory": "./data/mut_apo/prod.xtc",
        "color": "#4169E1",
    },
    "mutant_bound": {
        "label": "Mutant Bound",
        "topology": "./data/mut_bound/em.gro",
        "trajectory": "./data/mut_bound/prod.xtc",
        "color": "#1E90FF",
    },
}
```

### Enable/Disable Analyses

```python
"rmsd_rmsf": {
    "enabled": True,  # Set to False to skip this analysis
    "atom_selection": "protein and backbone",  # MDAnalysis selection language
    "reference_frame": 0,  # Frame 0 = initial structure
},
```

#### Common MDAnalysis Selections:

```python
"protein and backbone"      # C-alpha only
"protein"                   # All protein atoms
"protein and sidechains"    # Only sidechains
"resname ARG LYS HIS"       # Specific residue types
"resid 1:50"                # Residue ID range
"name CA"                   # Specific atom names
```

### SASA Configuration

```python
"sasa": {
    "enabled": True,
    "frame_stride": 10,  # Process every 10th frame (10 = 90% less time)
    "residue_groups": {
        "charged": [("ARG", "LYS", "HIS", "ASP", "GLU")],
        "hydrophobic": [("VAL", "LEU", "ILE", "MET", "PHE", "TRP", "PRO")],
    },
},
```

### Hydrogen Bond Analysis

```python
"hbond": {
    "enabled": True,
    "distance_cutoff": 3.5,  # Donor-acceptor distance (Angstroms)
    "angle_cutoff": 120.0,   # Donor-H-Acceptor angle (degrees)
},
```

### Secondary Structure (Helices/Strands)

For helical proteins (GPCRs have 7 transmembrane helices):

```python
"secondary_structure": {
    "helices": [
        (25, 60, 'TM1'),    # (start_residue, end_residue, label)
        (70, 95, 'TM2'),
        (110, 140, 'TM3'),
        # ... more helices
    ],
    "strands": [],
},
```

These regions will be highlighted as backgrounds in RMSF plots.

### Plotting Options

```python
"plotting": {
    "rolling_average_window_ns": 10.0,  # Smoothing window for RMSD
    "last_frames_statistics": 500,      # ns of trajectory for statistics
    "dpi": 300,                          # Plot resolution
    "figure_style": "seaborn-v0_8-whitegrid",  # matplotlib style
},
```

## Examples

### Example 1: GPCR Analysis

```python
CONFIG = {
    "protein_name": "β2-Adrenergic Receptor",
    "project_name": "gpcr_agonist_study",
    "output_dir": "./results/gpcr_2024",
    
    "systems": {
        "apo": {
            "label": "Apo (inactive)",
            "topology": "./trajectories/apo/em.gro",
            "trajectory": "./trajectories/apo/prod_center.xtc",
            "color": "#E74C3C",  # Red
        },
        "isoproterenol": {
            "label": "Isoproterenol Bound",
            "topology": "./trajectories/iso/em.gro",
            "trajectory": "./trajectories/iso/prod_center.xtc",
            "color": "#3498DB",  # Blue
        },
    },
    
    "rmsd_rmsf": {
        "enabled": True,
        "atom_selection": "protein and backbone",
        "reference_frame": 0,
    },
    
    "secondary_structure": {
        "helices": [
            (25, 55, 'TM1'), (64, 97, 'TM2'), (105, 140, 'TM3'),
            (157, 187, 'TM4'), (199, 229, 'TM5'), (243, 273, 'TM6'),
            (285, 310, 'TM7'),
        ],
    },
}
```

### Example 2: Ion Channel Analysis

```python
CONFIG = {
    "protein_name": "Potassium Channel",
    "systems": {
        "open": {
            "label": "Open State",
            "topology": "./data/kchannel_open/em.pdb",
            "trajectory": "./data/kchannel_open/md.xtc",
            "color": "#27AE60",  # Green
        },
        "closed": {
            "label": "Closed State",
            "topology": "./data/kchannel_closed/em.pdb",
            "trajectory": "./data/kchannel_closed/md.xtc",
            "color": "#C0392B",  # Dark red
        },
    },
    
    "distance_analysis": {
        "enabled": True,
        "residue_pairs": [(50, 150), (75, 175), (100, 200)],  # Gate residues
    },
}
```

### Example 3: Aquaporin Analysis

```python
CONFIG = {
    "protein_name": "Aquaporin-1",
    "systems": {
        "water_channel": {
            "label": "Water-Occupied",
            "topology": "./data/aqp1_water/em.gro",
            "trajectory": "./data/aqp1_water/prod.xtc",
            "color": "#3498DB",
        },
        "empty": {
            "label": "Empty Channel",
            "topology": "./data/aqp1_empty/em.gro",
            "trajectory": "./data/aqp1_empty/prod.xtc",
            "color": "#95A5A6",
        },
    },
    
    "sasa": {
        "enabled": True,
        "frame_stride": 5,  # Higher frequency for channel analysis
    },
}
```

## Output Files

### RMSD/RMSF
- `rmsd_comparison.png`: Time-series RMSD plot for all systems
- `rmsf_comparison.png`: Per-residue flexibility plot
- `rmsd_all_systems.csv`: Numerical RMSD data
- `rmsf_all_systems.csv`: Numerical RMSF data

### SASA
- `{system_name}_sasa.csv`: Solvent-accessible surface area per residue over time

### Hydrogen Bonds
- `{system_name}_hbonds.csv`: List of hydrogen bonds with distances and angles

### Contacts
- `{system_name}_contacts.csv`: Residue-residue contacts with frequency and distances

### Summary
- `summary_statistics.csv`: Statistical summary (mean, std, min, max) for all systems
- `ANALYSIS_REPORT.txt`: Text report of all analyses performed

## File Formats

### Supported Topology Files
- `.gro` - GROMACS structure (recommended)
- `.pdb` - Protein Data Bank format
- `.tpr` - GROMACS binary topology

### Supported Trajectory Formats
- `.xtc` - GROMACS compressed trajectory (recommended)
- `.dcd` - NAMD/CHARMM format
- `.trr` - GROMACS ASCII trajectory
- `.h5` - HDF5 trajectory
- `.nc` - NetCDF format

## Tips for Best Results

1. **Center Trajectories**: Use `gmx_mpi trjconv -center -pbc nojump` before analysis
2. **Frame Stride**: Use stride > 1 to speed up analysis of long trajectories
3. **Reference Frame**: Use first equilibrated frame (not initial frame) for more meaningful RMSD
4. **Color Selection**: Use distinct colors for different conditions
5. **Atom Selection**: Be specific (e.g., "backbone" vs "all atoms") to highlight relevant features

## Troubleshooting

### Error: "Topology file not found"
- Check file path is correct and uses forward slashes `/`
- Use absolute paths if relative paths don't work

### Error: "No atoms selected"
- Verify MDAnalysis selection string is valid
- Test with simpler selections like `"protein"`

### Memory Issues with Large Trajectories
- Increase `frame_stride` (process fewer frames)
- Reduce `chunk_size` in SASA analysis (in code)
- Run analysis on HPC cluster if available

### Plots Aren't Showing
- Ensure you're running Jupyter interactively (not batch mode)
- Check that matplotlib backend is set correctly: `%matplotlib inline`

## Performance Notes

| Trajectory Size | RMSD | SASA | H-bonds | Total |
|---|---|---|---|---|
| 1000 frames | <1 min | 2-5 min | 1-2 min | ~5-8 min |
| 10000 frames | 2-3 min | 20-50 min* | 5-10 min | ~30-60 min* |
| 100000 frames | 20-30 min | 2-5 hrs* | 30-60 min | 3-6 hrs* |

*Use `frame_stride` > 1 to dramatically reduce time

## Citation

If you use this analysis in published research, please cite:

```bibtex
@article{Michaud-Agrawal2011,
  title={MDAnalysis: A toolkit for the analysis of molecular dynamics simulations},
  author={Michaud-Agrawal, N. and Denning, E. J. and Woolf, T. B. and Beckstein, O.},
  journal={J. Comput. Chem.},
  volume={32},
  pages={2319--2327},
  year={2011},
  doi={10.1002/jcc.21787}
}

@article{McGibbon2015,
  title={MDTraj: A modern open library for the analysis of molecular dynamics trajectories},
  author={McGibbon, R. T. and Beauchamp, K. A. and Harrigan, M. P. and others},
  journal={Biophys. J.},
  volume={109},
  pages={1528--1532},
  year={2015},
  doi={10.1016/j.bpj.2015.08.015}
}
```

## License

This notebook is provided as-is for research and educational purposes.

## Questions or Issues?

- Check the configuration section carefully
- Review example configurations above
- Ensure all dependencies are installed: `conda list | grep -E "mdanalysis|mdtraj|pandas|numpy"`

---

**Last Updated**: February 2026  
**Compatible with**: Python 3.8+, MDAnalysis 2.0+, MDTraj 1.9+
