# Quick Reference: Configuration Examples

## Minimal Configuration (3 systems)

```python
CONFIG = {
    "protein_name": "MyProtein",
    "output_dir": "./results",
    
    "systems": {
        "sys1": {
            "label": "Condition 1",
            "topology": "./data/sys1/em.gro",
            "trajectory": "./data/sys1/prod.xtc",
            "color": "#FF6B6B",
        },
        "sys2": {
            "label": "Condition 2",
            "topology": "./data/sys2/em.gro",
            "trajectory": "./data/sys2/prod.xtc",
            "color": "#4169E1",
        },
        "sys3": {
            "label": "Condition 3",
            "topology": "./data/sys3/em.gro",
            "trajectory": "./data/sys3/prod.xtc",
            "color": "#2ECC71",
        },
    },
}
```

## GPCR (7 Transmembrane Helices)

```python
CONFIG = {
    "protein_name": "β2-Adrenergic Receptor (β2AR)",
    "systems": {
        "apo": {...},
        "agonist": {...},
        "antagonist": {...},
    },
    
    "secondary_structure": {
        "helices": [
            (25, 55, 'TM1'),
            (64, 97, 'TM2'),
            (105, 140, 'TM3'),
            (157, 187, 'TM4'),
            (199, 229, 'TM5'),
            (243, 273, 'TM6'),
            (285, 310, 'TM7'),
        ],
    },
    
    "rmsd_rmsf": {
        "enabled": True,
        "atom_selection": "protein and backbone",
    },
}
```

## Ion Channel (Open/Closed States)

```python
CONFIG = {
    "protein_name": "KcsA Potassium Channel",
    "systems": {
        "open": {
            "label": "Open (conducting)",
            "topology": "./data/open/em.gro",
            "trajectory": "./data/open/prod.xtc",
            "color": "#27AE60",
        },
        "closed": {
            "label": "Closed (non-conducting)",
            "topology": "./data/closed/em.gro",
            "trajectory": "./data/closed/prod.xtc",
            "color": "#E74C3C",
        },
    },
    
    "distance_analysis": {
        "enabled": True,
        "residue_pairs": [
            (45, 120),   # Gate residue pairs (adjust for your protein)
            (50, 125),
        ],
    },
}
```

## Aquaporin (Water Channel)

```python
CONFIG = {
    "protein_name": "Aquaporin-1",
    "systems": {
        "water_filled": {...},
        "empty": {...},
    },
    
    "sasa": {
        "enabled": True,
        "frame_stride": 5,  # Higher frequency
    },
    
    "hbond": {
        "enabled": True,
        "distance_cutoff": 3.0,  # Stricter for water interactions
    },
}
```

## Protein with Bound Ligand

```python
CONFIG = {
    "protein_name": "Enzyme-Substrate Complex",
    "systems": {
        "apo": {
            "label": "Apo (no substrate)",
            "topology": "./data/apo/em.gro",
            "trajectory": "./data/apo/md.xtc",
            "color": "#95A5A6",
        },
        "substrate": {
            "label": "With Substrate",
            "topology": "./data/with_substrate/em.gro",
            "trajectory": "./data/with_substrate/md.xtc",
            "color": "#3498DB",
        },
        "inhibitor": {
            "label": "With Inhibitor",
            "topology": "./data/with_inhibitor/em.gro",
            "trajectory": "./data/with_inhibitor/md.xtc",
            "color": "#E74C3C",
        },
    },
    
    "distance_analysis": {
        "enabled": True,
        "residue_pairs": [
            (40, 95),   # Active site residues
            (50, 100),
        ],
    },
}
```

## Wild-Type vs Mutant Comparison

```python
CONFIG = {
    "protein_name": "Protein X",
    "systems": {
        "wt_apo": {
            "label": "WT Apo",
            "topology": "./wt_apo/em.gro",
            "trajectory": "./wt_apo/prod.xtc",
            "color": "#3498DB",
        },
        "wt_bound": {
            "label": "WT Bound",
            "topology": "./wt_bound/em.gro",
            "trajectory": "./wt_bound/prod.xtc",
            "color": "#2980B9",
        },
        "mut_apo": {
            "label": "Mutant Apo",
            "topology": "./mut_apo/em.gro",
            "trajectory": "./mut_apo/prod.xtc",
            "color": "#E74C3C",
        },
        "mut_bound": {
            "label": "Mutant Bound",
            "topology": "./mut_bound/em.gro",
            "trajectory": "./mut_bound/prod.xtc",
            "color": "#C0392B",
        },
    },
}
```

## Custom Residue Analysis

```python
CONFIG = {
    # ... other config ...
    
    "sasa": {
        "enabled": True,
        "residue_groups": {
            "binding_site": [("TYR", "PHE", "TRP")],
            "catalytic": [("HIS", "ASP", "GLU", "SER")],
            "interface": [("VAL", "ILE", "LEU")],
        },
    },
}
```

## Long Trajectory (Speed Optimization)

```python
CONFIG = {
    # ... other config ...
    
    "rmsd_rmsf": {
        "enabled": True,
        "atom_selection": "protein and backbone",  # Less atoms = faster
        "reference_frame": 500,  # Skip initial non-equilibrated frames
    },
    
    "sasa": {
        "enabled": True,
        "frame_stride": 50,  # Process every 50th frame (~95% faster)
    },
    
    "hbond": {
        "enabled": False,  # Skip if time-limited
    },
    
    "plotting": {
        "rolling_average_window_ns": 25.0,  # Wider window = less noise
    },
}
```

## All Features Enabled

```python
CONFIG = {
    "protein_name": "Complete Analysis Example",
    "output_dir": "./comprehensive_results",
    
    "systems": {
        "sample1": {...},
        "sample2": {...},
    },
    
    "rmsd_rmsf": {
        "enabled": True,
        "atom_selection": "protein",
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
    
    "secondary_structure": {
        "helices": [(10, 30, 'H1'), (50, 70, 'H2')],
        "strands": [(35, 45, 'S1')],
    },
    
    "plotting": {
        "rolling_average_window_ns": 10.0,
        "last_frames_statistics": 500,
        "dpi": 300,
    },
}
```

---

## MDAnalysis Selection Language Cheat Sheet

```python
# Atom selections
"protein"                    # All protein atoms
"backbone"                   # C, CA, N, O atoms
"sidechains"                 # Side chain atoms
"ca" or "name CA"            # C-alpha atoms only

# Residue types
"resname ALA GLY SER"        # Specific residues
"protein and (ARG or LYS)"   # Charged residues
"protein and not hydrogen"   # Heavy atoms

# Residue ranges
"resid 1:50"                 # Residues 1-50
"resid 10 20 30"             # Specific residues
"resi 1:100:5"               # Every 5th residue from 1-100

# Atom properties
"name CA"                    # Specific atom names
"type C"                     # Atom types
"charge > 0"                 # Charged atoms

# Combinations
"protein and backbone"       # AND operator
"protein or ligand"          # OR operator
"protein and not (GLY)"      # NOT operator
"(resname GLU) and backbone" # Parentheses for clarity
```

---

## Color Palette Suggestions

### Distinct Colors
- Red: `#E74C3C` or `#FF6B6B`
- Blue: `#3498DB` or `#4169E1`
- Green: `#27AE60` or `#2ECC71`
- Orange: `#F39C12` or `#FF8C00`
- Purple: `#8E44AD` or `#9B59B6`
- Teal: `#16A085` or `#1ABC9C`

### For Multiple Conditions
```python
colors = [
    "#E74C3C",  # Red
    "#3498DB",  # Blue
    "#27AE60",  # Green
    "#F39C12",  # Orange
    "#8E44AD",  # Purple
    "#16A085",  # Teal
]
```

### Colorblind-Friendly
```python
colors = [
    "#1B9E77",  # Dark green
    "#D95F02",  # Orange
    "#7570B3",  # Purple
    "#E7298A",  # Pink
]
```

---

## Performance Benchmarks

| Analysis | 1000 frames | 10000 frames | 100000 frames |
|----------|-----------|-------------|--------------|
| RMSD/RMSF | <1 min | 1-2 min | 5-10 min |
| SASA (stride=10) | 1-2 min | 5-10 min | 20-50 min |
| H-bonds | <1 min | 2-5 min | 10-20 min |
| Total | 2-5 min | 10-20 min | 40-100 min |

**To speed up**: Increase `frame_stride` in SASA analysis
