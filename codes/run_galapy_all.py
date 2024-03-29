import os
import pandas as pd
import subprocess

num_cores = os.cpu_count()

# Read the ASCII table into a DataFrame
filename = 'SNIa_SDSS_flux.txt'
df = pd.read_csv(filename, sep="\s+")


# Path to the directory where the parameter files are stored (adjust as necessary)
param_files_dir = "./"

# Loop over the first 5 galaxies
for galaxy_id in df['ID']:
    param_file = f"{param_files_dir}galapy_hyper_parameter_{int(galaxy_id)}.py"

    # Construct the command to run
    command = f"galapy-fit {param_file} --multiprocessing {num_cores - 2}"

    # Execute the command
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully processed galaxy ID {galaxy_id}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing galaxy ID {galaxy_id}: {e}")

    break
