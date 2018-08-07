#TODO: Integrate database in cloud?
#TODO: GUI on desktop
#TODO: Collect data over time (connected to database)
#BUG:  Single file broken because doesnt know which directory to go
#TODO: Figure out bitbucket integrations, in order to know where these files will sit and how
#TODO: Fix ratio  statistic

import io
import textwrap
import argparse
import os
from tabulate import tabulate
from CLI_output import *

def get_arguments():
    """ The argument parser of the command-line version """
    parser = argparse.ArgumentParser(description=('Comment counting program'))

    parser.add_argument('-i',
                        help="name of the input folder", type=lambda x: is_valid_file(parser, x),
                        dest='input_folder')

    args = parser.parse_args()
    return args

def changeDirectory(dir_name):
    if(args.input_folder != None):
        os.chdir(dir_name)

def numberOfComments(file_name, comment_char, dir_name):
    """ Collect data on number of comments in the current file """
    isComment = False
    x = 0

    os.chdir(dir_name)
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
                    idx+=1
                if(comment_char=="/"):
                    if (line[idx+1]==comment_char and line[idx]==comment_char):
                        isComment = True
                    else:
                        pass
                    idx+=1
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

def numberOfTotalLines(file_name):
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

def iterate_folder(folder_name):
    """
    Put the names of each file in the directory into an iteratable list
    Currently supported languages: Python, Java, textfile
    """
    returnList = []
    for file in os.listdir(folder_name):
        if (file.endswith(".txt")
        or file.endswith(".py")
        or file.endswith(".java")
        or file.endswith(".s")):
            returnList.append(file)
    return returnList

if __name__ == "__main__":
    args = get_arguments()
    print(print_to_CLI(args))
