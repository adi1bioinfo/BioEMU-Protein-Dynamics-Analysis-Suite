# Quick Reference - Configuration Templates

Copy and paste the relevant CONFIG dictionary into the notebook's first cell.

## Template 1: General Protein (Minimal Config)

```python
CONFIG = {
    "protein_name": "MyProtein",
    "output_dir": "./results",
    
    "systems": {
        "system1": {
            "label": "System 1",
            "topology": "./data/system1/structure.gro",
            "trajectory": "./data/system1/trajectory.xtc",
            "color": "#FF6B6B",
        },
    },
    
    "rmsd_rmsf": {"enabled": True, "atom_selection": "protein and backbone"},
    "sasa": {"enabled": True},
    "hbond": {"enabled": True},
    
    "inter_helical": {"enabled": False},
    "pore_hydration": {"enabled": False},
    "water_bridges": {"enabled": False},
    "min_distance": {"enabled": False},
    
    "secondary_structure": {"helices": [], "strands": []},
    "plotting": {"rolling_average_ns": 10.0, "last_frames_ns": 500, "dpi": 300},
}
```

---

## Template 2: GPCR (7-Transmembrane Helices)

```python
CONFIG = {
    "protein_name": "GPCR_Name",
    "output_dir": "./gpcr_analysis",
    
    "systems": {
        "apo": {"label": "Inactive (Apo)", "topology": "./data/apo.gro", 
                "trajectory": "./data/apo.xtc", "color": "#FF6B6B"},
        "active": {"label": "Active (Agonist-Bound)", "topology": "./data/active.gro", 
                   "trajectory": "./data/active.xtc", "color": "#4169E1"},
    },
    
    "rmsd_rmsf": {"enabled": True, "atom_selection": "protein and name CA"},
    
    "inter_helical": {
        "enabled": True,
        "helix_pairs": [("H1", "H7"), ("H2", "H6"), ("H3", "H5")],
    },
    
    "sasa": {"enabled": True, "frame_stride": 10},
    
    "pore_hydration": {
        "enabled": True,
        "pore_residues": [70, 71, 72, 120, 121, 160, 161],  # Binding pocket
        "distance_cutoff": 5.0,
    },
    
    "hbond": {"enabled": True, "distance_cutoff": 3.5},
    
    "secondary_structure": {
        "helices": [
            (20, 45, 'H1'), (50, 75, 'H2'), (80, 105, 'H3'),
            (110, 135, 'H4'), (140, 165, 'H5'), (170, 195, 'H6'),
            (200, 225, 'H7'),
        ],
    },
}
```

---

## Template 3: Ion Channel (Pore Analysis)

```python
CONFIG = {
    "protein_name": "Ion_Channel",
    "output_dir": "./channel_analysis",
    
    "systems": {
        "closed": {"label": "Closed State", "topology": "./data/closed.gro", 
                   "trajectory": "./data/closed.xtc", "color": "#FF6B6B"},
        "open": {"label": "Open State", "topology": "./data/open.gro", 
                 "trajectory": "./data/open.xtc", "color": "#00A86B"},
    },
    
    "rmsd_rmsf": {"enabled": True},
    
    "inter_helical": {
        "enabled": True,
        "helix_pairs": [("H1", "H2"), ("H2", "H3"), ("H3", "H4")],
    },
    
    "pore_hydration": {
        "enabled": True,
        "pore_residues": [100, 101, 102, 103, 150, 151, 152, 153],
        "distance_cutoff": 4.5,
    },
    
    "water_bridges": {
        "enabled": True,
        "residue_pairs": [(100, 150), (102, 152)],
    },
    
    "hbond": {"enabled": True},
    
    "secondary_structure": {
        "helices": [(10, 35, 'H1'), (40, 65, 'H2'), (70, 95, 'H3'), (100, 125, 'H4')],
    },
}
```

---

## Template 4: Transporter (Multi-System Variant Analysis)

```python
CONFIG = {
    "protein_name": "Transporter_Name",
    "output_dir": "./transporter_analysis",
    
    "systems": {
        "wt_inward": {"label": "WT - Inward-Facing", "topology": "./data/wt_in.gro",
                      "trajectory": "./data/wt_in.xtc", "color": "#FF6B6B"},
        "wt_outward": {"label": "WT - Outward-Facing", "topology": "./data/wt_out.gro",
                       "trajectory": "./data/wt_out.xtc", "color": "#FF8C00"},
        "mut1_inward": {"label": "Mutant - Inward-Facing", "topology": "./data/mut_in.gro",
                        "trajectory": "./data/mut_in.xtc", "color": "#4169E1"},
    },
    
    "rmsd_rmsf": {"enabled": True},
    "inter_helical": {"enabled": True},
    
    "pore_hydration": {
        "enabled": True,
        "pore_residues": list(range(80, 100)) + list(range(140, 160)),
        "distance_cutoff": 5.0,
    },
    
    "min_distance": {
        "enabled": True,
        "residue_pairs": [(85, 145), (90, 150), (95, 155)],
    },
    
    "hbond": {"enabled": True},
    "sasa": {"enabled": True, "frame_stride": 20},
}
```

---

## Template 5: Aquaporin (Water Channel)

```python
CONFIG = {
    "protein_name": "Aquaporin",
    "output_dir": "./aqp_analysis",
    
    "systems": {
        "apo": {"label": "Apo", "topology": "./data/apo.gro", 
                "trajectory": "./data/apo.xtc", "color": "#FF6B6B"},
        "glycerol_bound": {"label": "Glycerol Bound", "topology": "./data/gly.gro", 
                           "trajectory": "./data/gly.xtc", "color": "#4169E1"},
    },
    
    "rmsd_rmsf": {"enabled": True},
    
    "pore_hydration": {
        "enabled": True,
        "pore_residues": [45, 46, 47, 120, 121, 122],  # NPA boxes
        "distance_cutoff": 4.0,
    },
    
    "water_bridges": {
        "enabled": True,
        "residue_pairs": [(45, 120), (46, 121), (47, 122)],
    },
    
    "hbond": {"enabled": True},
    "sasa": {"enabled": True},
}
```

---

## Tips for Configuration

### Finding Correct Residue Numbers

```python
# In Jupyter, before running analysis:
import MDAnalysis as mda
u = mda.Universe("./data/structure.gro")

# List all protein residues
for res in u.select_atoms("protein").residues:
    print(f"{res.resnum}: {res.name}")

# Find specific residue type
lys_residues = u.select_atoms("protein and resname LYS").residues
print(f"Lysine residues: {[r.resnum for r in lys_residues]}")
```

### Checking Atom Names

```python
# See what atom names are available
ca_atoms = u.select_atoms("protein and name CA")
print(f"Number of C-alpha atoms: {len(ca_atoms)}")

# Check for water molecules
waters = u.select_atoms("water")
print(f"Number of water atoms: {len(waters)}")
```

### Color Palette Ideas

| Color | Hex | Use For |
|-------|-----|---------|
| Red | #FF6B6B | APO/WT/Reference |
| Blue | #4169E1 | Bound/Mutant |
| Green | #00A86B | Alternative state |
| Orange | #FF8C00 | Secondary variant |
| Purple | #9400D3 | Tertiary variant |

### Helix Detection

```python
# Automatic helix detection from structure
import MDAnalysis
from MDAnalysis.analysis.helix_analysis import helix_analysis

u = mda.Universe("structure.gro")
ss = u.select_atoms("protein").residues.ss  # Secondary structure

# Print helices
for i, ss_type in enumerate(ss):
    if ss_type == 'H':
        print(f"Helix at residue {i}")
```

---

## Troubleshooting Configuration

### Error: "No atoms selected"

**Problem**: Selection string not matching atoms in structure

**Solution**:
```python
# Check what atoms exist
u = mda.Universe("structure.gro")
print(u.select_atoms("protein").atoms)
print(u.select_atoms("water").atoms)
```

### Error: "Residue not found"

**Problem**: Residue numbers don't match topology

**Solution**:
```python
# List all residue numbers
residues = u.select_atoms("protein").residues
res_nums = [r.resnum for r in residues]
print(f"Residue range: {min(res_nums)} to {max(res_nums)}")
```

### Pore residues not found

**Problem**: Binding site residues incorrectly specified

**Solution**:
```python
# Check specific residue
test_sel = u.select_atoms("resid 100")
print(f"Found {len(test_sel)} atoms for resid 100")
print(f"Residue name: {test_sel.residues[0].name if len(test_sel) > 0 else 'Not found'}")
```

---

## Running Multiple Analyses in Parallel

You can create multiple CONFIG dictionaries and run them in sequence:

```python
# In notebook cells:

# Configuration 1
CONFIG = {...}
rmsd1, rmsf1 = calculate_rmsd_rmsf(CONFIG)

# Configuration 2
CONFIG = {...}
rmsd2, rmsf2 = calculate_rmsd_rmsf(CONFIG)

# Compare results
df_rmsd = pd.concat([rmsd1, rmsd2])
# ... plot comparison
```

---

## Adapting for Your Protein

1. **Identify structure type**: GPCR, ion channel, transporter, etc.
2. **Find binding site residues**: Literature or PDB file
3. **Identify helices**: Secondary structure assignment
4. **Define key residue pairs**: Interactions to analyze
5. **Set appropriate thresholds**: Distance cutoffs, frame strides

---

**Last Updated**: February 2025
