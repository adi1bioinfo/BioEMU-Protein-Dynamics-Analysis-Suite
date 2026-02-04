# MD_Analysis_Protocol: Complete Package Summary

## What You Have

### 🔬 Main Analysis Notebook
- **File**: `MD_Analysis_Protocol.ipynb`
- **Purpose**: Generalized Jupyter notebook for analyzing any protein's MD simulations
- **Format**: GROMACS trajectory files (.xtc, .gro, .tpr)
- **Analyses Included**:
  - ✅ RMSD (Root Mean Square Deviation) - Overall stability
  - ✅ RMSF (Root Mean Square Fluctuation) - Per-residue flexibility
  - ✅ SASA (Solvent-Accessible Surface Area) - Hydration/exposure
  - ✅ Hydrogen Bonding Analysis - Interaction networks
  - ✅ Contact Analysis - Residue pair interactions
  - ✅ Summary Statistics - Mean, std, min, max values
  - ✅ Publication-ready plots (PNG, 300 DPI)
  - ✅ Numerical data export (CSV)

### 📖 Documentation Files

1. **MD_ANALYSIS_README.md** (main documentation)
   - Installation instructions
   - Quick start guide
   - Complete configuration reference
   - Example configurations (GPCR, Ion Channel, Aquaporin)
   - Troubleshooting guide
   - Performance benchmarks

2. **CONFIG_QUICK_REFERENCE.md** (configuration examples)
   - 10+ ready-to-use configuration templates
   - Minimal, comprehensive, and specialized examples
   - Protein-specific presets (GPCR, ion channels, etc.)
   - MDAnalysis selection language cheat sheet
   - Color palette recommendations

3. **BIOEMU_INTEGRATION_GUIDE.md** (for bioemu projects)
   - How to integrate with bioemu simulation pipeline
   - Directory structure recommendations
   - Pre-configured analysis setups
   - Automated analysis scripts
   - Publishing workflow

## Key Features

### ✨ No Hardcoding Required
- ✅ Single configuration dictionary (CONFIG) controls everything
- ✅ No need to edit code cells
- ✅ Easy to switch between proteins
- ✅ Parameterized atom selections (MDAnalysis language)

### 🎨 Flexible Visualization
- ✅ Customizable colors and labels per system
- ✅ Automatic comparative plotting (all systems vs each other)
- ✅ Optional secondary structure annotations (helices, strands)
- ✅ Rolling average smoothing with configurable window
- ✅ Statistical summary in plot legends

### ⚡ Efficient Analysis
- ✅ Chunk-based processing for large trajectories (memory-efficient)
- ✅ Frame striding to skip frames (reduce analysis time)
- ✅ Automatic garbage collection
- ✅ Suitable for 1000 to 1,000,000+ frame trajectories

### 📊 Comprehensive Output
```
analysis_results/
├── rmsd_rmsf/
│   ├── rmsd_comparison.png
│   ├── rmsf_comparison.png
│   ├── rmsd_all_systems.csv
│   └── rmsf_all_systems.csv
├── sasa/
│   └── {system}_sasa.csv
├── hbonds/
│   └── {system}_hbonds.csv
├── contacts/
│   └── {system}_contacts.csv
├── summary_statistics.csv
└── ANALYSIS_REPORT.txt
```

## How to Use

### For Any Protein (GPCR, Aquaporin, Ion Channel, etc.)

#### Step 1: Prepare Files
```
data/
├── system_1/
│   ├── em.gro (topology)
│   └── production.xtc (trajectory)
└── system_2/
    ├── em.gro
    └── production.xtc
```

#### Step 2: Configure
Edit `CONFIG` dictionary in Cell 1:
```python
CONFIG = {
    "protein_name": "Your Protein Name",
    "output_dir": "./results",
    "systems": {
        "system_1": {
            "label": "Display Name",
            "topology": "./data/system_1/em.gro",
            "trajectory": "./data/system_1/production.xtc",
            "color": "#FF6B6B",
        },
        # ... more systems
    },
}
```

#### Step 3: Run
Execute all cells in order (top to bottom)

#### Step 4: Review
Check `output_dir` for results

### For bioemu Projects

1. Store simulations in `simulations/` folder
2. Create config from template in `analysis_configs/`
3. Run `MD_Analysis_Protocol.ipynb`
4. Results saved to `results/` subfolder
5. See **BIOEMU_INTEGRATION_GUIDE.md** for details

## Configuration Examples Provided

| Use Case | File | Proteins |
|----------|------|----------|
| Minimal (3 systems) | CONFIG_QUICK_REFERENCE.md | Any |
| GPCR (7 TM helices) | CONFIG_QUICK_REFERENCE.md | β2AR, GPCR-X, etc. |
| Ion Channels | CONFIG_QUICK_REFERENCE.md | KcsA, TRPV1, etc. |
| Aquaporins | CONFIG_QUICK_REFERENCE.md | AQP1, AQP4, etc. |
| Enzyme-substrate | CONFIG_QUICK_REFERENCE.md | Any enzyme |
| WT vs Mutant | CONFIG_QUICK_REFERENCE.md | Any protein |
| Speed optimization | CONFIG_QUICK_REFERENCE.md | Large trajectories |

## Removed Features from Original

❌ **KDEL-specific elements**:
- Hardcoded system names (APO_12HSD, etc.)
- Absolute file paths to KDEL simulations
- KDEL-specific residue lists
- Protein-specific directory structures

✅ **Replaced with**:
- Generic "system_1", "system_2" identifiers
- Path variables in configuration
- Customizable residue selections via MDAnalysis language
- Flexible directory structure

## Analysis Capabilities

### RMSD Analysis
- Measures structural deviation from reference frame
- Shows overall stability of protein
- Optional rolling average smoothing
- Statistics for last N nanoseconds

### RMSF Analysis
- Per-residue flexibility/motion
- Identifies flexible loops and rigid cores
- Optional secondary structure highlighting
- Useful for understanding dynamics

### SASA Analysis
- Hydration of residues over time
- Memory-efficient chunk processing
- Per-residue tracking
- Grouped residue analysis (charged, hydrophobic, etc.)

### Hydrogen Bonding
- Donor-acceptor identification
- Distance and angle validation
- Frame-by-frame tracking
- Interaction network visualization

### Contact Analysis
- Residue-residue distance tracking
- Frequency statistics (how often contacts occur)
- Distance statistics (min, max, average)
- Useful for identifying stable/transient interactions

## System Requirements

### Software
- Python 3.8+
- Jupyter Notebook or JupyterLab
- MDAnalysis 2.0+
- MDTraj 1.9+
- pandas, numpy, matplotlib, seaborn

### Hardware
- RAM: 2 GB (minimum) to 16+ GB (for large trajectories)
- Disk: 1-10 GB for output (depends on trajectory size)
- CPU: Any modern processor

### Install Dependencies
```bash
conda install -c conda-forge mdanalysis mdtraj pandas numpy matplotlib seaborn scikit-learn
```

## Output Interpretation

### RMSD Plot
- Y-axis: RMSD (Å) - lower = more stable
- X-axis: Simulation time (ns)
- Plateau = system reached equilibrium
- Jumping = system instability

### RMSF Plot
- Y-axis: RMSF (Å) - higher = more flexible
- X-axis: Residue number
- Peaks = flexible loops
- Valleys = rigid structure (secondary structure)

### SASA Plot
- Y-axis: SASA (Ų)
- X-axis: Time (ns)
- Increasing = residue becoming more exposed
- Decreasing = residue becoming buried

## Citation

### If Publishing Results

Cite the underlying tools:

```bibtex
@article{Michaud-Agrawal2011,
  title={MDAnalysis: A toolkit for the analysis of molecular dynamics simulations},
  author={Michaud-Agrawal, N. and Denning, E. J. and Woolf, T. B. and Beckstein, O.},
  journal={Journal of Computational Chemistry},
  volume={32},
  pages={2319--2327},
  year={2011}
}

@article{McGibbon2015,
  title={MDTraj: A modern open library for the analysis of molecular dynamics trajectories},
  author={McGibbon, R. T. and Beauchamp, K. A. and Harrigan, M. P. and others},
  journal={Biophysical Journal},
  volume={109},
  pages={1528--1532},
  year={2015}
}
```

## File Manifest

### In This Package
```
/home/aditi/Desktop/python/work_related/
├── MD_Analysis_Protocol.ipynb              ← Main notebook
├── MD_ANALYSIS_README.md                   ← Full documentation
├── CONFIG_QUICK_REFERENCE.md               ← Configuration templates
└── BIOEMU_INTEGRATION_GUIDE.md             ← bioemu integration
```

### For bioemu Integration
```
bioemu_project/
├── analysis/
│   ├── MD_Analysis_Protocol.ipynb
│   ├── analysis_configs/
│   │   ├── gpcr_config.py
│   │   ├── aquaporin_config.py
│   │   └── template_config.py
│   └── results/
└── simulations/
    └── protein_simulation_outputs/
```

## Common Questions

**Q: How many systems can I compare?**
A: Unlimited - just add more entries to the `systems` dictionary

**Q: Can I analyze non-GROMACS trajectories?**
A: Yes - MDAnalysis supports .dcd, .trr, .h5 formats

**Q: What if my protein doesn't have obvious secondary structure?**
A: Leave `secondary_structure` empty - plots work fine without it

**Q: How do I speed up analysis for 100k+ frame trajectories?**
A: Increase `frame_stride` in SASA config (e.g., stride=50 = 50x faster)

**Q: Can I run without Jupyter?**
A: Yes - use papermill or other notebook runners for batch execution

**Q: What if residue numbering is different in my topology?**
A: MDAnalysis automatically detects residue numbering from the file

## Support & Feedback

- Check **MD_ANALYSIS_README.md** for detailed troubleshooting
- Review **CONFIG_QUICK_REFERENCE.md** for example configurations
- See **BIOEMU_INTEGRATION_GUIDE.md** if using with bioemu

## Version History

- **v1.0** (Feb 2026): Initial release
  - RMSD/RMSF analysis
  - SASA calculation
  - Hydrogen bonding
  - Contact analysis
  - Summary statistics
  - Publication-ready visualization

---

## Ready to Use!

### Next Steps:
1. ✅ Copy `MD_Analysis_Protocol.ipynb` to your project
2. ✅ Read appropriate guide:
   - General use → **MD_ANALYSIS_README.md**
   - Examples → **CONFIG_QUICK_REFERENCE.md**  
   - bioemu use → **BIOEMU_INTEGRATION_GUIDE.md**
3. ✅ Prepare your simulation files
4. ✅ Configure CONFIG dictionary
5. ✅ Run notebook
6. ✅ Review results

**Happy analyzing!** 🧬
