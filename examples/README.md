# BioEMU Analysis Examples

This library enables a **hybrid workflow**:
1.  **Generate data** using BioEMU (or standard MD).
2.  **Analyze** it using this suite.

We provide a complete, ready-to-run example using the **KDEL Receptor**.

---

## 🚀 Running the Example (Batteries Included)

We have included a 10ns simulation trajectory for the KDEL receptor so you can test the analysis suite immediately.

### 1. Locate the Data
The example data is in `examples/kdel_analysis/starter_data/`:
- `kdel_receptor_structure.gro`: The protein structure.
- `kdel_receptor_10ns_simulation.xtc`: A short 10ns trajectory.

### 2. Run the Analysis
1.  Open the main notebook: `Comprehensive_Analysis.ipynb` (at the root of the repo).
2.  In the **Configuration** cell, you can load the example config directly:
    ```python
    # Import the pre-made configuration
    import sys
    sys.path.append('./examples/kdel_analysis')
    from kdel_config import CONFIG
    
    # Or simply copy-paste the dictionary from kdel_config.py
    ```
3.  Run all cells.
4.  Check the `kdel_analysis_results/` folder for plots and reports.

---

## 🪄 Using Your Own Data

To analyze your own protein (e.g., from a BioEMU generation or GROMACS run):

1.  **Prepare your files**: You need a topology (`.pdb`, `.gro`) and a trajectory (`.xtc`, `.dcd`).
2.  **Edit the Configuration**:
    In the `Comprehensive_Analysis.ipynb` notebook, modify the `CONFIG` dictionary:
    
    ```python
    CONFIG = {
        "protein_name": "My Ion Channel",
        "output_dir": "./results_my_protein",
        "systems": {
            "wild_type": {
                "label": "Wild Type",
                "topology": "/path/to/my_data/structure.pdb",
                "trajectory": "/path/to/my_data/bioemu_samples.xtc",
                "color": "blue"
            },
            # Add more systems to compare if needed
             "mutant": { ... }
        },
        # ... enable/disable analyses below
    }
    ```

## 🧬 BioEMU Workflow
If you are generating ensembles with BioEMU:
1.  Run BioEMU to get PDB samples.
2.  Convert samples to a single trajectory `.xtc` (using `mdtraj` or `gromacs`).
3.  Analysis steps are identical to the above!

---
