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
    else:
        raise IOError

def print_to_CLI(args):
    """ Output all data into a tabulated form and out to CLI """
    headers=["File Name","Line Count","Comment Count"]
    returnTable = []
    if(args.input_folder != None): #Folder
        input_folder_name = args.input_folder
        list_files = iterate_folder(input_folder_name)
        for oneFile in list_files:
            comment_count = numberOfComments(oneFile, check_file_type(oneFile))
            line_count = numberOfTotalLines(oneFile)
            false_tuple = []
            false_tuple.append(oneFile)
            false_tuple.append(line_count)
            false_tuple.append(comment_count)
            returnTable.append(false_tuple)
        return (tabulate(returnTable, headers))

    else: #single file
        oneFile = args.single_file
        print(check_file_type(oneFile))
        comment_count = numberOfComments(oneFile,check_file_type(oneFile))
        line_count = numberOfTotalLines(oneFile)
        false_tuple = []
        false_tuple.append(oneFile)
        false_tuple.append(line_count)
        false_tuple.append(comment_count)
        returnTable.append(false_tuple)
        return (tabulate(returnTable, headers))

if __name__ == "__main__":
    print(print_to_CLI())
