# Example Analyses

This folder contains example configurations and templates for analyzing different types of protein systems. These examples demonstrate how to use this toolkit for various analysis scenarios.

## Available Examples

### 1. Comparative State Analysis (kdel_comparison/)

**Analysis Type**: Comparing different states of a protein
**Highlights**:
- Multi-state system comparison
- Ligand binding effects
- Conformational dynamics

**Configuration Template**: See `docs/QUICK_REFERENCE.md` for configuration examples

**To Run**:
```python
# In notebook, adapt the configuration to your protein system
# Refer to kdel_comparison/kdel_config.py as a template
```

---

### 2. Variant Analysis (gpcr_variants/)

**Analysis Type**: Comparing wild-type and mutant variants
**Highlights**:
- Multi-system comparison
- Structural differences across variants
- Stability and flexibility analysis

**Configuration Template**: See `docs/QUICK_REFERENCE.md` - Template 2

---

### 3. Functional Dynamics (ion_channel/)

**Analysis Type**: Analyzing conformational states and transitions
**Highlights**:
- State-dependent analysis
- Structural changes between states
- Hydration and interaction patterns
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
