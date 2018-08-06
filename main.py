#TODO: Take the file name as an input (DONE)
#TODO: Take a folder as an input (loop through and print the comment number of each) (DONE)
#TODO: Make data printing prettier basically
#TODO: Language support beyond python #, depending on file type of file being read in.
#TODO: Integrate database?

import io
import textwrap
import argparse
import os
import tabulate

def get_arguments():
    """ The argument parser of the command-line version """
    parser = argparse.ArgumentParser(description=('Comment counting program'))

    parser.add_argument('--input_folder', '-i',
                        help="name of the input folder", type=lambda x: is_valid_file(parser, x),
                        dest='i')

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
    input_folder_name = args.i
    list_files = iterate_folder(input_folder_name)
    for oneFile in list_files:
        comment_count = numberOfComments(oneFile)
        line_count = numberOfTotalLines(oneFile)
        false_tuple = []
        false_tuple.append(line_count)
        false_tuple.append(comment_count)
        returnTable.append(false_tuple)
    print(returnTable)
