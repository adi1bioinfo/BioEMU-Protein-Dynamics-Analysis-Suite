# API Reference

Complete documentation of all utility functions and classes in BioEMU Analysis Suite.

## Table of Contents

1. [trajectory_loader](#trajectory_loader)
2. [analysis_functions](#analysis_functions)
3. [visualization](#visualization)
4. [Configuration](#configuration)

---

## trajectory_loader

Functions for loading and validating MD simulation data.

### `load_trajectory(topology, trajectory)`

Load a molecular dynamics trajectory using MDAnalysis.

**Parameters:**
- `topology` (str): Path to topology file (.gro, .pdb, .psf, etc.)
- `trajectory` (str): Path to trajectory file (.xtc, .trr, .dcd, etc.)

**Returns:**
- `mda.Universe`: MDAnalysis Universe object

**Raises:**
- `FileNotFoundError`: If topology or trajectory file not found
- `ValueError`: If file format not recognized

**Example:**
```python
import MDAnalysis as mda
from utils.trajectory_loader import load_trajectory

# Load trajectory
u = load_trajectory(
    topology="./data/structure.gro",
    trajectory="./data/trajectory.xtc"
)

print(f"Loaded {len(u.trajectory)} frames")
print(f"Number of atoms: {u.atoms.n_atoms}")
```

---

### `validate_files(config)`

Validate that all files specified in CONFIG dictionary exist.

**Parameters:**
- `config` (dict): CONFIG dictionary with systems definition

**Returns:**
- `dict`: Dictionary of validation results:
  - `"valid"` (bool): Whether all files exist
  - `"missing_files"` (list): List of missing file paths
  - `"status"` (dict): Per-system validation status

**Raises:**
- `FileNotFoundError`: If critical files are missing

**Example:**
```python
from utils.trajectory_loader import validate_files

CONFIG = {
    "systems": {
        "system_1": {
            "topology": "./data/structure.gro",
            "trajectory": "./data/trajectory.xtc"
        }
    }
}

result = validate_files(CONFIG)
print(result["status"])  # {"system_1": True}
print(result["valid"])   # True
```

---

### `get_trajectory_info(universe)`

Get basic information about a loaded trajectory.

**Parameters:**
- `universe` (mda.Universe): MDAnalysis Universe object

**Returns:**
- `dict`: Information dictionary containing:
  - `"n_atoms"` (int): Total number of atoms
  - `"n_frames"` (int): Number of frames in trajectory
  - `"n_residues"` (int): Number of residues
  - `"dt_ps"` (float): Time step in picoseconds
  - `"total_time_ns"` (float): Total simulation time in nanoseconds

**Example:**
```python
from utils.trajectory_loader import load_trajectory, get_trajectory_info

u = load_trajectory("structure.gro", "trajectory.xtc")
info = get_trajectory_info(u)

print(f"Simulation: {info['total_time_ns']:.1f} ns")
print(f"Frames: {info['n_frames']}")
```

---

## analysis_functions

Functions for computing molecular properties and structural metrics.

### `calculate_rmsd_rmsf(universe, selection='protein and name CA', ref_frame=0)`

Calculate Root Mean Square Deviation (RMSD) and Root Mean Square Fluctuation (RMSF).

**Parameters:**
- `universe` (mda.Universe): MDAnalysis Universe object
- `selection` (str): MDAnalysis atom selection string (default: C-alpha atoms)
- `ref_frame` (int): Reference frame for RMSD calculation (default: 0, first frame)

**Returns:**
- `tuple`: (rmsd_array, rmsf_array, time_array)
  - `rmsd_array` (np.ndarray): RMSD in Angstroms, shape (n_frames,)
  - `rmsf_array` (np.ndarray): RMSF per residue, shape (n_residues,)
  - `time_array` (np.ndarray): Time in picoseconds, shape (n_frames,)

**Example:**
```python
from utils.analysis_functions import calculate_rmsd_rmsf

rmsd, rmsf, time = calculate_rmsd_rmsf(
    universe=u,
    selection="protein and name CA"
)

print(f"Average RMSD: {rmsd.mean():.2f} Å")
print(f"RMSF range: {rmsf.min():.2f} - {rmsf.max():.2f} Å")

# Create DataFrame for analysis
import pandas as pd
df = pd.DataFrame({
    "Time_ps": time,
    "RMSD_A": rmsd
})
```

---

### `calculate_sasa(universe, probe_radius=1.4, frame_stride=1)`

Calculate Solvent Accessible Surface Area (SASA) using Shrake-Rupley algorithm.

**Parameters:**
- `universe` (mda.Universe): MDAnalysis Universe object
- `probe_radius` (float): Probe radius in Angstroms (default: 1.4 for water)
- `frame_stride` (int): Process every Nth frame (default: 1, all frames)

**Returns:**
- `dict`: Dictionary with keys:
  - `"total_sasa"` (np.ndarray): Total SASA per frame, shape (n_frames,)
  - `"residue_sasa"` (np.ndarray): Per-residue SASA, shape (n_frames, n_residues)
  - `"residue_names"` (list): Residue names
  - `"residue_numbers"` (list): Residue numbers
  - `"time_ps"` (np.ndarray): Time points

**Example:**
```python
from utils.analysis_functions import calculate_sasa

sasa_data = calculate_sasa(
    universe=u,
    probe_radius=1.4,
    frame_stride=10  # Every 10th frame for speed
)

# Find most exposed residues
residue_avg = sasa_data["residue_sasa"].mean(axis=0)
most_exposed_idx = residue_avg.argsort()[-5:]  # Top 5

for idx in most_exposed_idx:
    print(f"{sasa_data['residue_numbers'][idx]}: "
          f"{residue_avg[idx]:.1f} Ų")
```

---

### `calculate_hydrogen_bonds(universe, distance_cutoff=3.5, angle_cutoff=120.0)`

Identify and count hydrogen bonds throughout trajectory.

**Parameters:**
- `universe` (mda.Universe): MDAnalysis Universe object
- `distance_cutoff` (float): H-acceptor distance cutoff in Angstroms (default: 3.5)
- `angle_cutoff` (float): D-H-A angle cutoff in degrees (default: 120.0)

**Returns:**
- `dict`: Hydrogen bond analysis data:
  - `"hbond_count"` (np.ndarray): Number of H-bonds per frame, shape (n_frames,)
  - `"hbond_pairs"` (list): List of (donor_resnum, acceptor_resnum) pairs
  - `"occupancy"` (dict): Per-pair occupancy (fraction of frames present)
  - `"time_ps"` (np.ndarray): Time points

**Example:**
```python
from utils.analysis_functions import calculate_hydrogen_bonds

hbonds = calculate_hydrogen_bonds(
    universe=u,
    distance_cutoff=3.5,
    angle_cutoff=120.0
)

print(f"Average H-bonds: {hbonds['hbond_count'].mean():.1f}")

# Find persistent H-bonds (>80% occupancy)
persistent = {k: v for k, v in hbonds["occupancy"].items() 
              if v > 0.8}
print(f"Persistent H-bonds: {len(persistent)}")
```

---

### `calculate_contact_map(universe, selection1, selection2, distance_cutoff=4.5)`

Calculate contact matrix between two atom selections.

**Parameters:**
- `universe` (mda.Universe): MDAnalysis Universe object
- `selection1` (str): First atom selection
- `selection2` (str): Second atom selection
- `distance_cutoff` (float): Contact distance threshold in Angstroms

**Returns:**
- `dict`: Contact analysis data:
  - `"contact_map"` (np.ndarray): Contact matrix, shape (n_atoms1, n_atoms2, n_frames)
  - `"occupancy"` (np.ndarray): Contact occupancy, shape (n_atoms1, n_atoms2)
  - `"distances"` (np.ndarray): Average distances, shape (n_atoms1, n_atoms2)

**Example:**
```python
from utils.analysis_functions import calculate_contact_map

contacts = calculate_contact_map(
    universe=u,
    selection1="resid 3:26 and name CA",  # Helix 1
    selection2="resid 27:47 and name CA",  # Helix 2
    distance_cutoff=5.0
)

occupancy = contacts["occupancy"]
print(f"Contact occupancy shape: {occupancy.shape}")
```

---

## visualization

Functions for creating publication-quality plots.

### `plot_rmsd(df_rmsd, config, save_path=None)`

Plot RMSD comparison for multiple systems.

**Parameters:**
- `df_rmsd` (pd.DataFrame): DataFrame with columns ['System', 'Time_ps', 'RMSD_A']
- `config` (dict): Configuration dictionary with plotting settings
- `save_path` (str): Path to save figure (default: None, don't save)

**Returns:**
- `None`: Displays plot

**Configuration Options:**
```python
CONFIG = {
    "plotting": {
        "style": "seaborn-v0_8-darkgrid",
        "figsize": (14, 6),
        "dpi": 100,
        "fontsize": 12,
    },
    "colors": {
        "system_1": "#FF6B6B",
        "system_2": "#4ECDC4",
    },
    "rmsd_rmsf": {
        "rolling_window": 10,  # Frames for rolling average
    }
}
```

**Example:**
```python
from utils.visualization import plot_rmsd
import pandas as pd

# Load RMSD data
df_rmsd = pd.read_csv("./results/rmsd_rmsf/rmsd_all.csv")

plot_rmsd(
    df_rmsd=df_rmsd,
    config=CONFIG,
    save_path="./results/rmsd_comparison.png"
)
```

---

### `plot_rmsf(df_rmsf, config, save_path=None)`

Plot per-residue flexibility (RMSF).

**Parameters:**
- `df_rmsf` (pd.DataFrame): DataFrame with columns ['Residue', 'ResidueNum', 'System', 'RMSF_A']
- `config` (dict): Configuration dictionary
- `save_path` (str): Path to save figure

**Returns:**
- `None`: Displays plot

**Example:**
```python
from utils.visualization import plot_rmsf

df_rmsf = pd.read_csv("./results/rmsd_rmsf/rmsf_all.csv")

plot_rmsf(
    df_rmsf=df_rmsf,
    config=CONFIG,
    save_path="./results/rmsf_comparison.png"
)
```

---

### `plot_sasa_heatmap(df_sasa, config, save_path=None, top_residues=20)`

Plot most exposed residues as heatmap.

**Parameters:**
- `df_sasa` (pd.DataFrame): DataFrame with SASA per residue
- `config` (dict): Configuration dictionary
- `save_path` (str): Path to save figure
- `top_residues` (int): Number of most exposed residues to plot (default: 20)

**Returns:**
- `None`: Displays plot

**Example:**
```python
from utils.visualization import plot_sasa_heatmap

df_sasa = pd.read_csv("./results/sasa/sasa_residue.csv")

plot_sasa_heatmap(
    df_sasa=df_sasa,
    config=CONFIG,
    save_path="./results/sasa_heatmap.png",
    top_residues=15
)
```

---

### `plot_distance_timeseries(times, distances_dict, labels, colors, title="Distance Dynamics")`

Plot multiple distance measurements on single plot.

**Parameters:**
- `times` (np.ndarray): Time in picoseconds
- `distances_dict` (dict): Dictionary of {label: distance_array}
- `labels` (list): List of distance labels for legend
- `colors` (list): List of colors matching labels
- `title` (str): Plot title

**Returns:**
- `None`: Displays plot

**Example:**
```python
from utils.visualization import plot_distance_timeseries
import numpy as np

times = np.arange(0, 10000, 1)  # 10 μs at 1 ps resolution
distances = {
    "H1-H2": np.random.randn(10000).cumsum() + 20,
    "H1-H3": np.random.randn(10000).cumsum() + 25,
}

plot_distance_timeseries(
    times=times,
    distances_dict=distances,
    labels=["Helix 1-2", "Helix 1-3"],
    colors=["#FF6B6B", "#4ECDC4"],
    title="Inter-helical Distance Evolution"
)
```

---

### `plot_hydrogen_bond_occupancy(df_hbonds, title="Hydrogen Bond Occupancy", top_n=15)`

Plot hydrogen bond occupancy as horizontal bar chart.

**Parameters:**
- `df_hbonds` (pd.DataFrame): DataFrame with columns ['ResidueA', 'ResidueB', 'Occupancy']
- `title` (str): Plot title
- `top_n` (int): Number of top H-bonds to display (default: 15)

**Returns:**
- `None`: Displays plot

**Example:**
```python
from utils.visualization import plot_hydrogen_bond_occupancy

df_hbonds = pd.read_csv("./results/hbonds/hbonds_summary.csv")

plot_hydrogen_bond_occupancy(
    df_hbonds=df_hbonds,
    title="Persistent Hydrogen Bonds",
    top_n=20
)
```

---

## Configuration

### CONFIG Dictionary Structure

Complete reference for the CONFIG dictionary used throughout the analysis.

**Template:**
```python
CONFIG = {
    # System definitions
    "systems": {
        "system_name": {
            "label": "Display name",
            "topology": "./path/to/structure.gro",
            "trajectory": "./path/to/trajectory.xtc",
            "color": "#FF6B6B"
        },
        # Add more systems as needed
    },
    
    # Analysis parameters
    "analyses": {
        "rmsd_rmsf": {
            "enabled": True,
            "selection": "protein and name CA",
            "ref_frame": 0,
        },
        "sasa": {
            "enabled": True,
            "probe_radius": 1.4,
            "frame_stride": 10,
        },
        "inter_helical": {
            "enabled": True,
            "helices": {
                "H1": "resid 3:26",
                "H2": "resid 27:47",
            },
            "distance_pairs": [("H1", "H2"), ("H1", "H3")],
        },
        "pore_hydration": {
            "enabled": True,
            "pore_residues": [50, 51, 52, 53],
            "water_cutoff_angstrom": 5.0,
        },
        "water_bridges": {
            "enabled": True,
            "residue_pairs": [(10, 20), (30, 40)],
            "distance_cutoff": 3.5,
        },
        "minimum_distance": {
            "enabled": True,
            "selection_1": "resid 10:15",
            "selection_2": "resid 40:45",
        },
        "hydrogen_bonds": {
            "enabled": True,
            "distance_cutoff": 3.5,
            "angle_cutoff": 120.0,
        },
    },
    
    # Plotting parameters
    "plotting": {
        "style": "seaborn-v0_8-darkgrid",
        "figsize": (14, 8),
        "dpi": 100,
        "fontsize": 12,
        "colors": {
            "system_1": "#FF6B6B",
            "system_2": "#4ECDC4",
        }
    }
}
```

---

### Atom Selection Syntax

Valid MDAnalysis selection strings:

```python
# Protein/nucleic acid
"protein"                # All protein atoms
"nucleic"                # All nucleic acid atoms
"backbone"               # Backbone atoms (CA, C, N, O)
"name CA"                # C-alpha atoms
"name CB"                # Beta carbon atoms

# Residue-based
"resid 3:26"             # Residues 3-26 (inclusive)
"resnum 100"             # Single residue 100
"resi 1-10"              # Alternative syntax: residues 1-10

# Atom name/type
"name CA CB"             # CA or CB atoms
"type C N"               # C or N atom types

# Residue type
"residue ALA"            # Alanine residues
"resname GLY"            # Glycine residues
"resname ALA GLY VAL"    # Multiple residue types

# Charge/mass
"charge +1"              # Positive charges
"mass > 12"              # Atoms heavier than carbon

# Combinations (boolean operators)
"protein and name CA"    # AND operator
"protein and resid 3:26" # Protein atoms in residues 3-26
"resid 1:50 or resid 100:150"  # OR operator
"(resid 3:26) and not name H"  # NOT operator (heavy atoms in H1)

# Distance-based
"around 5 resid 50"      # Within 5 Å of residue 50
```

---

## Usage Examples

### Complete Analysis Workflow

```python
import pandas as pd
from utils.trajectory_loader import load_trajectory, validate_files
from utils.analysis_functions import (
    calculate_rmsd_rmsf,
    calculate_sasa,
    calculate_hydrogen_bonds
)
from utils.visualization import plot_rmsd, plot_sasa_heatmap

# Configure
CONFIG = { ... }  # See QUICK_REFERENCE.md

# Validate
validate_files(CONFIG)

# Load trajectory
u = load_trajectory(
    topology=CONFIG["systems"]["system_1"]["topology"],
    trajectory=CONFIG["systems"]["system_1"]["trajectory"]
)

# Run analyses
rmsd, rmsf, time = calculate_rmsd_rmsf(u, "protein and name CA")
sasa_data = calculate_sasa(u, frame_stride=10)
hbonds = calculate_hydrogen_bonds(u)

# Create dataframes
df_rmsd = pd.DataFrame({
    "Time_ps": time,
    "RMSD_A": rmsd,
    "System": "My System"
})

# Plot
plot_rmsd(df_rmsd, CONFIG, "rmsd_plot.png")
```

---

**Last Updated:** February 2025
