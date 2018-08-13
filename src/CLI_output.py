from tabulate import tabulate
from main import *

def define_headers():
    headers=["File Name","Line Count","Comment Count","Ratio"]
    return headers

def print_to_CLI(table, args):
    headers = define_headers()
    print((tabulate(table, headers)))
