#TODO: Take the file name as an input (DONE)
#TODO: Take a folder as an input (loop through and print the comment number of each)
#TODO: Language support beyond python #
#TODO: Integrate database?

import io
import textwrap
import argparse
import os

file_name = 'sample.txt'

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

def get_arguments():
    """ The argument parser of the command-line version """
    parser = argparse.ArgumentParser(description=('Comment counting program'))

    parser.add_argument('--input_folder', '-i',
                        help="name of the input folder", type=lambda x: is_valid_file(parser, x),
                        dest='i')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_arguments()
    input_folder_name = args.i
    comment_count = numberOfComments(input_folder_name)
    line_count = numberOfTotalLines(input_folder_name)
    print_data(input_folder_name, comment_count, line_count)
