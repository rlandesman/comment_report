from tabulate import tabulate
from main import *

def check_file_type(file_name):
    """
    Check the type of a single file and return the correct charachter that needs to be checked for comments
    # -> python
    // -> Java
    # -> Textfile (my preference I recognize this loophole)
    """
    if(file_name.endswith(".txt")):
        return "#"
    elif(file_name.endswith(".py")):
        return "#"
    elif(file_name.endswith(".java")):
        return "/"
    elif(file_name.endswith(".s")):
        return "@"
    else:
        raise IOError

def print_to_CLI(args):
    """ Output all data into a tabulated form and out to CLI """
    headers=["File Name","Line Count","Comment Count","Ratio"]
    returnTable = []
    input_folder_name = args.input_folder
    list_files = iterate_folder(input_folder_name)
    for oneFile in list_files:
        comment_count = numberOfComments(oneFile, check_file_type(oneFile), input_folder_name)
        line_count = numberOfTotalLines(oneFile)
        ratio = round(float(comment_count)/float(line_count),3)
        stats = []
        stats.append(oneFile)
        stats.append(line_count)
        stats.append(comment_count)
        stats.append(ratio)
        returnTable.append(stats)
    return (tabulate(returnTable, headers))
