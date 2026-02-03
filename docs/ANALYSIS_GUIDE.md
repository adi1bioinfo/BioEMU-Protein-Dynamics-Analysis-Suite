# Complete Analysis Guide - BioEMU Analysis Suite

Comprehensive documentation of all 7 analyses available in this suite.

## Table of Contents

1. [RMSD & RMSF](#1-rmsd--rmsf)
2. [Inter-Helical Distance & Angle](#2-inter-helical-distance--angle)
3. [Pore Hydration](#3-pore-hydration)
4. [SASA (Solvent Accessible Surface Area)](#4-sasa-solvent-accessible-surface-area)
5. [Water Bridges](#5-water-bridges-direct--mediated)
6. [Minimum Distance](#6-minimum-distance-analysis)
7. [Hydrogen Bonds](#7-hydrogen-bond-analysis)

---

## 1. RMSD & RMSF

### What It Measures

**RMSD (Root Mean Square Deviation)**: Overall deviation of protein structure from a reference frame over time.
- **Units**: Ångströms (Å)
- **Interpretation**: Lower RMSD = more stable structure; higher = more flexible

**RMSF (Root Mean Square Fluctuation)**: Per-residue flexibility, showing which regions are more mobile.
- **Units**: Ångströms (Å)
- **Interpretation**: High RMSF = flexible loop/tail; Low RMSF = rigid core domain

### Biological Significance

- **RMSD plateau** indicates trajectory equilibration (protein has reached stable conformation)
- **Slow RMSD drift** suggests conformational transitions or insufficient equilibration
- **RMSF peaks** identify functionally important flexible regions (binding sites, gates, hinges)
- **RMSF secondary structure** shows helices are more rigid than loops

### Configuration

```python
"rmsd_rmsf": {
    "enabled": True,
    "atom_selection": "protein and backbone",  # or "protein and name CA"
    "reference_frame": 0,  # Use first frame as reference
}
```

### Example Interpretation

```
RMSD: Grows from 1.5 Å to 3.5 Å in first 100 ns, then plateaus
→ System equilibrated by 100 ns

RMSF: High peaks at residues 40-50, 120-135
→ These loops are flexible - likely important for function
```

### Output Files

- `rmsd_all.csv` - Time series of RMSD for all systems
- `rmsf_all.csv` - Per-residue RMSF values
- `rmsd_plot.png` - Comparative RMSD plot
- `rmsf_plot.png` - Comparative RMSF per residue

### When to Use

✅ **Always** - fundamental stability analysis
✅ For confirming equilibration
✅ Identifying flexible regions

---

## 2. Inter-Helical Distance & Angle

### What It Measures

Tracks the **distance and orientation** between transmembrane helices in helical proteins (GPCRs, ion channels, aquaporins).

- **Distance**: Center-of-mass distance between helix pairs (Å)
- **Angle**: Orientation/rotation angle between helices (degrees)

### Biological Significance

- **Helix opening/closing** during gating mechanism activation
- **Domain motion** - large movements indicate conformational changes
- **Functional transitions** - APO → BOUND state may show distinct helix repositioning
- **Mutation effects** - variants may show altered domain dynamics

### Configuration

```python
"inter_helical": {
    "enabled": True,
    "helix_pairs": [("H1", "H7"), ("H3", "H5")],  # Pair names
    # OR leave empty and use secondary_structure
}

"secondary_structure": {
    "helices": [
        (3, 26, 'H1'),      # (start_residue, end_residue, name)
        (34, 52, 'H2'),
        (58, 81, 'H3'),
        # ... etc
    ],
}
```

### Example Interpretation

```
H1-H7 distance: 15 Å (apo) → 18 Å (bound)
→ Helices move farther apart upon ligand binding

H3-H5 angle: Rotates -25° during 500 ns
→ Significant conformational change/gating
```

### Output Files

- `inter_helical/{pair}_distance.png` - Distance time series
- `inter_helical/{pair}_angle.png` - Orientation dynamics

### When to Use

✅ For GPCR/ion channel/transporter analysis
✅ Studying gating mechanisms
✅ Comparing conformational changes
❌ Not useful for globular proteins without clear helices

---

## 3. Pore Hydration

### What It Measures

**Water occupancy** in a functional cavity (binding pocket, ion channel pore, aquaporin channel).

- **Count**: Number of water molecules within cutoff distance (Å)
- **Occupancy**: Percentage of frames with water present
- **Residence time**: How long waters stay in the pore

### Biological Significance

- **Ion selectivity**: Water coordination affects which ions pass through
- **Gating**: Changes in hydration may precede/enable gating transitions
- **Binding affinity**: Water bridges in binding pocket stabilize ligands
- **Substrate translocation**: Required for transporters to function

### Configuration

```python
"pore_hydration": {
    "enabled": True,
    "pore_residues": [50, 51, 52, 100, 101],  # Residues defining pore
    "water_selection": "water",
    "distance_cutoff": 5.0,  # Angstroms from pore center
}
```

### Example Interpretation

```
APO:   avg 3.2 ± 1.5 waters
BOUND: avg 2.1 ± 1.2 waters

→ Ligand binding displaces water from pore
→ Suggests direct binding interactions
```

### Output Files

- `pore_hydration/{system}_pore_hydration.csv` - Water count time series
- `pore_hydration/pore_hydration.png` - Comparative plot

### When to Use

✅ Ion channels/transporters
✅ Binding pocket analysis
✅ Water-mediated interactions
❌ Soluble proteins (not applicable)

---

## 4. SASA (Solvent Accessible Surface Area)

### What It Measures

Surface area of each residue exposed to solvent (water).

- **Per-residue SASA**: How much of each residue is exposed
- **Total SASA**: Overall protein hydration surface area
- **Buried vs. Exposed**: Identifies core vs. surface residues

**Algorithm**: Shrake-Rupley algorithm (1973)
- Rolls probe sphere (1.4 Å radius = water) around protein
- Calculates contact surface area

### Biological Significance

- **Hydrophobic core**: Buried hydrophobic residues (low SASA)
- **Hydrophilic surface**: Surface-exposed charged residues (high SASA)
- **Binding site identification**: Binding sites often have characteristic SASA patterns
- **Dehydration upon binding**: Ligand binding often reduces SASA as water is displaced
- **Protein-protein interfaces**: Hidden surfaces indicate interaction sites

### Configuration

```python
"sasa": {
    "enabled": True,
    "frame_stride": 10,  # Process every 10th frame (faster)
}
```

### Output Files

- `sasa/{system}_sasa.csv` - Per-residue SASA time series
- Per-residue columns named `{ResName}_{ResNumber}`

### Example Analysis

```python
# In a new notebook cell:
import pandas as pd

# Load SASA data
df_sasa = pd.read_csv("./sasa/apo_sasa.csv")

# Find most exposed residues
df_sasa_mean = df_sasa.iloc[:, 1:-1].mean()
top_exposed = df_sasa_mean.nlargest(10)
print("Most exposed residues:")
print(top_exposed)

# Plot per-residue SASA
residue_nums = [int(col.split('_')[1]) for col in df_sasa.columns[1:-1]]
avg_sasa = df_sasa.iloc[:, 1:-1].mean()
plt.plot(residue_nums, avg_sasa)
plt.xlabel("Residue Number")
plt.ylabel("Average SASA (Ų)")
plt.show()
```

### When to Use

✅ Always - understand protein hydration
✅ Identify binding sites
✅ Study surface properties
✅ Protein-protein interaction sites

---

## 5. Water Bridges (Direct & Mediated)

### What It Measures

**Direct hydrogen bonds**: Between two protein residues
**Water-mediated bridges**: Two residues connected through one or more water molecules

### Types of Bridges

```
Direct Bridge:
  Residue A ←→ Residue B (H-bond)
  Occupancy: 80%

Water-Mediated Bridge:
  Residue A ←→ Water ←→ Residue B
  Occupancy: 60%
```

### Biological Significance

- **Stabilizing interactions**: Persistent bridges stabilize conformations
- **Functional dynamics**: Water bridges can form/break during conformational changes
- **Binding mechanisms**: Often mediate ligand-protein interactions
- **Specificity**: Water-mediated interactions provide specificity without requiring precise fit

### Configuration

```python
"water_bridges": {
    "enabled": True,
    "residue_pairs": [
        (10, 50),  # Residue 10 ↔ Residue 50
        (20, 100),
    ],
    "hbond_distance_cutoff": 3.5,  # Angstroms
    "occupancy_threshold": 0.01,   # 1% min occupancy
}
```

### Output Format

```
CSV Example:
Residue_Pair,Direct_Occupancy,Mediated_Occupancy,Total_Occupancy
10-50,0.65,0.15,0.80
20-100,0.45,0.30,0.75
```

### Interpretation

```
Bridge 10-50:
  Direct:   65% (strong, persistent H-bond)
  Mediated: 15% (occasional water involvement)
  
→ Primarily direct interaction, sometimes water-assisted
```

### Output Files

- `water_bridges/{system}_water_bridges_summary.csv` - Occupancy table

### When to Use

✅ Binding site analysis
✅ Stability mechanism identification
✅ Comparing apo vs. bound states
✅ Mutation impact assessment

---

## 6. Minimum Distance Analysis

### What It Measures

**Closest approach** between two selected residues/functional groups over time.

- **Minimum distance**: Smallest atom-to-atom distance each frame
- **Average distance**: Mean distance over trajectory
- **Contact frequency**: How often residues are within contact distance

### Biological Significance

- **Interaction network**: Identifies which residues interact
- **Contact dynamics**: Shows if residues approach/separate during simulation
- **Binding geometry**: Characterizes how residues are positioned relative to each other
- **Functional interactions**: Key residue pairs may have minimal distances during function

### Configuration

```python
"min_distance": {
    "enabled": True,
    "residue_pairs": [
        (10, 50),
        (20, 100),
    ],
    "selection1": "protein and name CA",  # C-alpha atoms
    "selection2": "protein and name CA",  # Or use specific atom names
}
```

### Advanced Selections

```python
# Aromatic rings only
"selection1": "protein and resid 50 and name CZ"

# Backbone atoms
"selection1": "protein and resid 10 and (name CA or name C or name N)"

# Side chain atoms
"selection1": "protein and resid 50 and not backbone"
```

### Output Files

- `min_distance/{pair}_distance.png` - Distance time series plot

### Example Interpretation

```
Residues 10-50:
  Range: 2.5 - 8.0 Å
  Mean:  5.2 ± 1.5 Å
  
→ Residues approach (2.5 Å) periodically
→ Likely interact through networks of residues
```

### When to Use

✅ Interaction mapping
✅ Specific residue pair analysis
✅ Mutation impact prediction
✅ Binding mechanism studies

---

## 7. Hydrogen Bond Analysis

### What It Measures

**Persistent hydrogen bonds** between protein residues and other molecules.

- **Occupancy**: Percentage of frames H-bond exists
- **Persistence**: How stable is the H-bond
- **Network**: Which residues form H-bonds with which

### H-Bond Criteria

Standard definition:
- **Distance**: Donor-Acceptor ≤ 3.5 Å (N-O or O-O)
- **Angle**: D-H-A angle ≥ 120° (or optional)

### Biological Significance

- **Secondary structure**: α-helices and β-sheets stabilized by backbone H-bonds
- **Tertiary structure**: Side-chain H-bonds stabilize core
- **Binding**: Ligand-protein H-bonds are key interaction
- **Salt bridges**: Special H-bonds between charged residues
- **Stability**: More H-bonds = more stable

### Configuration

```python
"hbond": {
    "enabled": True,
    "distance_cutoff": 3.5,      # Angstroms
    "angle_cutoff": 120.0,       # Degrees (optional)
    "residue_pairs": [
        (10, 50),    # Specific pair tracking
        (20, 100),
    ],
    # OR leave residue_pairs empty for all H-bonds
}
```

### Output Format

```
CSV Example:
Residue_Pair,Occupancy
10-50,0.75
20-100,0.45
35-65,0.92
```

### Interpretation

```
H-bond 10-50: 75% occupancy
→ Persistent interaction (exists 3/4 of the time)
→ Likely important for stability

H-bond 35-65: 92% occupancy
→ Very stable (almost always present)
→ Core structural interaction
```

### Output Files

- `hydrogen_bonds/{system}_hbonds.csv` - H-bond occupancy table

### How to Extend

```python
# In a new cell, create H-bond network visualization:
import networkx as nx
import matplotlib.pyplot as plt

# Load H-bond data
df_hbonds = pd.read_csv("./hydrogen_bonds/apo_hbonds.csv")

# Create network
G = nx.Graph()
for _, row in df_hbonds[df_hbonds['Occupancy'] > 0.3].iterrows():
    res1, res2 = map(int, row['Residue_Pair'].split('-'))
    G.add_edge(res1, res2, weight=row['Occupancy'])

# Plot
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, k=2)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=300)
nx.draw_networkx_edges(G, pos, width=[G[u][v]['weight']*3 for u, v in G.edges()])
nx.draw_networkx_labels(G, pos)
plt.title("H-bond Network")
plt.show()
```

### When to Use

✅ Always - structural stability analysis
✅ Binding site characterization
✅ Mutation prediction
✅ Drug design validation

---

## Advanced Usage & Troubleshooting

### Memory Issues with Large Trajectories

```python
# In SASA analysis, reduce frame_stride
"sasa": {
    "enabled": True,
    "frame_stride": 50,  # Skip more frames (faster, less memory)
}
```

### Custom Atom Selections

```python
# In min_distance:
"min_distance": {
    "enabled": True,
    "residue_pairs": [(10, 50)],
    "selection1": "protein and resid 10 and (name OE1 or name OE2)",  # GLU
    "selection2": "protein and resid 50 and (name NH1 or name NH2)",  # ARG
}
```

### Comparing Binding Sites Across Variants

```python
# In configuration, define same residue pairs for all systems
# This allows direct comparison of H-bonds, distances, etc.
"hbond": {
    "residue_pairs": [
        (50, 100),  # Same pair for all systems
        (51, 101),
    ],
}
```

### Extracting Statistics

```python
# After analysis, in new cell:
import pandas as pd
import numpy as np

# Load RMSD data
df_rmsd = pd.read_csv("./rmsd_rmsf/rmsd_all.csv")

# Group by system
for system in df_rmsd['System'].unique():
    df_sys = df_rmsd[df_rmsd['System'] == system]
    
    # Last 500 ns statistics
    df_last = df_sys[df_sys['Time_ns'] >= df_sys['Time_ns'].max() - 500]
    
    print(f"{system}:")
    print(f"  Mean RMSD:     {df_last['RMSD_A'].mean():.2f} ± {df_last['RMSD_A'].std():.2f} Å")
    print(f"  Min/Max:       {df_last['RMSD_A'].min():.2f} / {df_last['RMSD_A'].max():.2f} Å")
```

---

## Recommended Reading

- **RMSD/RMSF**: Müller et al. (2004) - MD analysis tutorial
- **SASA**: Shrake & Rupley (1973) - Original algorithm
- **H-bonds**: Baker & Hubbard (1984) - H-bond geometry standards
- **Water bridges**: Loewenstein et al. (1999) - Protein-water interactions

---

## Contributing New Analyses

Want to add a new analysis? See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines!

---

**Last Updated**: February 2025
