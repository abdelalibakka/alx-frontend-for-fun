#!/usr/bin/python3
"""
script to convert Markdown to HTML
"""

import sys
import os

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get input and output file names
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        sys.stderr.write("Missing {}\n".format(markdown_file))
        sys.exit(1)

    # If all checks pass, print nothing and exit 0
    sys.exit(0)

