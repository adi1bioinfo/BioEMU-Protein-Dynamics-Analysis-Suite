# Use official Python runtime as base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install conda for MDAnalysis (from conda-forge)
RUN apt-get update && apt-get install -y conda \
    && rm -rf /var/lib/apt/lists/*

# Install MDAnalysis from conda-forge
RUN conda install -c conda-forge mdanalysis mdtraj -y && conda clean -afy

# Copy repository
COPY . .

# Expose Jupyter port
EXPOSE 8888

# Default command - start Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
