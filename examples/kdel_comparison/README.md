# Comparative State Analysis Example

This directory contains a configuration template for analyzing multi-state protein dynamics.

## Analysis Template

This example demonstrates comparative analysis of different protein states (e.g., apo vs. ligand-bound, wild-type vs. mutant, open vs. closed).

## Analysis Focus

1. **Structural Stability**: RMSD/RMSF across different states
2. **Conformational Changes**: Domain or secondary structure dynamics
3. **Solvation Patterns**: Water accessibility and occupancy
4. **Interaction Analysis**: Hydrogen bonds and contact patterns

## To Use This Template

1. **Prepare your trajectory files**:
   ```
   your_project/
   ├── data/
   │   ├── state1/
   │   │   ├── structure.gro (or .pdb)
   │   │   └── trajectory.xtc (or .dcd, .h5)
   │   └── state2/
   │       ├── structure.gro
   │       └── trajectory.xtc
   ```

2. **Adapt the configuration**:
   ```python
   from examples.kdel_comparison.kdel_config import CONFIG
   # Modify protein_name, paths, and analysis parameters for your system
   ```

3. **Results will be saved** to your specified output directory

## Configuration Tips

- See `docs/QUICK_REFERENCE.md` for detailed configuration options
- Adjust analysis parameters (stride, cutoffs) based on your trajectory size
- Define secondary structure regions if analyzing helices/sheets
- Use consistent file formats across all systems being compared

---

For more details, see [README.md](../../README.md) and [ANALYSIS_GUIDE.md](../../docs/ANALYSIS_GUIDE.md)
