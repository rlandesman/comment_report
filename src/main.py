# TODO: Integrate this python script as backend to the website?
# TODO: Collect data over time (connected to database)
# TODO: Bitbucket/Github integration still neccessary
# TODO: It's static right now; Trends per repo per week/day would be cooler of a project.

import io
import textwrap
import argparse
import os
from tabulate import tabulate
from CLI_output import *
from visualize import *
from stats import *

def get_arguments():
    """ The argument parser of the command-line version """
    parser = argparse.ArgumentParser(description=('Comment counting program'))

    parser.add_argument('-i',
                        help="name of the input folder", type=lambda x: is_valid_file(parser, x),
                        dest='input_folder')

    parser.add_argument('-g',
                        help="name of the Github/BitBucket HTTPS link",
                        dest='input_repo')

    args = parser.parse_args()
    return args

def delete_single_dir(args):
    if (args.input_folder != None):
        pass
    elif (args.input_repo != None):
        os.system("echo")
        current = (os.getcwd())
        os.system("rm -rf " + current)
    else:
        pass


if __name__ == "__main__":
    args = get_arguments()
    data = gather_data(args)
    print_to_CLI(data, args)
    visualize(data)
    delete_single_dir(args)
