# Installation Guide - BioEMU Analysis Suite

Complete setup instructions for all platforms and environments.

## Table of Contents

1. [Quick Install (Recommended)](#quick-install-recommended)
2. [Option 1: Conda Installation](#option-1-conda-installation)
3. [Option 2: Pip with Virtual Environment](#option-2-pip-with-virtual-environment)
4. [Option 3: Docker](#option-3-docker)
5. [Troubleshooting](#troubleshooting)
6. [Verification](#verification)

---

## Quick Install (Recommended)

For most users, this is the fastest way to get started:

```bash
# Clone repository
git clone https://github.com/your-username/BioEMU-Protein-Dynamics.git
cd BioEMU-Protein-Dynamics

# Create conda environment (recommended)
conda create -n bioemu-analysis python=3.9
conda activate bioemu-analysis

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import mdtraj, MDAnalysis; print('✓ Installation successful!')"

# Launch Jupyter
jupyter notebook Comprehensive_Analysis.ipynb
```

---

## Option 1: Conda Installation

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed
- ~2 GB disk space for environment

### Step-by-Step

```bash
# 1. Clone the repository
git clone https://github.com/your-username/BioEMU-Protein-Dynamics.git
cd BioEMU-Protein-Dynamics

# 2. Create a new conda environment
conda create -n bioemu-analysis python=3.9 -y

# 3. Activate the environment
conda activate bioemu-analysis

# 4. Install MDAnalysis from conda-forge (recommended)
conda install -c conda-forge mdanalysis mdtraj -y

# 5. Install remaining dependencies from pip
pip install -r requirements.txt
```

### Using Environment File (Alternative)

```bash
# Create from YAML file
conda env create -f environment.yml

# Activate
conda activate bioemu-analysis
```

### Managing the Conda Environment

```bash
# List all environments
conda env list

# Activate environment
conda activate bioemu-analysis

# Deactivate environment
conda deactivate

# Update packages
conda update --all -c conda-forge

# Remove environment (if needed)
conda env remove -n bioemu-analysis
```

---

## Option 2: Pip with Virtual Environment

### Prerequisites

- Python 3.8+ installed ([Download](https://www.python.org/downloads/))
- pip package manager (included with Python)
- ~1 GB disk space

### Linux / macOS

```bash
# 1. Clone repository
git clone https://github.com/your-username/BioEMU-Protein-Dynamics.git
cd BioEMU-Protein-Dynamics

# 2. Create virtual environment
python3 -m venv bioemu-env

# 3. Activate virtual environment
source bioemu-env/bin/activate

# 4. Upgrade pip (optional but recommended)
pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt
```

### Windows

```bash
# 1. Clone repository
git clone https://github.com/your-username/BioEMU-Protein-Dynamics.git
cd BioEMU-Protein-Dynamics

# 2. Create virtual environment
python -m venv bioemu-env

# 3. Activate virtual environment
bioemu-env\Scripts\activate

# 4. Upgrade pip (optional)
python -m pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt
```

### Managing Virtual Environment

```bash
# View where venv is located
which python  # Linux/macOS
where python  # Windows

# Deactivate environment
deactivate

# Reactivate environment
source bioemu-env/bin/activate  # Linux/macOS
bioemu-env\Scripts\activate     # Windows
```

---

## Option 3: Docker

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed

### Build and Run

```bash
# 1. Clone repository
git clone https://github.com/your-username/BioEMU-Protein-Dynamics.git
cd BioEMU-Protein-Dynamics

# 2. Build Docker image
docker build -t bioemu-analysis:latest .

# 3. Run container with volume mounting
docker run -it \
  -v $(pwd):/workspace \
  -p 8888:8888 \
  bioemu-analysis:latest

# 4. Inside container, launch Jupyter
jupyter notebook --ip=0.0.0.0 --allow-root
```

### Access Jupyter in Docker

Open browser and go to: `http://localhost:8888`

### Using Docker Compose (Optional)

```yaml
# docker-compose.yml
version: '3'
services:
  bioemu:
    build: .
    volumes:
      - .:/workspace
    ports:
      - "8888:8888"
    command: jupyter notebook --ip=0.0.0.0 --allow-root
```

Run with:

```bash
docker-compose up
```

---

## Verification

### Check Installation

```bash
python -c "import mdtraj, MDAnalysis, pandas, numpy; print('✓ All core packages installed')"
```

### Verify MDAnalysis

```python
import MDAnalysis as mda
print(mda.__version__)
```

### Verify MDTraj

```python
import mdtraj as md
print(md.__version__)
```

### Test with Sample Data

```bash
# If sample data is included
cd examples/kdel_comparison
jupyter notebook
```

---

## System-Specific Instructions

### Ubuntu/Debian

```bash
# Install system dependencies (optional, for compilation)
sudo apt-get install build-essential python3-dev

# Proceed with conda or pip installation above
```

### macOS

```bash
# If using Homebrew
brew install python@3.9

# Then proceed with pip installation
```

### Windows 10/11

1. Install [Python 3.9+](https://www.python.org/downloads/windows/)
   - Check "Add Python to PATH" during installation
2. Open Command Prompt or PowerShell
3. Follow pip installation steps above

### High-Performance Cluster (HPC)

```bash
# Example: Using module system (SLURM environment)
module load python/3.9
module load gcc/10

python3 -m venv bioemu-env
source bioemu-env/bin/activate
pip install -r requirements.txt
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'mdtraj'"

**Solution**: MDAnalysis wasn't installed. Run:

```bash
conda install -c conda-forge mdanalysis mdtraj -y
# OR
pip install mdtraj
```

### Issue: "Permission denied" when installing with pip

**Solution**: Use user installation:

```bash
pip install --user -r requirements.txt
```

### Issue: Conda command not found

**Solution**: 
- Reinstall [Anaconda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- Or use pip with virtual environment instead

### Issue: Jupyter kernel not found

**Solution**:

```bash
python -m ipykernel install --user --name bioemu-analysis
```

### Issue: Memory error with large trajectories

**Solution**: Use chunked processing:

```python
# In the notebook, set smaller chunk sizes
CONFIG["chunk_size"] = 1000  # Process 1000 frames at a time
```

### Issue: Matplotlib backend error (especially on SSH/remote)

**Solution**: Use non-interactive backend:

```python
import matplotlib
matplotlib.use('Agg')  # Add at top of notebook
```

### Issue: "libGL.so.1: cannot open shared object file" (Linux HPC)

**Solution**: 

```bash
export LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH
```

---

## Updating Installation

### Update Conda Environment

```bash
conda activate bioemu-analysis
conda update --all
```

### Update Pip Installation

```bash
source bioemu-env/bin/activate
pip install --upgrade -r requirements.txt
```

### Update Repository

```bash
git pull origin main
```

---

## Performance Optimization

### For Large Trajectories

```bash
# Install HDF5 support for faster file I/O
conda install -c conda-forge h5py

# Use MDAnalysis with in-memory trajectory
# (See ANALYSIS_GUIDE.md for details)
```

### For Multi-GPU Analysis

```bash
# Install GPU-accelerated libraries (optional)
conda install -c conda-forge cudatoolkit
pip install cupy  # GPU-accelerated NumPy
```

---

## Next Steps

1. **Quick Start**: See [README.md](../README.md#quick-start)
2. **Example Analysis**: Run `examples/kdel_comparison/`
3. **Full Documentation**: Read [ANALYSIS_GUIDE.md](./ANALYSIS_GUIDE.md)
4. **Configuration**: Check [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)

---

## Getting Help

- ❓ Check [FAQ](#troubleshooting) section above
- 🔍 Search [GitHub Issues](https://github.com/your-username/BioEMU-Protein-Dynamics/issues)
- 💬 Open a [GitHub Discussion](https://github.com/your-username/BioEMU-Protein-Dynamics/discussions)
- 📧 Contact maintainer via GitHub

---

## System Requirements Summary

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.9+ |
| RAM | 4 GB | 8+ GB |
| Disk Space | 2 GB | 10+ GB |
| OS | Linux/macOS/Windows | Linux/macOS |

---

**Last Updated**: February 2025
