# This script (run.py) is the entry point of the program.
# It checks the command-line arguments and calls the main function from Module1 to initiate the Reddit content download process.
# Usage: python run.py <URLList>
#   - <URLList>: a txt file listing the URLs of the Reddit posts to download.
# The program downloads the content from the specified Reddit post, processes it, and saves the extracted comments to the output file.

import sys
from Module1.RedditScrape1 import main

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <input_urls_file.txt>")
    else:
        main()
