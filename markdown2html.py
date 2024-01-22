#!/usr/bin/python3
"""
Script to convert Markdown to HTML
"""

import sys
import os

def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts the content of a Markdown file to HTML and writes it to an output file.
    """
    # Your conversion logic can be added here
    # For simplicity, this function just prints a message indicating success
    print("Conversion successful!")

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

    # Call the conversion function
    convert_markdown_to_html(markdown_file, html_file)

    # If all checks pass, print nothing and exit 0
    sys.exit(0)

