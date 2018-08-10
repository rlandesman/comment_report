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

def compute_comment_stats(file_name, comment_char):
    """ Collect data on number of comments in the current file """
    isComment = False
    x = 0

    with open(file_name) as input:
        idx = 0
        for line in input:
            isComment = False
            while idx < (len(line) - 1):
                if(comment_char == "#"):
                    if (line[idx] == comment_char and line[idx+1] != '"'  and line[idx-1] != '"'):
                        isComment = True
                    else:
                        pass
                if(comment_char=="/"):
                    if (line[idx+1]==comment_char and line[idx]==comment_char):
                        isComment = True
                    else:
                        pass
                if(comment_char=="@"):
                    if (line[idx]==comment_char):
                        isComment = True
                    else:
                        pass
                idx+=1
            if (isComment == True):
                x = x + 1
            idx=0
        return(x)

def compute_linenumber_stats(file_name):
    """ Collect data on number of total lines in the current file """
    x = 0
    with open(file_name) as input:
        for line in input:
            x = x + 1
    return(x)

def is_valid_file(parser, arg):
    """ Check if file can be opened (legit path?) """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def single_dir_cleanup():
    """ Remove single directory that was cloned througn github """
    os.system("cd ..") #Idk why there are two cd calls tbh but it works
    os.system("cd ..")
    dir_name = (os.path.dirname(os.path.realpath(__file__)))
    os.system("rm -rf "+ dir_name)

if __name__ == "__main__":
    args = get_arguments()
    data = gather_data(args)
    visualize(data)
    print_to_CLI(data)
    single_dir_cleanup()
