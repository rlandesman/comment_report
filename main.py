#TODO: Take the file name as an input
#TODO: Take a folder as an input (loop through and print the comment number of each)
#TODO: Language support beyond python #

import io
import textwrap

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

def prettyPrint(file_name, number_of_comments):
    print textwrap.dedent("""\
    In the file: %s, there are %s comment lines
    testing test
    """ %(file_name,number_of_comments))

def main():
    comment_count = numberOfComments(file_name)
    prettyPrint(file_name, comment_count)

main()
