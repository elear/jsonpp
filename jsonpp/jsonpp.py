#!python
"""
Very simple stupid program to pretty print JSON.
"""

import json
import argparse
from sys import stdin

def jsonpp(filename,indent=3):
    """
    Take as input a filename or None for stdin.
    Output pretty printed JSON.
    """

    if filename:
        with open(filename,'r',encoding='utf-8') as json_fp:
            jstring=json.load(json_fp)
    else:
        jstring=json.load(stdin)

    return json.dumps(jstring,indent=indent)

def cli():
    """
    take arguments to pass to json pretty print routine.
    """

    parser= argparse.ArgumentParser(description="pretty print json")
    parser.add_argument('-i','--indent', help="how much to indent",default=3)
    parser.add_argument('filename',nargs='?',help="file to be pretty printed")

    args=parser.parse_args()
    if args.filename:
        filename=args.filename
    else:
        filename='stdin'

    try:
        print(jsonpp(args.filename,int(args.indent)))
    except OSError as os_error:
        print(f'{filename}: ' + str(os_error))
    except json.decoder.JSONDecodeError as j_error:
        print(f'{filename}: JSON error: ' + str(j_error) + '\n')
    except ValueError:
        print(f'{filename}: indent should be a positive integer')
