# Welcome to JSONPP


This package is nothing more than a wrapper for the basic JSON
json.dumps() function.  It simply takes as input a single JSON file
and outputs pretty printed JSON.  I didn't pass sort_keys because
I didn't see the value but feel free to submit a PR.

## Building


1. Bop the version on setup.cfg
2. python3 -m build -w
3. cd dist
4. pip3 install that file


## Usage
    usage: jsonpp [-h] [-i INDENT] [filename]

    positional arguments:
      filename              file to be pretty printed

    optional arguments:
      -h, --help            show this help message and exit
      -i INDENT, --indent INDENT
			    how much to indent

From python (you probably could do this on your own):

from jsonpp import jsonpp

string=jsonpp(file,indent=3)

