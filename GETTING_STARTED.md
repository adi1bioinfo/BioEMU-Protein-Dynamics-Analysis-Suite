# Getting Started

Complete walkthrough to run your first analysis in 15 minutes.

## 5-Minute Setup

### Step 1: Install Python (if needed)

**Linux/macOS:**
```bash
# Check if Python installed
python3 --version

# If not installed:
# macOS
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-pip
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during install

---

### Step 2: Create Virtual Environment

**Linux/macOS:**
```bash
cd BioEMU-Protein-Dynamics

# Create environment
python3 -m venv bioemu-env

# Activate
source bioemu-env/bin/activate

# You should see (bioemu-env) in your prompt
```

**Windows (PowerShell):**
```powershell
cd BioEMU-Protein-Dynamics

# Create environment
python -m venv bioemu-env

# Activate
.\bioemu-env\Scripts\Activate.ps1

# If error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

**Or use conda (recommended for scientific packages):**
```bash
conda env create -f environment.yml
conda activate bioemu
```

---

### Step 4: Verify Installation

```bash
python -c "import MDAnalysis; import mdtraj; print('✅ Ready!')"
```

---

## 10-Minute First Run

### Option A: Use Example KDEL Data

The repository includes example data to test the analysis:

```bash
# Navigate to notebook
cd BioEMU-Protein-Dynamics

# Start Jupyter
jupyter notebook Comprehensive_Analysis.ipynb
```

**In Jupyter:**

1. **Open the notebook** - Click on `Comprehensive_Analysis.ipynb`

2. **Edit Cell 1 (CONFIG):**
   ```python
   CONFIG = {
       "systems": {
           "kdel_example": {
               "label": "KDEL Receptor",
               "topology": "./data/kdel_example/structure.gro",
               "trajectory": "./data/kdel_example/trajectory.xtc",
               "color": "#FF6B6B"
           }
       },
       "analyses": {
           "rmsd_rmsf": {"enabled": True},
           "sasa": {"enabled": False},  # Skip slow analysis
           "water_bridges": {"enabled": False},
       },
       "plotting": {"figsize": (14, 6), "dpi": 100}
   }
   ```

3. **Run cells in order:** `Cell` → `Run All`

4. **Check results:**
   ```bash
   ls -la results/
   ```

---

### Option B: Use Your Own Data

1. **Prepare your files:**
   ```bash
   # Create data directory
   mkdir -p data/my_system/
   
   # Copy your files
   cp /path/to/structure.gro data/my_system/
   cp /path/to/trajectory.xtc data/my_system/
   ```

2. **Edit CONFIG in Cell 1:**
   ```python
   CONFIG = {
       "systems": {
           "my_system": {
               "label": "My Protein",
               "topology": "./data/my_system/structure.gro",
               "trajectory": "./data/my_system/trajectory.xtc",
               "color": "#FF6B6B"
           }
       },
       "analyses": {
           "rmsd_rmsf": {"enabled": True},
           # Add other analyses as needed
       }
   }
   ```

3. **Run the notebook**

4. **Find results in** `results/` directory

---

## Understanding the Results

### After running the analysis, you'll see:

```
results/
├── rmsd_rmsf/
│   ├── rmsd_all.csv          # RMSD vs time
│   └── rmsf_all.csv          # Per-residue flexibility
├── sasa/
│   ├── sasa_total.csv        # Total accessible surface area
│   └── sasa_residue.csv      # Per-residue values
├── water_bridges/
│   └── water_bridges.csv     # Water-mediated interactions
├── hydrogen_bonds/
│   └── hbonds.csv            # H-bond occupancy
└── plots/
    ├── rmsd_comparison.png   # RMSD plot
    ├── rmsf_comparison.png   # Flexibility plot
    ├── sasa_heatmap.png      # Exposed residues
    └── hbonds_bar.png        # H-bond frequencies
```

---

### Key Output Files Explained

#### `rmsd_all.csv` - Protein Stability
```
Time_ps,System,RMSD_A
0.0,kdel_example,0.0
100.0,kdel_example,1.23
200.0,kdel_example,1.45
...
```
- **Low RMSD** = Stable structure
- **Increasing RMSD** = Unfolding or drift
- **Plateauing RMSD** = Equilibrated system

#### `rmsf_all.csv` - Flexibility per Residue
```
ResidueNum,Residue,System,RMSF_A
1,MET,kdel_example,0.45
2,ASP,kdel_example,0.78
...
```
- **High RMSF** = Flexible regions (loops, domains)
- **Low RMSF** = Stable regions (secondary structure)

#### `sasa_residue.csv` - Surface Exposure
```
ResidueNum,Residue,SASA_avg,SASA_std
1,MET,120.5,15.3
2,ASP,95.2,12.1
...
```
- Tells you which residues are most exposed to solvent
- Useful for identifying binding pockets or accessible regions

---

## Common Tasks

### Task 1: Analyze Multiple Systems at Once

```python
CONFIG = {
    "systems": {
        "WT": {
            "label": "Wild Type",
            "topology": "./data/wt/structure.gro",
            "trajectory": "./data/wt/trajectory.xtc",
            "color": "#FF6B6B"
        },
        "mutant": {
            "label": "L45A Mutant",
            "topology": "./data/mutant/structure.gro",
            "trajectory": "./data/mutant/trajectory.xtc",
            "color": "#4ECDC4"
        }
    },
    # Rest of config...
}
```

Then run - both systems will be analyzed and plotted together!

---

### Task 2: Focus on Specific Regions

**Analyze only a domain:**
```python
CONFIG = {
    "analyses": {
        "rmsd_rmsf": {
            "selection": "resid 3:26 and name CA",  # Only helix 1
        }
    }
}
```

**Analyze inter-helical dynamics:**
```python
"inter_helical": {
    "enabled": True,
    "helices": {
        "TM1": "resid 3:26",
        "TM2": "resid 27:47",
        "TM3": "resid 48:68",
    },
    "distance_pairs": [
        ("TM1", "TM2"),
        ("TM1", "TM3"),
        ("TM2", "TM3"),
    ]
}
```

---

### Task 3: Speed Up Analysis

For large trajectories, use frame stride:

```python
CONFIG = {
    "analyses": {
        "rmsd_rmsf": {
            "enabled": True,
            # Default: process every frame
        },
        "sasa": {
            "enabled": True,
            "frame_stride": 50,  # Process every 50th frame
        },
        "water_bridges": {
            "enabled": True,
            "frame_stride": 100,  # Process every 100th frame
        }
    }
}
```

**Speed comparison:**
- No stride: 10 μs trajectory = 10,000 frames, 2-3 hours
- stride=10: Same trajectory = 1,000 frames, 20-30 minutes
- stride=100: Same trajectory = 100 frames, 2-3 minutes

---

### Task 4: Generate Publication-Ready Figures

Use higher DPI and larger figures:

```python
CONFIG = {
    "plotting": {
        "figsize": (16, 10),    # Larger figure
        "dpi": 300,              # Publication quality
        "fontsize": 14,          # Larger fonts
        "style": "seaborn-v0_8-whitegrid",
    }
}
```

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'MDAnalysis'"

**Solution:**
```bash
# Make sure environment is activated
source bioemu-env/bin/activate  # macOS/Linux

# Reinstall
pip install --upgrade MDAnalysis
```

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for more issues.

---

### Problem: "FileNotFoundError: trajectory file not found"

**Solution:**
```bash
# Check files exist
ls -la data/my_system/
# Output should show your structure.gro and trajectory.xtc

# Use absolute paths
"topology": "/home/user/BioEMU-Protein-Dynamics/data/my_system/structure.gro"
```

---

### Problem: Out of Memory

**Solution:**
```python
# Add frame stride to all analyses
"frame_stride": 100,  # Process every 100th frame
```

---

## Next Steps

After your first analysis:

1. **Read the analysis explanations:** [docs/ANALYSIS_GUIDE.md](docs/ANALYSIS_GUIDE.md)
   - Understand what each analysis reveals about your protein

2. **Explore configuration templates:** [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)
   - Copy templates for GPCR, ion channels, transporters, etc.

3. **Use the API reference:** [docs/API_REFERENCE.md](docs/API_REFERENCE.md)
   - Learn to write custom analysis scripts

4. **Check examples:** `examples/` directory
   - See how KDEL receptor was analyzed
   - Adapt to your protein

---

## Advanced: Running Python Scripts

Instead of Jupyter, you can run analyses via Python script:

**create_analysis.py:**
```python
#!/usr/bin/env python3

import pandas as pd
from utils.trajectory_loader import load_trajectory
from utils.analysis_functions import calculate_rmsd_rmsf, calculate_sasa
from utils.visualization import plot_rmsd, plot_sasa_heatmap

# Configuration
CONFIG = {
    "systems": {
        "my_system": {
            "topology": "./data/structure.gro",
            "trajectory": "./data/trajectory.xtc",
            "label": "My Protein"
        }
    },
    "analyses": {
        "rmsd_rmsf": {"enabled": True},
        "sasa": {"enabled": True, "frame_stride": 10}
    },
    "plotting": {"figsize": (14, 6), "dpi": 100}
}

# Load
sys_name = "my_system"
sys_cfg = CONFIG["systems"][sys_name]
u = load_trajectory(sys_cfg["topology"], sys_cfg["trajectory"])

# Analyze
rmsd, rmsf, time = calculate_rmsd_rmsf(u)
sasa_data = calculate_sasa(u, frame_stride=10)

# Save
df_rmsd = pd.DataFrame({
    "Time_ps": time,
    "RMSD_A": rmsd,
    "System": sys_cfg["label"]
})
df_rmsd.to_csv("results/rmsd.csv", index=False)

print("✅ Analysis complete!")
print(f"Average RMSD: {rmsd.mean():.2f} Ų")
```

**Run it:**
```bash
python create_analysis.py
```

---

## Finding Help

- **Installation issues:** [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- **Analysis explanations:** [docs/ANALYSIS_GUIDE.md](docs/ANALYSIS_GUIDE.md)
- **Configuration examples:** [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)
- **Function reference:** [docs/API_REFERENCE.md](docs/API_REFERENCE.md)
- **Report a bug:** [GitHub Issues](https://github.com/your-username/BioEMU-Protein-Dynamics/issues)

---

**Happy analyzing! 🧬**
  ```python
  "topology": "./data/system_1/em.gro",  # Change paths here
  "trajectory": "./data/system_1/production.xtc",
  ```
- [ ] Update protein name and system labels

## First Run (variable time - depends on trajectory size)

Open Jupyter:
```bash
jupyter notebook MD_Analysis_Protocol.ipynb
```

- [ ] **Cell 1**: Run configuration cell
  - See: ✅ Configuration loaded
  - See: ✅ All system files verified
  
- [ ] **Cell 2**: Run utility functions
  - Just loads helper functions
  
- [ ] **Cell 3**: Run RMSD/RMSF calculation
  - Takes 1-5 minutes depending on trajectory size
  - Should see progress messages
  
- [ ] **Cell 4**: Run RMSD/RMSF plots
  - Should display two plots
  - Check if they look reasonable
  
- [ ] **Cells 5-7**: Run remaining analyses
  - SASA (takes longer if large trajectory)
  - Hydrogen bonds
  - Contacts
  
- [ ] **Cell 8**: Run summary statistics
  - Should see a table with statistics
  
- [ ] **Cell 9**: Run final report
  - Check results folder

## Verify Results (5 minutes)

Check these files in your output folder:

### Must have (basic analyses):
- [ ] `rmsd_rmsf/rmsd_comparison.png` (main plot)
- [ ] `rmsd_rmsf/rmsf_comparison.png` (flexibility plot)
- [ ] `summary_statistics.csv` (numbers table)

### Optional (depending on what you enabled):
- [ ] `sasa/system_*_sasa.csv` (surface area data)
- [ ] `hbonds/system_*_hbonds.csv` (hydrogen bonds)
- [ ] `contacts/system_*_contacts.csv` (residue contacts)
- [ ] `ANALYSIS_REPORT.txt` (summary text)

## Troubleshooting

**Problem**: Topology file not found
```
✗ ❌ ./data/system_1/em.gro
```
**Solution**: 
- Check file path is correct
- Use absolute paths if relative paths don't work
- Ensure forward slashes `/` not backslashes `\`

**Problem**: "No atoms selected"
**Solution**:
- Verify your MDAnalysis selection string
- Test with `"protein"` (simplest selection)
- See MDAnalysis docs: https://www.mdanalysis.org/docs/documentation_pages/selections.html

**Problem**: Memory error during SASA analysis
**Solution**:
- Increase `frame_stride` (process fewer frames): `"frame_stride": 50`
- This will run 5-10x faster

**Problem**: Analysis runs but plots are empty
**Solution**:
- Check data was loaded: look at CSV files in output folder
- Try simpler atom selection in CONFIG
- See MD_ANALYSIS_README.md → Troubleshooting

## Next Steps After First Run

### Option 1: Analyze More Proteins
- [ ] Update file paths in CONFIG
- [ ] Re-run notebook

### Option 2: Customize Analysis
- [ ] Edit analysis options (which to enable/disable)
- [ ] Adjust rolling average window size
- [ ] Change colors and labels
- [ ] Add secondary structure definitions

### Option 3: Prepare for Publication
- [ ] Run with all analyses enabled
- [ ] Check plots at 300 DPI
- [ ] Export summary_statistics.csv
- [ ] Use BIOEMU_INTEGRATION_GUIDE.md for multi-panel figures

### Option 4: Automate for bioemu
- [ ] Follow BIOEMU_INTEGRATION_GUIDE.md
- [ ] Create pre-configured analysis_configs/
- [ ] Set up automated runs for all simulations

## Common Configuration Changes

### Disable Analyses (to speed up)
```python
"rmsd_rmsf": {"enabled": False},  # Skip RMSD/RMSF
"sasa": {"enabled": False},       # Skip SASA
"hbond": {"enabled": False},      # Skip H-bonds
"contacts": {"enabled": False},   # Skip contacts
```

### Change colors
```python
"color": "#FF6B6B",  # Change hex color
```

### Add secondary structure annotations
```python
"secondary_structure": {
    "helices": [(3, 26, 'H1'), (34, 52, 'H2')],
    "strands": [(10, 20, 'S1')],
},
```

### Change output directory
```python
"output_dir": "/path/to/my/results",
```

### Add more systems to compare
```python
"systems": {
    "system_1": {...},
    "system_2": {...},
    "system_3": {...},  # Add new ones
    "system_4": {...},
}
```

## File Size & Time Estimates

| Trajectory | Analysis | Time |
|-----------|----------|------|
| 1,000 frames | All | 5-10 min |
| 10,000 frames | All | 30-60 min |
| 100,000 frames | All* | 2-6 hours |

*Use frame_stride=50 or higher for faster analysis

## Help Resources

1. **Getting started**: Read PACKAGE_SUMMARY.md (5 min)
2. **Configuration help**: Check CONFIG_QUICK_REFERENCE.md
3. **Detailed guide**: Read MD_ANALYSIS_README.md
4. **bioemu integration**: Read BIOEMU_INTEGRATION_GUIDE.md
5. **Troubleshooting**: MD_ANALYSIS_README.md → Troubleshooting section

## Documentation Map

```
START HERE
    ↓
INDEX.md (you are here)
    ↓
PACKAGE_SUMMARY.md (5 min overview)
    ↓
CONFIG_QUICK_REFERENCE.md (find your protein)
    ↓
MD_Analysis_Protocol.ipynb (open in Jupyter)
    ↓
MD_ANALYSIS_README.md (detailed help if needed)
    ↓
BIOEMU_INTEGRATION_GUIDE.md (if using bioemu)
```

## Quick Commands Reference

```bash
# Activate environment
conda activate md_analysis

# Start Jupyter
jupyter notebook

# Check if dependencies installed
python -c "import MDAnalysis, mdtraj; print('OK')"

# Run analysis (non-interactive)
papermill MD_Analysis_Protocol.ipynb output.ipynb
```

## Success Criteria

You'll know the analysis worked when you see:
✅ Files created in output folder  
✅ RMSD/RMSF plots displayed  
✅ Summary statistics printed  
✅ CSV data files with numerical results  
✅ ANALYSIS_REPORT.txt generated  

## Common Proteins - Quick Config Lookup

| Protein | Config | Systems |
|---------|--------|---------|
| GPCR | See CONFIG_QUICK_REFERENCE.md | Apo, Agonist, Antagonist |
| Ion Channel | See CONFIG_QUICK_REFERENCE.md | Open, Closed |
| Aquaporin | See CONFIG_QUICK_REFERENCE.md | Water-filled, Empty |
| Enzyme | See CONFIG_QUICK_REFERENCE.md | Apo, Bound, Inhibited |
| Membrane protein | See MD_ANALYSIS_README.md | Any condition |

## When Stuck

1. **Check the error message** - usually very specific
2. **Look at MD_ANALYSIS_README.md** → Troubleshooting section
3. **Find your protein type** in CONFIG_QUICK_REFERENCE.md
4. **Copy a working example** and modify paths only
5. **Test with simplest config first**

## Ready? 

- [ ] All boxes above checked?
- [ ] Files copied to project?
- [ ] Configuration edited?
- [ ] Dependencies installed?

→ **Open Jupyter and run the notebook!**

```bash
jupyter notebook MD_Analysis_Protocol.ipynb
```

---

**Questions?** Review MD_ANALYSIS_README.md first - it likely answers your question!

**First time with this?** Start with PACKAGE_SUMMARY.md for a 5-minute overview.
