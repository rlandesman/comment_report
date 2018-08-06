#BUG:  Ensure that both individual file and folders are supported in CLI input
#TODO: Language support beyond python #, depending on file type of file being read in.
#TODO: Integrate database?

import io
import textwrap
import argparse
import os
from tabulate import tabulate
from CLI_output import *

def get_arguments():
    """ The argument parser of the command-line version """
    parser = argparse.ArgumentParser(description=('Comment counting program'))

    parser.add_argument('--input_folder', '-i',
                        help="name of the input folder", type=lambda x: is_valid_file(parser, x),
                        dest='i')

    parser.add_argument('--single_file', '-s',
                        help="name of the input file", type=lambda x: is_valid_file(parser, x),
                        dest='s')

    args = parser.parse_args()
    return args

def numberOfComments(file_name):
    isComment = False
    x = 0
    with open(file_name) as input:
        for line in input:
            isComment = False
            for char in line:
                if char == "#":
                    isComment = True
                else:
                    pass
            if (isComment == True):
                x = x + 1
        return(x)

def numberOfTotalLines(file_name):
    x = 0
    with open(file_name) as input:
        for line in input:
            x = x + 1
    return(x)

def is_valid_file(parser, arg):
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def print_data(file_name, number_of_comments,number_of_lines):
    """
    Deprecated function due to tabulate library
    """
    print textwrap.dedent("""\
    In total there are %s lines of code in this file
    In the file: %s, there are %s comment lines
    """ %(number_of_lines, file_name, number_of_comments))

def iterate_folder(folder_name):
    """
    Put the names of each file in the directory into an iteratable list
    """
    returnList = []
    for file in os.listdir(folder_name):
        if file.endswith(".txt") or file.endswith(".py"):
            returnList.append(file)
    return returnList

if __name__ == "__main__":
    returnTable = []
    args = get_arguments()
    print_to_CLI(args)
    #return args
