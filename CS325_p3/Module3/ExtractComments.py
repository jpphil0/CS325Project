# This module (ExtractComments.py) contains the extract_comments function.
# It expects two parameters:
#   - input_file (str): The name of the file containing the raw Reddit post content.
#   - output_file (str): The name of the file to save the extracted comments. This will be set to "comments.txt".
# The function reads the input file, extracts comments using regular expressions, and saves them to the specified output file.

import re

def extract_comments(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Use regular expression to extract comments
        comments = re.findall(r'Comments:\n(.+)', content, re.DOTALL)
        comments_text = comments[0].strip() if comments else ""

        # Save extracted comments to "comments.txt" file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(comments_text)

        print(f"Comments extracted and saved to '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")
