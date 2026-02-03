# Example Configuration - KDEL Receptor Analysis
# Save as: examples/kdel_comparison/kdel_config.py
# Usage: Copy to your project and modify file paths

CONFIG = {
    # ========== PROJECT DETAILS ==========
    "protein_name": "KDEL Receptor (KDELR)",
    "project_name": "kdel_apo_vs_bound",
    
    "output_dir": "./kdel_analysis_results",
    
    # ========== SYSTEMS TO ANALYZE ==========
    # Define your BioEMU or GROMACS simulation outputs here
    "systems": {
        "apo": {
            "label": "APO (unbound)",
            "topology": "./data/kdel_apo/structure.gro",
            "trajectory": "./data/kdel_apo/trajectory.xtc",
            "color": "#FF6B6B",  # Red
        },
        "kdel_bound": {
            "label": "KDEL Peptide Bound",
            "topology": "./data/kdel_kdel/structure.gro",
            "trajectory": "./data/kdel_kdel/trajectory.xtc",
            "color": "#4169E1",  # Blue
        },
        "kkee_bound": {
            "label": "KKEE Variant Bound",
            "topology": "./data/kdel_kkee/structure.gro",
            "trajectory": "./data/kdel_kkee/trajectory.xtc",
            "color": "#00A86B",  # Green
        },
    },
    
    # ========== ANALYSIS CONFIGURATION ==========
    
    # 1. RMSD/RMSF - Overall protein stability and per-residue flexibility
    "rmsd_rmsf": {
        "enabled": True,
        "atom_selection": "protein and backbone",  # C-alpha atoms
        "reference_frame": 0,  # Use first frame as reference
    },
    
    # 2. Inter-helical Distance & Angle - Domain dynamics
    # KDELR has 7 transmembrane helices
    "inter_helical": {
        "enabled": True,
        "helix_pairs": [("H1", "H7"), ("H2", "H6"), ("H3", "H5")],  # Key pairs to analyze
    },
    
    # 3. Pore Hydration - Water occupancy in ligand-binding pocket
    "pore_hydration": {
        "enabled": True,
        "pore_residues": [50, 51, 52, 100, 101, 102, 150],  # Binding pocket residues
        "water_selection": "water",
        "distance_cutoff": 5.0,  # Angstroms
    },
    
    # 4. SASA - Solvent accessible surface area (hydration)
    "sasa": {
        "enabled": True,
        "frame_stride": 10,  # Process every 10th frame for speed
    },
    
    # 5. Water Bridges - Direct and water-mediated interactions
    "water_bridges": {
        "enabled": True,
        "residue_pairs": [
            (50, 100),  # Key residue pairs in binding site\n            (51, 101),\n            (52, 102),\n        ],\n        "hbond_distance_cutoff": 3.5,  # Angstroms\n        "occupancy_threshold": 0.01,  # 1% threshold\n    },\n    \n    # 6. Minimum Distance - Closest approach between residues\n    "min_distance": {\n        "enabled": True,\n        "residue_pairs": [\n            (50, 100),\n            (51, 101),\n        ],\n        "selection1": \"protein and name CA\",  # C-alpha atoms\n        "selection2": \"protein and name CA\",\n    },\n    \n    # 7. Hydrogen Bonds - Persistent H-bonds in binding region\n    "hbond": {\n        "enabled": True,\n        "distance_cutoff": 3.5,  # Angstroms\n        "angle_cutoff": 120.0,  # Degrees\n        "residue_pairs\": [\n            (50, 100),  # Specific H-bonds to track\n            (51, 101),\n        ],\n    },\n    \n    # ========== SECONDARY STRUCTURE ==========\n    # Define helices for annotations on plots\n    \"secondary_structure\": {\n        \"helices\": [\n            (3, 26, 'H1'),      # Transmembrane helix 1\n            (34, 52, 'H2'),     # Transmembrane helix 2\n            (58, 81, 'H3'),     # etc.\n            (95, 108, 'H4'),\n            (115, 141, 'H5'),\n            (146, 174, 'H6'),\n            (178, 204, 'H7'),   # Transmembrane helix 7\n        ],\n        \"strands\": [],  # No beta sheets in GPCR\n    },\n    \n    # ========== VISUALIZATION ==========\n    \"plotting\": {\n        \"rolling_average_ns\": 10.0,   # 10 ns rolling average for smoothing\n        \"last_frames_ns\": 500,        # Use last 500 ns for statistics\n        \"dpi\": 300,                   # High resolution for publications\n        \"figure_style\": \"seaborn-v0_8-whitegrid\",\n    },\n}\n\n# ============================================================================\n# USAGE INSTRUCTIONS\n# ============================================================================\n# \n# 1. Edit file paths above to match your simulation output locations\n# \n# 2. In your Jupyter notebook, replace the CONFIG dictionary with:\n#    from kdel_config import CONFIG\n# \n# 3. Or copy-paste this CONFIG directly into the notebook's configuration cell\n# \n# 4. Adjust residue numbers and selections based on your protein!\n# \n# ============================================================================\n