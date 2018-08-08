from tabulate import tabulate
from main import *
import os

def filter_file(single_file):
    """ Method used to filter out unwanted files """
    if(single_file.endswith(".txt")
        or single_file.endswith(".py")
        or single_file.endswith(".java")
        or single_file.endswith(".s")):
            return single_file

def match_comment_type(file_name):
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
        return "null"

def define_headers():
    headers=["File Name","Line Count","Comment Count","Ratio"]
    return headers

def get_full_path(root_folder):
    """ Takes the name of a root folder and returns list of all the full name paths to each file"""
    absolute_list = []
    for dirpath,_,filenames in os.walk(root_folder):
        for f in filenames:
            absolute_list.append((os.path.abspath(os.path.join(dirpath, f))))
    return absolute_list

def parseFlagType(args):
    """ Input --> namespace object and output --> raw info of flag """
    if (args.input_folder != None):
        return args.input_folder
    elif (args.input_repo != None): #Will change here when needed to clone the repo into local machine, need to reutrn directory name regardless
        pass
    else:
        pass

def gather_data(args):
    """ Output all data into a tabulated form and out to CLI """
    returnTable = []
    directory = parseFlagType(args)
    os.chdir(directory)
    absolute_list = get_full_path(args.input_folder)
    for oneFile in absolute_list:
        if filter_file(oneFile):
            comment_count = compute_comment_stats(oneFile, match_comment_type(oneFile)) # In an endless loop here...
            line_count = compute_linenumber_stats(oneFile)
            ratio = round(float(comment_count)/float(line_count),3)
            stats = []
            stats.append(oneFile)
            stats.append(line_count)
            stats.append(comment_count)
            stats.append(ratio)
            returnTable.append(stats)
        else:
            pass
    return returnTable

def print_to_CLI(table):
    headers = define_headers()
    print((tabulate(table, headers)))
