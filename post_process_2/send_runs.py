#!/Local/ph_daniel/anaconda3/bin/python -u

import csv
import os
import re

import post_process_main_file

mac = True

if mac:
    prefix = "/Users/jalal/Desktop/ECMC/ECMC_simulation_results3.0/"
    code_prefix = "/Users/jalal/Desktop/ECMC"
else:
    prefix = "C:/Users/Galal/ECMC/"
    code_prefix = "C:/Users/Galal/OneDrive - Technion/Desktop/figures/results/"

# prefix = "/storage/ph_daniel/danielab/ECMC_simulation_results3.0/"
# code_prefix = "/storage/ph_daniel/jalal/ECMC_post_process_results/"


def params_from_name(name):
    ss = re.split("[_=]", name)
    for i, s in enumerate(ss):
        if s == 'N':
            N = int(ss[i + 1])
        if s == 'h':
            h = float(ss[i + 1])
        if s == 'rhoH':
            rhoH = float(ss[i + 1])
        if s == 'triangle' or s == 'square':
            ic = s
            if ss[i - 1] == 'AF' and s == 'triangle':
                ic = 'honeycomb'
    return N, h, rhoH, ic


def create_op_dir(sim):
    op_dir = os.path.join(prefix, sim, "OP")
    if not os.path.exists(op_dir):
        os.mkdir(op_dir)
    return


def main():

    fields = ['file name', 'AF order parameter', 'no of connected components', 'Bipartiteness', 'no. of dislocations', 'no of unpaired vecs after first pairing']
    sims = [d for d in os.listdir(prefix) if d.startswith('N=') and os.path.isdir(os.path.join(prefix, d))]

    for sim in sims:
        create_op_dir(sim)
    f = open(os.path.join(code_prefix, 'post_process_files_to_run.csv'), 'wt')
    try:
        writer = csv.writer(f, lineterminator='\n')
        for sim_name in sims:
            N, h, rhoH, ic = params_from_name(sim_name)
            # comment this out to run post_process on all files in simulation results
            if h == 0.8 and rhoH == 0.81 and N == 90000 and ic == 'square':
                writer.writerow((sim_name,))

    finally:
        f.close()

    try:

        ff = open(os.path.join(code_prefix, 'list_of_jobs.txt'), 'wt')
        f = open(os.path.join(code_prefix, 'post_process_files_to_run.csv'), 'r')
        folders_to_run = csv.reader(f)
        jobs_writer = csv.writer(ff, lineterminator='\n')

        for [folder] in folders_to_run:
            N, h, rhoH, ic = params_from_name(folder)
            join_path = os.path.join(prefix, folder+'/')
            files = [d for d in os.listdir(join_path) if d.isnumeric()] # and d == '21648433']
            destination = open(os.path.join(code_prefix, 'post_process_results' + folder + '.csv'), 'wt')
            writer = csv.writer(destination, lineterminator='\n')
            writer.writerow(fields)
            for file in files:
                jobs_writer.writerow((folder, file))
                ff.flush()
                # parameters = post_process_main_file.read_from_file(N, rhoH, h, join_path + file, destination)
                # row = [file] + list(parameters)
                # writer.writerow(row)
                # destination.flush()

    finally:
        os.system("condor_submit post_process_run.sub")
        ff.close()
        destination.close()
        f.close()


if __name__ == "__main__":
    main()
