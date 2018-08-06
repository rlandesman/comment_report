from tabulate import tabulate
def print_to_CLI():
    if(args.i != None):
        input_folder_name = args.i
        list_files = iterate_folder(input_folder_name)
        for oneFile in list_files:
            comment_count = numberOfComments(oneFile)
            line_count = numberOfTotalLines(oneFile)
            false_tuple = []
            false_tuple.append(oneFile)
            false_tuple.append(line_count)
            false_tuple.append(comment_count)
            returnTable.append(false_tuple)
        return (tabulate(returnTable, headers=["File Name","Line Count","Comment Count"]))
    elif(args.s != None):
        oneFile = args.s
        comment_count = numberOfComments(oneFile)
        line_count = numberOfTotalLines(oneFile)
        false_tuple = []
        false_tuple.append(oneFile)
        false_tuple.append(line_count)
        false_tuple.append(comment_count)
        returnTable.append(false_tuple)
        return (tabulate(returnTable, headers=["File Name","Line Count","Comment Count"]))

if __name__ == "__main__":
    print(print_to_CLI())
