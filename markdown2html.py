#!/usr/bin/python3
"""
Script to convert Markdown to HTML
"""

import sys
import os
import re
import hashlib

def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts the content of a Markdown file to HTML and writes it to an output file.
    """
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # Regular expressions for matching Markdown syntaxes
    heading_pattern = re.compile(r'^(#{1,6})\s(.+)$', flags=re.MULTILINE)
    ul_pattern = re.compile(r'^-\s(.+)$', flags=re.MULTILINE)
    ol_pattern = re.compile(r'^\*\s(.+)$', flags=re.MULTILINE)
    paragraph_pattern = re.compile(r'^(.+)$', flags=re.MULTILINE)
    bold_pattern = re.compile(r'\*\*(.+?)\*\*')
    emphasis_pattern = re.compile(r'__(.+?)__')
    md5_pattern = re.compile(r'\[\[(.+?)\]\]')
    remove_c_pattern = re.compile(r'\(\((.+?)\)\)')

    # Function to replace Markdown syntaxes with HTML
    def replace_heading(match):
        level = len(match.group(1))
        heading_text = match.group(2)
        return f'<h{level}>{heading_text}</h{level}>'

    def replace_ul(match):
        return f'<ul><li>{match.group(1)}</li></ul>'

    def replace_ol(match):
        return f'<ol><li>{match.group(1)}</li></ol>'

    def replace_paragraph(match):
        return f'<p>{match.group(1)}</p>'

    def replace_bold(match):
        return f'<b>{match.group(1)}</b>'

    def replace_emphasis(match):
        return f'<em>{match.group(1)}</em>'

    def replace_md5(match):
        content = match.group(1).encode('utf-8')
        return hashlib.md5(content).hexdigest()

    def replace_remove_c(match):
        return match.group(1).replace('c', '')

    # Replace Markdown syntaxes with HTML
    html_content = heading_pattern.sub(replace_heading, markdown_content)
    html_content = ul_pattern.sub(replace_ul, html_content)
    html_content = ol_pattern.sub(replace_ol, html_content)
    html_content = paragraph_pattern.sub(replace_paragraph, html_content)
    html_content = bold_pattern.sub(replace_bold, html_content)
    html_content = emphasis_pattern.sub(replace_emphasis, html_content)
    html_content = md5_pattern.sub(replace_md5, html_content)
    html_content = remove_c_pattern.sub(replace_remove_c, html_content)

    # Write HTML content to the output file
    with open(html_file, 'w') as html_file:
        html_file.write(html_content)

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

