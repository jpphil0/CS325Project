# This module (RedditScrape1.py) is the main program for downloading content from a Reddit post.
# It expects two command-line arguments: <URL> <raw_output_file.txt>
#   - <URL>: URL of the Reddit post to download.
#   - <raw_output_file.txt>: The name of the file to save the raw Reddit post content in the Data/raw directory.
# After downloading the content, it calls the extract_comments function from module3 to process the raw data.


import sys
import os
from Module2.RedditScrape2 import download_reddit_content
from Module3.ExtractComments import extract_comments

def main():
    if len(sys.argv) != 3:
        print("Usage: python file1.py <URL> <output_file.txt>")
    else:
        reddit_url = sys.argv[1]
        output_file_raw = os.path.join("Data", "raw", sys.argv[2])

        # Download Reddit content and save it to raw file
        download_reddit_content(reddit_url, output_file_raw)

        # Extract comments from the raw file and save them to processed file
        output_file_processed = "Data/processed/comments.txt"
        extract_comments(output_file_raw, output_file_processed)

if __name__ == "__main__":
    main()
