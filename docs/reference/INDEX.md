# 📚 Documentation Index

## Quick Links

### 🚀 I want to start analyzing immediately
→ Read: **PACKAGE_SUMMARY.md** (5 min read)  
→ Then: **CONFIG_QUICK_REFERENCE.md** (find your protein type)

### 📖 I need detailed documentation
→ Read: **MD_ANALYSIS_README.md** (comprehensive guide)

### 🔧 I'm integrating with bioemu
→ Read: **BIOEMU_INTEGRATION_GUIDE.md** (step-by-step setup)

### 💻 I want to use the notebook
→ Open: **MD_Analysis_Protocol.ipynb** (Jupyter notebook)

---

## Files in This Package

| File | Purpose | Read Time | Best For |
|------|---------|-----------|----------|
| `MD_Analysis_Protocol.ipynb` | **Main notebook** - actual analysis code | - | Running analysis |
| `PACKAGE_SUMMARY.md` | Overview of package, features, outputs | 5 min | Getting started |
| `MD_ANALYSIS_README.md` | Complete documentation & guide | 20 min | Detailed setup |
| `CONFIG_QUICK_REFERENCE.md` | Ready-to-use configurations | 10 min | Finding your example |
| `BIOEMU_INTEGRATION_GUIDE.md` | bioemu project integration | 15 min | Using with bioemu |
| `INDEX.md` | This file - navigation guide | 3 min | Orientation |

---

## What This Package Does

**Analyzes molecular dynamics simulations of ANY protein from GROMACS**

### Supported Proteins
✅ GPCR (G-protein coupled receptors)  
✅ Aquaporin (water channels)  
✅ Ion channels (KcsA, TRPV1, etc.)  
✅ Enzymes (any protein with substrate/ligand)  
✅ Membrane proteins  
✅ Soluble proteins  
✅ Any protein with a PDB/topology file

### Analyses Performed
1. **RMSD** - Overall structural stability
2. **RMSF** - Per-residue flexibility
3. **SASA** - Solvent exposure over time
4. **Hydrogen Bonds** - Interaction networks
5. **Contacts** - Residue pair interactions
6. **Summary Statistics** - Mean, std, min, max values

### Output Types
- 📊 High-quality PNG plots (300 DPI, publication-ready)
- 📋 CSV data files (for further analysis)
- 📄 Text reports (analysis summary)

---

## Getting Started in 3 Steps

### Step 1: Prepare Your Data
```
your_project/
├── MD_Analysis_Protocol.ipynb
└── data/
    ├── system_1/
    │   ├── em.gro (topology)
    │   └── production.xtc (trajectory)
    └── system_2/
        ├── em.gro
        └── production.xtc
```

### Step 2: Configure (Edit CONFIG dictionary in Cell 1)
```python
CONFIG = {
    "protein_name": "Your Protein",
    "systems": {
        "system_1": {
            "label": "Condition A",
            "topology": "./data/system_1/em.gro",
            "trajectory": "./data/system_1/production.xtc",
            "color": "#FF6B6B",
        },
        "system_2": {
            "label": "Condition B",
            "topology": "./data/system_2/em.gro",
            "trajectory": "./data/system_2/production.xtc",
            "color": "#4169E1",
        },
    },
}
```

### Step 3: Run
Execute all notebook cells in order → Results saved to `./analysis_results/`

---

## Reading Guide by Use Case

### 👨‍💻 I'm a bioinformatician - I want to analyze simulations quickly

1. Read **PACKAGE_SUMMARY.md** (overview)
2. Find your protein in **CONFIG_QUICK_REFERENCE.md** (examples)
3. Copy config to notebook
4. Run notebook cells
5. Review plots in output folder

**Time investment**: ~30 minutes (including analysis runtime)

### 🧬 I'm a computational biologist - I want detailed control

1. Read **MD_ANALYSIS_README.md** (full reference)
2. Study configuration section carefully
3. Learn MDAnalysis selection language (cheat sheet in CONFIG_QUICK_REFERENCE.md)
4. Customize config for your protein
5. Run notebook with monitoring

**Time investment**: ~2 hours (for complete understanding)

### 🚀 I'm using bioemu - I want to integrate this into my workflow

1. Read **BIOEMU_INTEGRATION_GUIDE.md** (integration steps)
2. Create project structure (as specified in guide)
3. Set up analysis_configs/ folder
4. Run notebook on bioemu outputs
5. Automate with provided scripts

**Time investment**: ~1-2 hours (one-time setup)

### 📊 I want to publish results - I need publication-quality figures

1. Run full notebook analysis (all analyses enabled)
2. Results automatically saved as PNG at 300 DPI
3. Use summary_statistics.csv for tables
4. Combine multiple plots using PIL (example in BIOEMU_INTEGRATION_GUIDE.md)
5. Citation information in MD_ANALYSIS_README.md

**Example**: See "Publishing Results" section in BIOEMU_INTEGRATION_GUIDE.md

---

## Configuration Templates Available

### ✅ In CONFIG_QUICK_REFERENCE.md

| Template | Proteins | Status |
|----------|----------|--------|
| Minimal (3 systems) | Any | Ready |
| GPCR (TM1-7) | β2AR, ADRB1, etc. | Ready |
| Ion Channel | KcsA, TRPV1, NavAb | Ready |
| Aquaporin | AQP1, AQP4, etc. | Ready |
| Enzyme + ligand | Any enzyme | Ready |
| WT vs Mutant | Any protein | Ready |
| Multiple replicates | Any | Ready |
| Speed optimization | Large trajectories | Ready |
| All features enabled | Testing | Ready |

---

## Troubleshooting Decision Tree

```
Problem with analysis?
│
├─ "Topology file not found"
│  └─ Check file paths are correct
│     See: MD_ANALYSIS_README.md → Troubleshooting
│
├─ "No atoms selected"
│  └─ Verify MDAnalysis selection string
│     See: CONFIG_QUICK_REFERENCE.md → Selection Cheat Sheet
│
├─ "Memory error with large trajectory"
│  └─ Increase frame_stride or reduce chunk_size
│     See: MD_ANALYSIS_README.md → Performance Notes
│
├─ "Don't know how to configure"
│  └─ Find your protein type in examples
│     See: CONFIG_QUICK_REFERENCE.md → Templates
│
├─ "Using with bioemu"
│  └─ Follow integration guide
│     See: BIOEMU_INTEGRATION_GUIDE.md
│
└─ "Something else"
   └─ Check MD_ANALYSIS_README.md → Troubleshooting
```

---

## Key Concepts

### What is RMSD?
**Root Mean Square Deviation** - measures how much the protein structure changes over time. Lower values = more stable.

### What is RMSF?
**Root Mean Square Fluctuation** - measures flexibility of each residue. Higher values = more flexible regions.

### What is SASA?
**Solvent-Accessible Surface Area** - amount of protein surface exposed to water. Useful for understanding hydration and interactions.

### What are H-bonds?
Weak interactions between residues. Important for protein stability and function.

### What are Contacts?
Pairs of residues that come within a cutoff distance. Frequent contacts = important interactions.

---

## Installation Checklist

- [ ] Python 3.8 or higher installed
- [ ] Conda or pip available
- [ ] Dependencies installed:
  ```bash
  conda install -c conda-forge mdanalysis mdtraj pandas numpy matplotlib seaborn
  ```
- [ ] Jupyter Notebook or JupyterLab installed
- [ ] Simulation files (.xtc, .gro) available
- [ ] `MD_Analysis_Protocol.ipynb` in your project folder

If you get stuck on any step, see MD_ANALYSIS_README.md → Installation section.

---

## How to Use This Index

1. **First time?** → Read PACKAGE_SUMMARY.md, then find your protein in CONFIG_QUICK_REFERENCE.md
2. **Need details?** → Read MD_ANALYSIS_README.md
3. **Using bioemu?** → Read BIOEMU_INTEGRATION_GUIDE.md
4. **Lost?** → Check this file (INDEX.md) → Use decision tree above
5. **Ready to start?** → Open MD_Analysis_Protocol.ipynb

---

## File Location Reference

```
/home/aditi/Desktop/python/work_related/
├── MD_Analysis_Protocol.ipynb          ← The main notebook
├── MD_ANALYSIS_README.md               ← Full documentation  
├── CONFIG_QUICK_REFERENCE.md           ← Configuration examples
├── BIOEMU_INTEGRATION_GUIDE.md         ← bioemu integration
├── PACKAGE_SUMMARY.md                  ← Feature overview
└── INDEX.md                             ← This file
```

Copy all files to your bioemu/analysis project folder.

---

## Next Steps

✅ **What to do now:**

1. Choose your path (bioinformatician/biologist/bioemu user)
2. Read the recommended guide for your path
3. Find/create your configuration
4. Copy notebook to your project
5. Run analysis

✅ **After running analysis:**

1. Review plots in output folder
2. Check summary_statistics.csv
3. Export data for publication
4. Cite MDAnalysis and MDTraj

---

## Quick Reference Links

| Need | File | Section |
|------|------|---------|
| Feature overview | PACKAGE_SUMMARY.md | All |
| Step-by-step guide | MD_ANALYSIS_README.md | Quick Start |
| Config examples | CONFIG_QUICK_REFERENCE.md | All |
| bioemu setup | BIOEMU_INTEGRATION_GUIDE.md | Step 1-5 |
| Troubleshooting | MD_ANALYSIS_README.md | Troubleshooting |
| Performance tips | MD_ANALYSIS_README.md | Performance Notes |
| Citations | MD_ANALYSIS_README.md | Citation |

---

**Last Updated**: February 2026  
**Version**: 1.0  
**Status**: ✅ Ready for use

Start with **PACKAGE_SUMMARY.md** if you're new!
