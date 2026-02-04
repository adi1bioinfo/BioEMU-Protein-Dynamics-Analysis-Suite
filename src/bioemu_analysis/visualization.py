"""
Visualization functions for MD analysis plots.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_rmsd(df_rmsd, config, save_path=None):
    """
    Plot RMSD comparison across systems.
    
    Parameters
    ----------
    df_rmsd : pd.DataFrame
        DataFrame with columns: Time_ns, RMSD_A, System
    config : dict
        Configuration dictionary with plotting parameters
    save_path : str, optional
        Path to save figure
    
    Returns
    -------
    matplotlib.figure.Figure
        Generated figure
    """
    colors = {sys_key: sys_info.get("color", "#000000") 
              for sys_key, sys_info in config["systems"].items()}
    labels = {sys_key: sys_info.get("label", sys_key) 
              for sys_key, sys_info in config["systems"].items()}
    
    sns.set_style(config["plotting"]["figure_style"])
    fig, ax = plt.subplots(figsize=(14, 6))
    
    rolling_window_ns = config["plotting"]["rolling_average_ns"]
    
    for sys_key in config["systems"].keys():
        df_sys = df_rmsd[df_rmsd['System'] == sys_key].copy()
        
        if df_sys.empty:
            continue
        
        # Calculate rolling average
        dt = (df_sys['Time_ns'].iloc[1] - df_sys['Time_ns'].iloc[0]) if len(df_sys) > 1 else 1.0
        window_frames = max(1, int(rolling_window_ns / dt))
        df_sys['RMSD_smooth'] = df_sys['RMSD_A'].rolling(
            window=window_frames, min_periods=1, center=True
        ).mean()
        
        # Statistics for last N frames
        last_ns = config["plotting"]["last_frames_ns"]
        df_recent = df_sys[df_sys['Time_ns'] >= (df_sys['Time_ns'].max() - last_ns)]
        mean_rmsd = df_recent['RMSD_A'].mean()
        std_rmsd = df_recent['RMSD_A'].std()
        
        label = f"{labels[sys_key]} (avg: {mean_rmsd:.2f} Â± {std_rmsd:.2f} Ã)"
        color = colors[sys_key]
        
        ax.plot(df_sys['Time_ns'], df_sys['RMSD_A'], color=color, alpha=0.2, linewidth=0.5)
        ax.plot(df_sys['Time_ns'], df_sys['RMSD_smooth'], color=color, linewidth=2.5, label=label)
    
    ax.set_xlabel("Time (ns)", fontsize=12, fontweight='bold')
    ax.set_ylabel("RMSD (Ã)", fontsize=12, fontweight='bold')
    ax.set_title(f"RMSD Analysis: {config['protein_name']}", fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='best')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config["plotting"]["dpi"], bbox_inches='tight')
    
    return fig


def plot_rmsf(df_rmsf, config, save_path=None):
    """
    Plot per-residue RMSF with secondary structure annotations.
    
    Parameters
    ----------
    df_rmsf : pd.DataFrame
        DataFrame with columns: Residue, RMSF_A, System
    config : dict
        Configuration dictionary
    save_path : str, optional
        Path to save figure
    
    Returns
    -------
    matplotlib.figure.Figure
        Generated figure
    """
    colors = {sys_key: sys_info.get("color", "#000000") 
              for sys_key, sys_info in config["systems"].items()}
    labels = {sys_key: sys_info.get("label", sys_key) 
              for sys_key, sys_info in config["systems"].items()}
    
    sns.set_style(config["plotting"]["figure_style"])
    fig, ax = plt.subplots(figsize=(14, 6))
    
    for sys_key in config["systems"].keys():
        df_sys = df_rmsf[df_rmsf['System'] == sys_key]
        
        if df_sys.empty:
            continue
        
        ax.plot(df_sys['Residue'], df_sys['RMSF_A'], color=colors[sys_key], 
                linewidth=2.5, label=labels[sys_key])
    
    # Add secondary structure annotations
    if config["secondary_structure"]["helices"]:
        helix_colors = ['gold', 'lightcoral', 'plum', 'lightskyblue', 'mediumpurple']
        max_rmsf = df_rmsf['RMSF_A'].max()
        
        for i, (start, end, name) in enumerate(config["secondary_structure"]["helices"]):
            color = helix_colors[i % len(helix_colors)]
            ax.axvspan(start, end, color=color, alpha=0.2, zorder=0)
            ax.text((start + end) / 2, max_rmsf * 0.95, name, 
                   ha='center', va='top', fontsize=9)
    
    ax.set_xlabel("Residue Number", fontsize=12, fontweight='bold')
    ax.set_ylabel("RMSF (Ã)", fontsize=12, fontweight='bold')
    ax.set_title(f"RMSF Analysis: {config['protein_name']}", fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='best')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(bottom=0)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config["plotting"]["dpi"], bbox_inches='tight')
    
    return fig


def plot_sasa_heatmap(df_sasa, config, save_path=None, top_residues=20):
    """
    Plot SASA values as heatmap.
    
    Parameters
    ----------
    df_sasa : pd.DataFrame
        DataFrame with SASA values
    config : dict
        Configuration dictionary
    save_path : str, optional
        Path to save figure
    top_residues : int
        Number of most exposed residues to show
    
    Returns
    -------
    matplotlib.figure.Figure
        Generated figure
    """
    # Get mean SASA per residue
    residue_cols = [col for col in df_sasa.columns if col not in ['Time_ns', 'System']]
    sasa_mean = df_sasa[residue_cols].mean()
    top_exposed = sasa_mean.nlargest(top_residues)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.bar(range(len(top_exposed)), top_exposed.values, color='steelblue', alpha=0.7)
    ax.set_xticks(range(len(top_exposed)))
    ax.set_xticklabels(top_exposed.index, rotation=45, ha='right')
    ax.set_ylabel("Average SASA (Å²)", fontsize=12, fontweight='bold')
    ax.set_title(f"Top {top_residues} Most Exposed Residues", fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config["plotting"]["dpi"], bbox_inches='tight')
    
    return fig


def plot_distance_timeseries(times, distances_dict, labels, colors, title, save_path=None):
    """
    Plot distance time series.
    
    Parameters
    ----------
    times : np.ndarray
        Time points (ns)
    distances_dict : dict
        Dictionary with distance arrays keyed by system/pair name
    labels : dict
        Label mapping
    colors : dict
        Color mapping
    title : str
        Plot title
    save_path : str, optional
        Path to save figure
    
    Returns
    -------
    matplotlib.figure.Figure
        Generated figure
    """
    fig, ax = plt.subplots(figsize=(12, 5))
    
    for key, distances in distances_dict.items():
        ax.plot(times, distances, label=labels.get(key, key), 
                color=colors.get(key, '#000000'), linewidth=2, alpha=0.8)
    
    ax.set_xlabel("Time (ns)", fontsize=11, fontweight='bold')
    ax.set_ylabel("Distance (Ã)", fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_hydrogen_bond_occupancy(df_hbonds, title="Hydrogen Bond Occupancy", 
                                  top_n=20, save_path=None):
    """
    Plot H-bond occupancy as bar chart.
    
    Parameters
    ----------
    df_hbonds : pd.DataFrame
        DataFrame with columns: Residue_Pair, Occupancy
    title : str
        Plot title
    top_n : int
        Number of top H-bonds to show
    save_path : str, optional
        Path to save figure
    
    Returns
    -------
    matplotlib.figure.Figure
        Generated figure
    """
    df_sorted = df_hbonds.sort_values('Occupancy', ascending=True).tail(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors_hb = ['green' if x >= 0.5 else 'orange' if x >= 0.2 else 'red' 
                 for x in df_sorted['Occupancy']]
    
    ax.barh(df_sorted['Residue_Pair'], df_sorted['Occupancy'], color=colors_hb, alpha=0.7)
    ax.set_xlabel("Occupancy", fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlim(0, 1.0)
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, v in enumerate(df_sorted['Occupancy']):
        ax.text(v + 0.02, i, f'{v:.1%}', va='center', fontsize=9)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
