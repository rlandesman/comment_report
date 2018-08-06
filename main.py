#TODO: Take the file name as an input (DONE)
#TODO: Take a folder as an input (loop through and print the comment number of each)
#TODO: Language support beyond python #

import io
import textwrap
import argparse

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

def print_data(file_name, number_of_comments):
    print textwrap.dedent("""\
    In the file: %s, there are %s comment lines
    """ %(file_name, number_of_comments))

def get_arguments():
    """ The argument parser of the command-line version """
    parser = argparse.ArgumentParser(description=('Comment counting program'))

    parser.add_argument('--input_file', '-i',
                        help="name of the input file", type=str, dest='i')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_arguments()
    input_file_name = args.i
    comment_count = numberOfComments(input_file_name)
    print_data(input_file_name, comment_count)
