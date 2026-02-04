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
        
        label = f"{labels[sys_key]} (avg: {mean_rmsd:.2f} ± {std_rmsd:.2f} Å)\"\n        color = colors[sys_key]\n        \n        ax.plot(df_sys['Time_ns'], df_sys['RMSD_A'], color=color, alpha=0.2, linewidth=0.5)\n        ax.plot(df_sys['Time_ns'], df_sys['RMSD_smooth'], color=color, linewidth=2.5, label=label)\n    \n    ax.set_xlabel(\"Time (ns)\", fontsize=12, fontweight='bold')\n    ax.set_ylabel(\"RMSD (Å)\", fontsize=12, fontweight='bold')\n    ax.set_title(f\"RMSD Analysis: {config['protein_name']}\", fontsize=14, fontweight='bold')\n    ax.legend(fontsize=11, loc='best')\n    ax.grid(True, alpha=0.3)\n    ax.set_ylim(bottom=0)\n    \n    plt.tight_layout()\n    \n    if save_path:\n        plt.savefig(save_path, dpi=config[\"plotting\"][\"dpi\"], bbox_inches='tight')\n    \n    return fig\n\n\ndef plot_rmsf(df_rmsf, config, save_path=None):\n    \"\"\"\n    Plot per-residue RMSF with secondary structure annotations.\n    \n    Parameters\n    ----------\n    df_rmsf : pd.DataFrame\n        DataFrame with columns: Residue, RMSF_A, System\n    config : dict\n        Configuration dictionary\n    save_path : str, optional\n        Path to save figure\n    \n    Returns\n    -------\n    matplotlib.figure.Figure\n        Generated figure\n    \"\"\"\n    colors = {sys_key: sys_info.get(\"color\", \"#000000\") \n              for sys_key, sys_info in config[\"systems\"].items()}\n    labels = {sys_key: sys_info.get(\"label\", sys_key) \n              for sys_key, sys_info in config[\"systems\"].items()}\n    \n    sns.set_style(config[\"plotting\"][\"figure_style\"])\n    fig, ax = plt.subplots(figsize=(14, 6))\n    \n    for sys_key in config[\"systems\"].keys():\n        df_sys = df_rmsf[df_rmsf['System'] == sys_key]\n        \n        if df_sys.empty:\n            continue\n        \n        ax.plot(df_sys['Residue'], df_sys['RMSF_A'], color=colors[sys_key], \n                linewidth=2.5, label=labels[sys_key])\n    \n    # Add secondary structure annotations\n    if config[\"secondary_structure\"][\"helices\"]:\n        helix_colors = ['gold', 'lightcoral', 'plum', 'lightskyblue', 'mediumpurple']\n        max_rmsf = df_rmsf['RMSF_A'].max()\n        \n        for i, (start, end, name) in enumerate(config[\"secondary_structure\"][\"helices\"]):\n            color = helix_colors[i % len(helix_colors)]\n            ax.axvspan(start, end, color=color, alpha=0.2, zorder=0)\n            ax.text((start + end) / 2, max_rmsf * 0.95, name, \n                   ha='center', va='top', fontsize=9)\n    \n    ax.set_xlabel(\"Residue Number\", fontsize=12, fontweight='bold')\n    ax.set_ylabel(\"RMSF (Å)\", fontsize=12, fontweight='bold')\n    ax.set_title(f\"RMSF Analysis: {config['protein_name']}\", fontsize=14, fontweight='bold')\n    ax.legend(fontsize=11, loc='best')\n    ax.grid(True, alpha=0.3, axis='y')\n    ax.set_ylim(bottom=0)\n    \n    plt.tight_layout()\n    \n    if save_path:\n        plt.savefig(save_path, dpi=config[\"plotting\"][\"dpi\"], bbox_inches='tight')\n    \n    return fig\n\n\ndef plot_sasa_heatmap(df_sasa, config, save_path=None, top_residues=20):\n    \"\"\"\n    Plot SASA values as heatmap.\n    \n    Parameters\n    ----------\n    df_sasa : pd.DataFrame\n        DataFrame with SASA values\n    config : dict\n        Configuration dictionary\n    save_path : str, optional\n        Path to save figure\n    top_residues : int\n        Number of most exposed residues to show\n    \n    Returns\n    -------\n    matplotlib.figure.Figure\n        Generated figure\n    \"\"\"\n    # Get mean SASA per residue\n    residue_cols = [col for col in df_sasa.columns if col not in ['Time_ns', 'System']]\n    sasa_mean = df_sasa[residue_cols].mean()\n    top_exposed = sasa_mean.nlargest(top_residues)\n    \n    fig, ax = plt.subplots(figsize=(12, 6))\n    \n    ax.bar(range(len(top_exposed)), top_exposed.values, color='steelblue', alpha=0.7)\n    ax.set_xticks(range(len(top_exposed)))\n    ax.set_xticklabels(top_exposed.index, rotation=45, ha='right')\n    ax.set_ylabel(\"Average SASA (Ų)\", fontsize=12, fontweight='bold')\n    ax.set_title(f\"Top {top_residues} Most Exposed Residues\", fontsize=14, fontweight='bold')\n    ax.grid(True, alpha=0.3, axis='y')\n    \n    plt.tight_layout()\n    \n    if save_path:\n        plt.savefig(save_path, dpi=config[\"plotting\"][\"dpi\"], bbox_inches='tight')\n    \n    return fig\n\n\ndef plot_distance_timeseries(times, distances_dict, labels, colors, title, save_path=None):\n    \"\"\"\n    Plot distance time series.\n    \n    Parameters\n    ----------\n    times : np.ndarray\n        Time points (ns)\n    distances_dict : dict\n        Dictionary with distance arrays keyed by system/pair name\n    labels : dict\n        Label mapping\n    colors : dict\n        Color mapping\n    title : str\n        Plot title\n    save_path : str, optional\n        Path to save figure\n    \n    Returns\n    -------\n    matplotlib.figure.Figure\n        Generated figure\n    \"\"\"\n    fig, ax = plt.subplots(figsize=(12, 5))\n    \n    for key, distances in distances_dict.items():\n        ax.plot(times, distances, label=labels.get(key, key), \n                color=colors.get(key, '#000000'), linewidth=2, alpha=0.8)\n    \n    ax.set_xlabel(\"Time (ns)\", fontsize=11, fontweight='bold')\n    ax.set_ylabel(\"Distance (Å)\", fontsize=11, fontweight='bold')\n    ax.set_title(title, fontsize=12, fontweight='bold')\n    ax.legend(fontsize=10)\n    ax.grid(True, alpha=0.3)\n    ax.set_ylim(bottom=0)\n    \n    plt.tight_layout()\n    \n    if save_path:\n        plt.savefig(save_path, dpi=300, bbox_inches='tight')\n    \n    return fig\n\n\ndef plot_hydrogen_bond_occupancy(df_hbonds, title=\"Hydrogen Bond Occupancy\", \n                                  top_n=20, save_path=None):\n    \"\"\"\n    Plot H-bond occupancy as bar chart.\n    \n    Parameters\n    ----------\n    df_hbonds : pd.DataFrame\n        DataFrame with columns: Residue_Pair, Occupancy\n    title : str\n        Plot title\n    top_n : int\n        Number of top H-bonds to show\n    save_path : str, optional\n        Path to save figure\n    \n    Returns\n    -------\n    matplotlib.figure.Figure\n        Generated figure\n    \"\"\"\n    df_sorted = df_hbonds.sort_values('Occupancy', ascending=True).tail(top_n)\n    \n    fig, ax = plt.subplots(figsize=(10, 6))\n    \n    colors_hb = ['green' if x >= 0.5 else 'orange' if x >= 0.2 else 'red' \n                 for x in df_sorted['Occupancy']]\n    \n    ax.barh(df_sorted['Residue_Pair'], df_sorted['Occupancy'], color=colors_hb, alpha=0.7)\n    ax.set_xlabel(\"Occupancy\", fontsize=11, fontweight='bold')\n    ax.set_title(title, fontsize=12, fontweight='bold')\n    ax.set_xlim(0, 1.0)\n    ax.grid(True, alpha=0.3, axis='x')\n    \n    # Add value labels\n    for i, v in enumerate(df_sorted['Occupancy']):\n        ax.text(v + 0.02, i, f'{v:.1%}', va='center', fontsize=9)\n    \n    plt.tight_layout()\n    \n    if save_path:\n        plt.savefig(save_path, dpi=300, bbox_inches='tight')\n    \n    return fig\n"
