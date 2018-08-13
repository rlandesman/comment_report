import os
import io
import textwrap
import argparse

new_repo_name = "new_repo" # Variable name of new repo being made (then delete_single_dir)


def parse_flag_type(args):
    """ Input --> namespace object and output --> raw directory location of flag object"""
    if (args.input_folder != None):
        return args.input_folder
    elif (args.input_repo != None): # Return full path directory name
        os.system("git clone " + args.input_repo + " " + new_repo_name)
        return os.path.abspath(new_repo_name)
    else:
        pass

def gather_data(args):
    """ Output all data into a tabulated form and out to CLI """
    returnTable = []
    directory = parse_flag_type(args)
    os.chdir(directory)
    absolute_list = get_full_path(directory)
    for oneFile in absolute_list:
        if filter_file(oneFile):
            comment_count = compute_comment_stats(oneFile, match_comment_type(oneFile))
            line_count = compute_linenumber_stats(oneFile)
            ratio = round(float(comment_count)/float(line_count),3) #To the third decimal spot
            stats = []
            stats.append(oneFile)
            stats.append(line_count)
            stats.append(comment_count)
            stats.append(ratio)
            returnTable.append(stats)
        else:
            pass
    return returnTable

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

def get_full_path(root_folder):
    """ Takes the name of a root folder and returns list of all the full name paths to each file"""
    absolute_list = []
    for dirpath,_,filenames in os.walk(root_folder):
        for f in filenames:
            absolute_list.append((os.path.abspath(os.path.join(dirpath, f))))
    return absolute_list

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

def is_valid_file(parser, arg):
    """ Check if file can be opened (legit path?) """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg
