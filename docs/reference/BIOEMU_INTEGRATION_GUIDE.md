# Integration Guide: MD_Analysis_Protocol with bioemu

This guide explains how to use `MD_Analysis_Protocol.ipynb` as a post-simulation analysis module in a bioemu-based project.

## Overview

**bioemu** generates GROMACS simulations of any protein. Once simulations are complete:

1. ✅ Extract simulation outputs (`.xtc`, `.gro`, `.tpr`)
2. ✅ Configure `MD_Analysis_Protocol.ipynb` with file paths
3. ✅ Run analysis notebook
4. ✅ Generate publication-ready plots and statistics

## Directory Structure for bioemu Project

```
bioemu_project/
├── README.md
├── INSTALLATION.md
├── SIMULATION_INSTRUCTIONS.md
│
├── simulations/                              # bioemu output folder
│   ├── protein1_variant1/
│   │   ├── em.gro
│   │   ├── production.xtc
│   │   ├── md.log
│   │   └── energy.edr
│   │
│   ├── protein1_variant2/
│   │   ├── em.gro
│   │   ├── production.xtc
│   │   └── ...
│   │
│   └── protein2_variant1/
│       ├── em.gro
│       ├── production.xtc
│       └── ...
│
├── analysis/
│   ├── MD_Analysis_Protocol.ipynb              # <-- Use this notebook
│   ├── ANALYSIS_README.md
│   ├── CONFIG_QUICK_REFERENCE.md
│   ├── analysis_configs/
│   │   ├── protein1_config.py
│   │   └── protein2_config.py
│   │
│   └── results/                                # Generated outputs
│       ├── protein1_analysis_2024-02-03/
│       ├── protein2_analysis_2024-02-03/
│       └── ...
│
└── notebooks/                                  # Jupyter notebooks
    ├── Analysis.ipynb
    ├── Visualization.ipynb
    └── Statistics.ipynb
```

## Step 1: Run bioemu Simulations

```bash
# Example: Simulate multiple proteins with bioemu
bioemu simulate --protein GPCR --variants WT,Y123F,R456Q --replicates 3

# This generates:
# simulations/GPCR_WT_rep1/
# simulations/GPCR_WT_rep2/
# simulations/GPCR_WT_rep3/
# simulations/GPCR_Y123F_rep1/
# ... etc
```

## Step 2: Extract Simulation Files

After bioemu runs, the output folder contains trajectory files. Organize them:

```bash
cd analysis/

# Move or link simulation results
mkdir -p ../simulations
# Copy .xtc and .gro files to simulations/
```

## Step 3: Create Analysis Configuration

Save this as `analysis_configs/protein1_config.py`:

```python
# Configuration for GPCR analysis (bioemu output)

CONFIG = {
    "protein_name": "GPCR",
    "project_name": "bioemu_gpcr_variants",
    "output_dir": "./results/gpcr_2024",
    
    # Define all bioemu simulation outputs
    "systems": {
        "wt_rep1": {
            "label": "WT Replicate 1",
            "topology": "../simulations/GPCR_WT_rep1/em.gro",
            "trajectory": "../simulations/GPCR_WT_rep1/production.xtc",
            "color": "#3498DB",
        },
        "wt_rep2": {
            "label": "WT Replicate 2",
            "topology": "../simulations/GPCR_WT_rep2/em.gro",
            "trajectory": "../simulations/GPCR_WT_rep2/production.xtc",
            "color": "#5DADE2",
        },
        "wt_rep3": {
            "label": "WT Replicate 3",
            "topology": "../simulations/GPCR_WT_rep3/em.gro",
            "trajectory": "../simulations/GPCR_WT_rep3/production.xtc",
            "color": "#85C1E2",
        },
        
        "mut1_rep1": {
            "label": \"Y123F Rep 1\",
            "topology": "../simulations/GPCR_Y123F_rep1/em.gro",
            "trajectory": "../simulations/GPCR_Y123F_rep1/production.xtc",
            "color": "#E74C3C",
        },
        "mut1_rep2": {
            "label": \"Y123F Rep 2\",
            "topology": "../simulations/GPCR_Y123F_rep2/em.gro",
            "trajectory": "../simulations/GPCR_Y123F_rep2/production.xtc",
            "color": "#EC7063",
        },
        "mut1_rep3": {
            "label": \"Y123F Rep 3\",
            "topology": "../simulations/GPCR_Y123F_rep3/em.gro",
            "trajectory": "../simulations/GPCR_Y123F_rep3/production.xtc",
            "color": "#F1948A",
        },
    },
    
    # Protein-specific settings
    "rmsd_rmsf": {
        "enabled": True,
        "atom_selection": "protein and backbone",
        "reference_frame": 0,
    },
    
    "sasa": {
        "enabled": True,
        "frame_stride": 10,
    },
    
    "hbond": {
        "enabled": True,
        "distance_cutoff": 3.5,
        "angle_cutoff": 120.0,
    },
    
    "contacts": {
        "enabled": True,
        "distance_cutoff": 4.5,
    },
    
    # Define secondary structure (if applicable to your protein)
    "secondary_structure": {
        "helices": [
            (25, 55, 'TM1'),   # 7 transmembrane helices for GPCRs
            (64, 97, 'TM2'),
            (105, 140, 'TM3'),
            (157, 187, 'TM4'),
            (199, 229, 'TM5'),
            (243, 273, 'TM6'),
            (285, 310, 'TM7'),
        ],
        "strands": [],
    },
    
    "plotting": {
        "rolling_average_window_ns": 10.0,
        "last_frames_statistics": 500,
        "dpi": 300,
    },
}
```

## Step 4: Run Analysis Notebook

### Option A: Jupyter Interactive

```bash
cd analysis/
jupyter notebook MD_Analysis_Protocol.ipynb

# Then:
# 1. Load the config: exec(open("analysis_configs/protein1_config.py").read())
# 2. Edit CONFIG if needed
# 3. Run all cells
```

### Option B: Command Line (Non-Interactive)

```bash
cd analysis/

# Create a wrapper script:
python << 'EOF'
import json

# Load config
exec(open("analysis_configs/protein1_config.py").read())

# Export to JSON (optional)
with open("loaded_config.json", "w") as f:
    # Filter out non-JSON-serializable objects
    config_json = {k: v for k, v in CONFIG.items() if k != "systems"}
    json.dump(config_json, f, indent=2)

print("✅ Config loaded")
print(f"Systems: {list(CONFIG['systems'].keys())}")
print(f"Output: {CONFIG['output_dir']}")
EOF
```

### Option C: JupyterLab in Batch Mode

```bash
# Install papermill (if not already installed)
pip install papermill

# Create a parameters notebook cell first, then:
papermill MD_Analysis_Protocol.ipynb output.ipynb \
    -p config_file "analysis_configs/protein1_config.py"
```

## Step 5: Review Results

After running the notebook, check the output directory:

```bash
analysis/results/gpcr_2024/
├── rmsd_rmsf/
│   ├── rmsd_comparison.png          # Main RMSD plot
│   ├── rmsf_comparison.png          # Flexibility plot
│   ├── rmsd_all_systems.csv         # Raw data
│   └── rmsf_all_systems.csv
│
├── sasa/
│   ├── wt_rep1_sasa.csv
│   ├── wt_rep2_sasa.csv
│   ├── mut1_rep1_sasa.csv
│   └── ...
│
├── hbonds/
│   └── *_hbonds.csv
│
├── contacts/
│   └── *_contacts.csv
│
├── summary_statistics.csv            # Key metrics table
├── ANALYSIS_REPORT.txt               # Text summary
└── analysis_metadata.json             # Record of what was analyzed
```

## Integration with bioemu Repository

### Add to bioemu README

```markdown
## Post-Simulation Analysis

After running bioemu simulations, use the analysis notebook:

```bash
cd analysis/
jupyter notebook MD_Analysis_Protocol.ipynb
```

See [ANALYSIS_README.md](analysis/ANALYSIS_README.md) for detailed instructions.
```

### Create Standard Config for Each Protein

Save pre-configured files for common proteins:

```
analysis/
├── CONFIG_QUICK_REFERENCE.md
├── analysis_configs/
│   ├── gpcr_config.py              # Pre-filled for GPCRs
│   ├── aquaporin_config.py         # Pre-filled for Aquaporins
│   ├── ion_channel_config.py       # Pre-filled for Ion Channels
│   └── template_config.py           # Template for new proteins
```

### Automated Analysis Script (Optional)

Create `analysis/run_analysis.sh`:

```bash
#!/bin/bash

# Automatically analyze all bioemu outputs

PROTEIN=$1
if [ -z "$PROTEIN" ]; then
    echo "Usage: ./run_analysis.sh <protein_name>"
    echo "Example: ./run_analysis.sh gpcr"
    exit 1
fi

CONFIG_FILE="analysis_configs/${PROTEIN}_config.py"
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Config not found: $CONFIG_FILE"
    exit 1
fi

echo "Running analysis for $PROTEIN..."
echo "Config: $CONFIG_FILE"

python << 'PYTHON_EOF'
import subprocess
exec(open('analysis_configs/' + '${PROTEIN}_config.py').read())

print(f"Output directory: {CONFIG['output_dir']}")
print(f"Systems: {list(CONFIG['systems'].keys())}")

# Would run the notebook here
print("✅ Ready to analyze")
PYTHON_EOF
```

Run with:
```bash
bash run_analysis.sh gpcr
bash run_analysis.sh aquaporin
```

## Publishing Results

### Generate Publication Figure

```python
# In a new notebook cell, after analysis:

import os
import matplotlib.pyplot as plt
from PIL import Image

# Combine multiple analysis plots
fig = plt.figure(figsize=(16, 10))

gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# Load and display plots
rmsd_img = Image.open("results/gpcr_2024/rmsd_rmsf/rmsd_comparison.png")
rmsf_img = Image.open("results/gpcr_2024/rmsd_rmsf/rmsf_comparison.png")

ax1 = fig.add_subplot(gs[0, :])
ax1.imshow(rmsd_img)
ax1.axis('off')

ax2 = fig.add_subplot(gs[1, :])
ax2.imshow(rmsf_img)
ax2.axis('off')

plt.savefig("results/gpcr_2024/combined_analysis.png", dpi=300, bbox_inches='tight')
print("✅ Combined figure saved")
```

### Export Summary Table

```python
import pandas as pd

# Read summary statistics
df_summary = pd.read_csv("results/gpcr_2024/summary_statistics.csv")

# Format for publication
print(df_summary.to_latex(float_format="{:.2f}".format))
```

## Troubleshooting for bioemu Integration

### Issue: File paths don't work
**Solution**: Check that simulation folder structure matches config. Use absolute paths if needed:

```python
import os
base_dir = os.path.abspath("../simulations")
"topology": os.path.join(base_dir, "GPCR_WT_rep1/em.gro"),
```

### Issue: Multiple proteins, don't want to edit notebook manually
**Solution**: Create a master script that selects config:

```python
import sys

protein = sys.argv[1] if len(sys.argv) > 1 else "gpcr"
exec(open(f"analysis_configs/{protein}_config.py").read())

print(f"✅ Loaded config for {protein}")
```

### Issue: Want to analyze subset of simulations
**Solution**: Create variant configs:

```
analysis_configs/
├── gpcr_all.py              # All variants and replicates
├── gpcr_wt_only.py          # Only WT
└── gpcr_variants_rep1.py    # Only first replicate of each variant
```

## Example: Complete bioemu + Analysis Workflow

```bash
# 1. Run bioemu
bioemu simulate --protein GPCR --variants WT,Y123F --replicates 2

# 2. Move results
mv GPCR_* simulations/

# 3. Configure analysis
cd analysis/
# (Edit/create analysis_configs/gpcr_config.py)

# 4. Run notebook
jupyter notebook MD_Analysis_Protocol.ipynb
# Load config and run all cells

# 5. Review results
open results/gpcr_2024/rmsd_rmsf/rmsd_comparison.png

# 6. Export for publication
# (Summary statistics already in summary_statistics.csv)
```

## Next Steps

1. **Integrate into bioemu** repository
2. **Create protein-specific configs** for common proteins
3. **Add to CI/CD pipeline** to auto-analyze new simulations
4. **Create Jupyter hub server** for collaborative analysis
5. **Develop web dashboard** to visualize results

---

**Integration Last Updated**: February 2026
