import argparse
import subprocess
import sys
import os
from pathlib import Path

def check_bioemu_installed():
    """Checks if bioemu is installed in the current environment."""
    try:
        # Check if we can import bioemu or if the module is reachable
        subprocess.run([sys.executable, "-m", "bioemu.sample", "--help"], 
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def run_sampling(protein_dir, sequence, num_samples, output_dir_base):
    """
    Runs the BioEMU sampling command.
    
    Args:
        protein_dir (str): Name of the protein directory/label (e.g., GPCR).
        sequence (str): Path to FASTA file or raw sequence string.
        num_samples (int): Number of conformations to generate.
        output_dir_base (str): Base directory for outputs.
    """
    
    # Define output directory structure: results/{protein_dir}_bioemu
    output_dir = Path(output_dir_base) / f"{protein_dir}_bioemu"
    
    print(f"🚀 Starting BioEMU Sampling for: {protein_dir}")
    print(f"   - Input Sequence: {sequence}")
    print(f"   - Samples: {num_samples}")
    print(f"   - Output Directory: {output_dir}")
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Check Installation
    if not check_bioemu_installed():
        print("\n❌ Error: 'bioemu' module not found or not executable.")
        print("   Please ensure you have activated your environment (e.g., 'conda activate bioemu').")
        print("   Install instructions: https://github.com/microsoft/bioemu")
        sys.exit(1)

    # 2. Construct Command
    cmd = [
        sys.executable, "-m", "bioemu.sample",
        "--sequence", str(sequence),
        "--num_samples", str(num_samples),
        "--output_dir", str(output_dir)
    ]
    
    # 3. Execute
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Sampling Complete! Results saved to: {output_dir}")
        print("   You can now proceed to analysis.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Sampling Failed with error code {e.returncode}.")
        sys.exit(e.returncode)

def main():
    parser = argparse.ArgumentParser(
        description="BioEMU Sampling Wrapper: A framework for generating protein ensembles."
    )
    
    parser.add_argument(
        "--protein_dir", 
        type=str, 
        required=True, 
        help="Label for your protein (e.g., 'GPCR', 'KDEL'). Used for naming output folders."
    )
    parser.add_argument(
        "--sequence", 
        type=str, 
        default="examples/kdel_analysis/starter_data/kdel.fasta",
        help="Path to FASTA file or amino acid sequence string. Default: KDEL example."
    )
    parser.add_argument(
        "--num_samples", 
        type=int, 
        default=100,
        help="Number of conformations to generate. Default: 100."
    )
    parser.add_argument(
        "--output_dir", 
        type=str, 
        default="results",
        help="Base directory for results. Default: './results'"
    )

    args = parser.parse_args()
    
    run_sampling(args.protein_dir, args.sequence, args.num_samples, args.output_dir)

if __name__ == "__main__":
    main()
