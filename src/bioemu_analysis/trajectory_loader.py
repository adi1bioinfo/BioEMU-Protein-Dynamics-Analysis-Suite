"""Trajectory loading and file handling utilities."""

import os


def load_trajectory(topology_file, trajectory_file):
    """Load a molecular dynamics trajectory using MDAnalysis.

    Raises ImportError if MDAnalysis is not installed.
    """
    try:
        import MDAnalysis as mda
    except Exception as e:
        raise ImportError("MDAnalysis not installed. Install with: conda install -c conda-forge mdanalysis")

    if not os.path.exists(topology_file):
        raise FileNotFoundError(f"Topology file not found: {topology_file}")
    if not os.path.exists(trajectory_file):
        raise FileNotFoundError(f"Trajectory file not found: {trajectory_file}")

    u = mda.Universe(topology_file, trajectory_file)
    return u


def validate_files(config):
    """Validate that all trajectory files in config exist."""
    missing = []
    for sys_key, sys_info in config.get("systems", {}).items():
        topo = sys_info.get("topology")
        traj = sys_info.get("trajectory")
        if topo and not os.path.exists(topo):
            missing.append(f"{sys_key} topology: {topo}")
        if traj and not os.path.exists(traj):
            missing.append(f"{sys_key} trajectory: {traj}")
    if missing:
        return False, missing
    return True, []


def get_trajectory_info(topology_file, trajectory_file):
    """Return a small info dict about the trajectory (uses MDAnalysis)."""
    u = load_trajectory(topology_file, trajectory_file)
    try:
        n_atoms = u.atoms.n_atoms
        n_frames = len(u.trajectory)
    except Exception:
        n_atoms = None
        n_frames = None
    info = {
        "n_atoms": n_atoms,
        "n_frames": n_frames,
        "topology_file": topology_file,
        "trajectory_file": trajectory_file,
    }
    return info
