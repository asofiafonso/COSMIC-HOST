import os
import pandas as pd
import subprocess

num_cores = os.cpu_count()


filename = 'SN_data_8bands_flux.txt'
df = pd.read_csv(filename, sep="\s+")

sfhs = ["insitu", "lognormal", "delayedexp"]
engines = ["emcee", "dynesty"]

param_files_dir = "./"


for sfh in sfhs:
    for engine in engines:
        for galaxy_id in df['ID']:
            param_file = f"{param_files_dir}galapy_hyper_parameter_{int(galaxy_id)}_{sfh}_{engine}.py"

            command = f"galapy-fit {param_file} --multiprocessing {num_cores - 2}"

            try:
                subprocess.run(command, check=True, shell=True)
                print(f"Successfully processed galaxy ID {galaxy_id}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing galaxy ID {galaxy_id}: {e}")

    #break
