from tabulate import tabulate
from main import *
import os

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
        pass

def getFullPathNames(root_folder):
    """ Takes the name of a root folder and returns list of all the full name paths to each file"""
    absolute_list = []
    for dirpath,_,filenames in os.walk(root_folder):
        for f in filenames:
            absolute_list.append((os.path.abspath(os.path.join(dirpath, f))))
    return absolute_list

def print_to_CLI(args):
    """ Output all data into a tabulated form and out to CLI """
    headers=["File Name","Line Count","Comment Count","Ratio"]
    returnTable = []
    os.chdir(args.input_folder)
    absolute_list = getFullPathNames(args.input_folder)

    for oneFile in absolute_list:
        comment_count = numberOfComments(oneFile, check_file_type(oneFile))
        line_count = numberOfTotalLines(oneFile)
        ratio = round(float(comment_count)/float(line_count),3)
        stats = []
        stats.append(oneFile)
        stats.append(line_count)
        stats.append(comment_count)
        stats.append(ratio)
        returnTable.append(stats)
    return (tabulate(returnTable, headers))
