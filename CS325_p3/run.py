# This script (run.py) is the entry point of the program.
# It checks the command-line arguments and calls the main function from Module1 to initiate the Reddit content download process.
# Usage: python run.py <URL> <raw_output_file.txt>
#   - <URL>: URL of the Reddit post to download.
#   - <raw_output_file.txt>: The name of the file to save the raw Reddit post content in the Data/raw directory.
# The program downloads the content from the specified Reddit post, processes it, and saves the extracted comments to the output file.

import sys
from Module1.RedditScrape1 import main


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run.py <URL> <output_file.txt>")
    else:
        main()