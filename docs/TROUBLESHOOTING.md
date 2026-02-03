# Troubleshooting Guide

Solutions to common issues when using BioEMU Analysis Suite.

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [File & Data Issues](#file--data-issues)
3. [Analysis Errors](#analysis-errors)
4. [Performance Issues](#performance-issues)
5. [Visualization Problems](#visualization-problems)
6. [Getting Help](#getting-help)

---

## Installation Issues

### Issue: "ModuleNotFoundError: No module named 'mdtraj'"

**Error Message:**
```
ModuleNotFoundError: No module named 'mdtraj'
```

**Cause:** MDTraj not installed

**Solution:**
```bash
# Option 1: Using conda (recommended)
conda install -c conda-forge mdtraj

# Option 2: Using pip
pip install mdtraj
```

---

### Issue: "ModuleNotFoundError: No module named 'MDAnalysis'"

**Error Message:**
```
ModuleNotFoundError: No module named 'MDAnalysis'
```

**Cause:** MDAnalysis not installed

**Solution:**
```bash
# Using conda (recommended for MDAnalysis)
conda install -c conda-forge mdanalysis

# Or pip
pip install MDAnalysis
```

---

### Issue: "pip: command not found"

**Cause:** pip not installed or Python not in PATH

**Solution (Linux/macOS):**
```bash
python3 -m pip install -r requirements.txt
```

**Solution (Windows):**
```bash
python -m pip install -r requirements.txt
```

---

### Issue: Virtual environment not activating

**Cause:** Incorrect activation command

**Solution (macOS/Linux):**
```bash
# Check if venv exists
ls -la bioemu-env/

# Activate (bash/zsh)
source bioemu-env/bin/activate

# You should see (bioemu-env) in prompt
```

**Solution (Windows):**
```bash
# Activate (PowerShell)
.\bioemu-env\Scripts\Activate.ps1

# If error, enable script execution:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Issue: "Could not find a version that satisfies the requirement"

**Cause:** Package version conflict or incorrect version specification

**Solution:**
```bash
# Update pip first
pip install --upgrade pip

# Then install with less strict versioning
pip install mdanalysis mdtraj pandas numpy matplotlib seaborn

# Or install from conda-forge (better for scientific packages)
conda install -c conda-forge mdanalysis mdtraj
```

---

## File & Data Issues

### Issue: "FileNotFoundError: No such file or directory"

**Error Message:**
```
FileNotFoundError: [Errno 2] No such file or directory: './data/system1/structure.gro'
```

**Cause:** Topology or trajectory file path incorrect

**Solution:**
1. Check file exists:
```bash
ls -la ./data/system1/structure.gro
ls -la ./data/system1/trajectory.xtc
```

2. Use absolute paths in CONFIG:
```python
CONFIG = {
    "systems": {
        "system_1": {
            "topology": "/full/path/to/structure.gro",  # Absolute path
            "trajectory": "/full/path/to/trajectory.xtc",
        }
    }
}
```

3. Or ensure you're in correct directory:
```bash
pwd  # Check current directory
cd /home/aditi/Desktop/python/BioEMU-Protein-Dynamics
```

---

### Issue: "No atoms selected with..."

**Error Message:**
```
⚠️ No atoms selected with 'protein and name CA'
```

**Cause:** Selection string doesn't match atoms in structure

**Solution:**
```python
# Check what atoms exist in your structure
import MDAnalysis as mda
u = mda.Universe("./data/structure.gro")

# List available atom names
print(u.select_atoms("protein").names)

# List available residue names
print([r.name for r in u.select_atoms("protein").residues])

# Try simpler selection
u.select_atoms("protein")  # All protein atoms
u.select_atoms("backbone")  # Only backbone
u.select_atoms("name CA")  # Only C-alpha
```

---

### Issue: "Residue not found"

**Error Message:**
```
⚠️ No pore residues found
```

**Cause:** Residue numbers in CONFIG don't match structure

**Solution:**
```python
# Find residue number range
import MDAnalysis as mda
u = mda.Universe("./data/structure.gro")
protein = u.select_atoms("protein")
residues = protein.residues
print(f"Residue range: {residues[0].resnum} to {residues[-1].resnum}")

# List all residues
for res in residues:
    print(f"{res.resnum}: {res.name}")
```

Then update CONFIG with correct residue numbers.

---

### Issue: "Trajectory too large / Out of memory"

**Cause:** Processing entire trajectory at once

**Solution 1:** Use frame stride
```python
CONFIG = {
    "sasa": {
        "enabled": True,
        "frame_stride": 50,  # Process every 50th frame instead of 10
    }
}
```

**Solution 2:** Use chunk processing (in notebook cell)
```python
# Process in chunks instead of all at once
chunk_size = 1000
for i, chunk in enumerate(md.iterload(traj_file, top=top_file, chunk=chunk_size)):
    # Process chunk
    sasa = md.shrake_rupley(chunk, mode='residue')
    # Save intermediate results
    print(f"Chunk {i} processed")
```

---

## Analysis Errors

### Issue: "KeyError: 'System'"

**Error Message:**
```
KeyError: 'System'
```

**Cause:** DataFrame doesn't have 'System' column

**Solution:** Ensure CONFIG has systems defined:
```python
CONFIG = {
    "systems": {
        "system_1": {
            "label": "My System",
            "topology": "...",
            "trajectory": "...",
        }
    }
}
```

---

### Issue: "ValueError: could not convert string to float"

**Cause:** Trying to plot non-numeric data

**Solution:** Check data types:
```python
# Load CSV and check types
df = pd.read_csv("./results/rmsd_rmsf/rmsd_all.csv")
print(df.dtypes)

# Ensure numeric columns
df['RMSD_A'] = pd.to_numeric(df['RMSD_A'], errors='coerce')
df = df.dropna()
```

---

### Issue: "Empty residue selection"

**Cause:** Wrong residue numbers for helices

**Solution:**
```python
# Verify helix residue ranges
import MDAnalysis as mda
u = mda.Universe("structure.gro")

# Test helix selection
h1_atoms = u.select_atoms("resid 3:26")  # H1
print(f"H1 atoms: {len(h1_atoms)}")

if len(h1_atoms) == 0:
    # Residue numbering might be different
    # Try finding actual helix boundaries:
    protein = u.select_atoms("protein")
    for i, res in enumerate(protein.residues[:50]):
        print(f"Index {i}: Residue {res.resnum} {res.name}")
```

---

## Performance Issues

### Issue: "Analysis taking too long"

**Causes:** Large trajectories, small frame stride, slow I/O

**Solutions:**

1. **Increase frame stride** (process fewer frames):
```python
CONFIG = {
    "sasa": {"frame_stride": 50},  # Process every 50th frame
    "water_bridges": {"enabled": True},  # Calculate less frequently
}
```

2. **Disable unnecessary analyses:**
```python
CONFIG = {
    "rmsd_rmsf": {"enabled": True},   # Keep this (fast)
    "sasa": {"enabled": False},       # Disable (slow)
    "water_bridges": {"enabled": False},  # Disable
}
```

3. **Use SSD storage:** If on HPC, copy to local SSD first
```bash
cp /slow/storage/trajectory.xtc /tmp/trajectory.xtc
# Then use /tmp path in CONFIG
```

4. **Run on HPC cluster:**
```bash
# Request compute node with more resources
sbatch -N 1 -n 4 --mem=32GB analysis_job.sh
```

---

### Issue: "Memory usage constantly increasing"

**Cause:** Not clearing intermediate variables

**Solution:** Add garbage collection:
```python
import gc

# In analysis loop
for frame in u.trajectory:
    # Do analysis
    process_frame(frame)
    
    # Every 100 frames, clean up
    if frame.frame % 100 == 0:
        gc.collect()
```

---

### Issue: "Slow trajectory loading from network drive"

**Cause:** Network I/O is slow

**Solution:**
```bash
# Copy to local disk first
cp -r /network/path/simulations ./local_copy/

# Then use local path in CONFIG
# After analysis, cleanup:
rm -rf ./local_copy/
```

---

## Visualization Problems

### Issue: "Backend not available" / "No display"

**Error Message:**
```
_tkinter.TclError: no display name and no $DISPLAY environment variable
```

**Cause:** Running on remote/headless server

**Solution:**
```python
# Add to top of notebook:
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

import matplotlib.pyplot as plt

# Now plots will save but not display
# Matplotlib will still save .png files
```

---

### Issue: "Plots look blurry / low quality"

**Cause:** DPI setting too low

**Solution:**
```python
CONFIG = {
    "plotting": {
        "dpi": 300,  # Increase from default 100
    }
}
```

---

### Issue: "Colors not visible / plot colors wrong"

**Cause:** Color names or hex codes incorrect

**Solution:**
```python
# Use standard matplotlib colors
"color": "red"      # Named colors
"color": "C0"       # Tab colors (C0-C9)
"color": "#FF0000"  # Hex colors

# Valid colors:
VALID_COLORS = {
    "red": "#FF0000",
    "blue": "#0000FF",
    "green": "#00AA00",
    "orange": "#FF8C00",
    "purple": "#9400D3",
}

# Check if color is valid
import matplotlib.colors
try:
    matplotlib.colors.to_rgba("#FF6B6B")
    print("Color valid")
except:
    print("Invalid color")
```

---

### Issue: "Plot labels overlapping"

**Cause:** Too many labels or long names

**Solution:**
```python
# In notebook cell after plotting:
fig, ax = plt.subplots(figsize=(16, 8))  # Larger figure

# Rotate labels
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent cutoff
plt.tight_layout()
```

---

## Getting Help

### Before Asking for Help

1. **Check the documentation:**
   - [README.md](README.md) - Overview
   - [docs/INSTALLATION.md](docs/INSTALLATION.md) - Setup
   - [docs/ANALYSIS_GUIDE.md](docs/ANALYSIS_GUIDE.md) - Analysis details
   - [docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md) - Configuration templates

2. **Try minimal example:**
```python
import MDAnalysis as mda
u = mda.Universe("structure.gro")
print(f"Loaded {u.atoms.n_atoms} atoms")
```

3. **Check error message carefully** - note exact line number and code

### Where to Get Help

- **GitHub Issues:** [Report a bug](https://github.com/your-username/BioEMU-Protein-Dynamics/issues)
- **GitHub Discussions:** [Ask a question](https://github.com/your-username/BioEMU-Protein-Dynamics/discussions)
- **Stack Overflow:** Tag with `mdanalysis` or `mdtraj`
- **MDAnalysis Forum:** https://userguide.mdanalysis.org/

### Providing Good Bug Reports

Include:
1. **Error message** (full stack trace)
2. **Your code** (CONFIG and which cells you ran)
3. **Your system** (OS, Python version, library versions):
```bash
python --version
conda list | grep -E "mdanalysis|mdtraj|numpy"
```
4. **Minimal reproducible example**
5. **What you expected vs. what happened**

Example bug report:
```
Title: SASA analysis crashes with large trajectories

Python: 3.9.0
OS: Ubuntu 20.04
MDAnalysis: 2.0.0
MDTraj: 1.9.7

Error:
MemoryError: Unable to allocate 16.0 GiB for an array...

Config:
systems: 1 system with 5 μs trajectory (5 million frames)
frame_stride: 1

Expected: SASA calculated for all frames
Actual: Memory error after ~10,000 frames

Workaround: Using frame_stride=100 works
```

---

## Common Fixes Checklist

- [ ] Conda/pip installed
- [ ] All dependencies installed (`pip list | grep mdanalysis`)
- [ ] File paths correct (use absolute paths)
- [ ] Residue numbers match structure
- [ ] Atom selections valid
- [ ] CONFIG dictionary syntax correct
- [ ] Jupyter kernel restarted after installing packages
- [ ] Frame stride adjusted for memory issues
- [ ] Analysis enabled in CONFIG

---

**Last Updated:** February 2025
