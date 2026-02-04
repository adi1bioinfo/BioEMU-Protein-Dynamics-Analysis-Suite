# Installation — BioEMU Protein Dynamics Analysis Suite

This guide consolidates installation steps for both BioEMU and the Analysis Suite.

## Recommended: Conda environment (tested with Python 3.10)

```bash
conda create -n bioemu-analysis python=3.10
conda activate bioemu-analysis
conda install -c conda-forge --file installation/conda-packages.txt || true
# fall back to installing requirements via pip
pip install -r installation/requirements.txt
```

## Pip quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r installation/requirements.txt
```

## Notes
- For GPU acceleration, ensure CUDA drivers are installed and compatible with your Python packages.
- To enable MD relaxation in BioEMU: `pip install "bioemu[md]>=1.0.0"`

