
# ==========================================
# CONFIGURATION
# ==========================================

# ---------------------------------------------------------
# OPTION 1: RUNNING THE EXAMPLE (KDEL RECEPTOR)
# ---------------------------------------------------------
# To run the included example, uncomment the lines below:
# import sys
# sys.path.append('./examples/kdel_analysis')
# from kdel_config import CONFIG

# ---------------------------------------------------------
# OPTION 2: YOUR OWN DATA (EDIT BELOW)
# ---------------------------------------------------------
CONFIG = {
    "protein_name": "My Protein Analysis",
    "output_dir": "./results",
    
    # Define your systems here
    "systems": {
        # EXAMPLE SYSTEM (Comment out if using your own data)
        "example_kdel": {
            "label": "KDEL Receptor (Example)",
            "topology": "./examples/kdel_analysis/starter_data/kdel_receptor_structure.gro",
            "trajectory": "./examples/kdel_analysis/starter_data/kdel_receptor_10ns_simulation.xtc",
            "color": "#4169E1"
        },
        
        # YOUR SYSTEM (Uncomment and fill in)
        # "my_system": {
        #     "label": "My BioEMU Ensemble",
        #     "topology": "./data/my_protein/structure.pdb",
        #     "trajectory": "./data/my_protein/samples.xtc",
        #     "color": "red"
        # }
    },
    
    # Analysis Settings
    "rmsd_rmsf": {"enabled": True, "atom_selection": "protein and name CA", "reference_frame": 0},
    "inter_helical": {"enabled": False}, # Enable if you have helices
    "sasa": {"enabled": False},
    "hbond": {"enabled": False},
}