# Example Analyses

This folder contains example configurations and results for different protein types.

## Available Examples

### 1. KDEL Receptor Comparison (kdel_comparison/)

**Protein**: KDEL Receptor (KDELR)
**Analysis**: Apo vs. KDEL peptide-bound conformations
**Highlights**:
- 7 transmembrane helices
- Ligand-induced conformational changes
- Water-mediated interactions

**Files**:
- `kdel_config.py` - Configuration file with KDEL-specific settings
- `data/` - (add your simulation files here)
- `results/` - (analysis output)

**To Run**:
```python
# In notebook, replace CONFIG with:
from examples.kdel_comparison.kdel_config import CONFIG

# Or copy contents into the notebook's configuration cell
```

---

### 2. GPCR Variants (gpcr_variants/)

**Protein**: G-Protein Coupled Receptor
**Analysis**: Wild-type vs. point mutations
**Highlights**:
- Multi-system comparison
- Variant effect prediction
- Conformational stability

**Configuration Template**: See `docs/QUICK_REFERENCE.md` - Template 2

---

### 3. Ion Channel Gating (ion_channel/)

**Protein**: Ion Channel
**Analysis**: Closed vs. open state dynamics
**Highlights**:
- Pore hydration analysis
- Gating mechanism
- Helix reorientation

**Configuration Template**: See `docs/QUICK_REFERENCE.md` - Template 3

---

## How to Create Your Own Example

1. **Create a folder**: `examples/my_protein/`

2. **Add configuration file**: `my_protein_config.py`
   ```python
   CONFIG = {
       "protein_name": "My Protein",
       "systems": { ... },
       # ... rest of config
   }
   ```

3. **Create data subfolder**: `examples/my_protein/data/`
   - Add your topology and trajectory files

4. **Add README**: `examples/my_protein/README.md`
   - Explain the protein and what to expect

5. **Run analysis** and save results to `examples/my_protein/results/`

---

## Contributing Examples

Found an interesting analysis? Share it!

1. Fork this repository
2. Add your example following the template above
3. Include a brief description and results summary
4. Submit a pull request

---

## Tips for Using Examples

- **Start simple**: Begin with KDEL example if new to the suite
- **Adapt templates**: Use `QUICK_REFERENCE.md` templates as starting points
- **Test first**: Run on a subset of data first (smaller frame stride)
- **Compare systematically**: Keep system names and selections consistent

---

For more information:
- [ANALYSIS_GUIDE.md](../docs/ANALYSIS_GUIDE.md) - Detailed analysis descriptions
- [QUICK_REFERENCE.md](../docs/QUICK_REFERENCE.md) - Configuration templates
- [README.md](../README.md) - Main documentation

---

**Last Updated**: February 2025
