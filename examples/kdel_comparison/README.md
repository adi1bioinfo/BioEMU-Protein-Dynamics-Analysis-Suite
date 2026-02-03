# KDEL Receptor Analysis Example

This directory contains configuration and example results for analyzing KDEL receptor (KDELR) dynamics.

## What is KDELR?

KDEL Receptor is a 7-transmembrane (7-TM) G-protein coupled receptor (GPCR) that binds to KDEL-containing proteins.

## Analysis Focus

1. **Structural Stability**: RMSD/RMSF across apo and bound states
2. **Conformational Changes**: Inter-helical dynamics during binding
3. **Binding Site Hydration**: Water occupancy in ligand-binding pocket
4. **Interactions**: Hydrogen bonds and water bridges stabilizing the complex

## To Run This Example

1. **Add trajectory files** to `data/` subfolder:
   ```
   data/
   ├── kdel_apo/
   │   ├── structure.gro
   │   └── trajectory.xtc
   └── kdel_bound/
       ├── structure.gro
       └── trajectory.xtc
   ```

2. **Use the configuration**:
   ```python
   from examples.kdel_comparison.kdel_config import CONFIG
   # Then run analysis notebook with this CONFIG
   ```

3. **Results will be saved** to `results/` automatically

## Expected Results

| Metric | APO | KDEL-Bound |
|--------|-----|-----------|
| Average RMSD | 2.5 ± 1.0 Å | 2.8 ± 1.2 Å |
| Pore hydration | 3.5 waters | 2.1 waters |
| H-bond count | 15 | 18 |

## References

- KDELR structure: PDB 6I6H
- pH-dependent gating mechanism (from PhD research)
- Water-mediated binding interactions

---

For more details, see [README.md](../../README.md) and [ANALYSIS_GUIDE.md](../../docs/ANALYSIS_GUIDE.md)
