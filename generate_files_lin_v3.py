import os
import random
import subprocess
import math
import argparse
import traceback
from pathlib import Path
from math import exp, expm1

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--num_files_total',help='# of total files',required=True)
    parser.add_argument('-w','--width',help='Filesystem width. # of top level directories')
    parser.add_argument('-d','--base_dir',help='Base dir to generate files to. e.g. "/tmp/test 1/dir1" ',required=True)
    parser.add_argument('-s','--avg_file_size',help='Avg. file size in bytes',required=True)
    parser.add_argument('-c','--counter_start',help='Directory counter, default is 0')
    args_list = parser.parse_args()

    # define the number of files
    # num_files_total = 524520
    # width = 5
    # num_files_per_p = int(num_files_total/width)

    if args_list.width is None:
        width = 1
    else:
        width = int(args_list.width)

    if args_list.counter_start is None:
        dir_count = 0
    else:
        dir_count = int(args_list.counter_start)

    num_files_total = int(args_list.num_files_total)
    num_files_per_p = int(num_files_total/width)

    count = 0
    total_size = 0

    while count < num_files_total:
        depth = random.randint(3,7)
        #depth = 2
        #avg_file_size = int(math.pow(2,random.randint(1,9))*1024)
        avg_file_size = int(args_list.avg_file_size) 
        size = avg_file_size * num_files_per_p
        total_size = total_size + size
        count = count + num_files_per_p

        depth = depth + 1
        directory = args_list.base_dir + str(dir_count)
        print(directory)
        subprocess.call(["./file_gopher_linux", "-D", str(depth), "-s", str(size), "-n", str(num_files_per_p), "-d", str(directory)])
        dir_count = dir_count + 1

    print('Total # of files created: ' + str(count))
    print('Total size of dataset (GB): ' + (str(int(total_size/(1024*1024*1024)))))

except:
    print('\n=====================================\n')
    traceback.print_exc()
