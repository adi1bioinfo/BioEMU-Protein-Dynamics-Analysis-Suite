
def test_import_package():
    """Test that the package can be imported."""
    try:
        import bioemu_analysis
        assert True
    except ImportError:
        assert False, "Failed to import bioemu_analysis"

def test_import_submodules():
    """Test importing submodules."""
    from bioemu_analysis import trajectory_loader
    from bioemu_analysis import analysis_functions
    from bioemu_analysis import visualization
    
    assert trajectory_loader is not None
    assert analysis_functions is not None
    assert visualization is not None
