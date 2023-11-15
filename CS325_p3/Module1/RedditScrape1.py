# This module (RedditScrape1.py) is the main program for downloading content from a Reddit post.
# It expects two command-line arguments: <URL> <raw_output_file.txt>
#   - <URL>: URL of the Reddit post to download.
#   - <raw_output_file.txt>: The name of the file to save the raw Reddit post content in the Data/raw directory.
# After downloading the content, it calls the extract_comments function from module3 to process the raw data.


import sys
import os
from Module2.RedditScrape2 import download_reddit_content
from Module3.ExtractComments import extract_comments

def sanitize_filename(filename):
    # Replace problematic characters with underscores
    return "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in filename)

def process_urls_from_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as url_file:
            urls = url_file.read().splitlines()

        for idx, url in enumerate(urls, start=1):
            # Create a unique raw filename based on the order of input
            raw_filename = f"raw_{idx}.txt"
            output_file_raw = os.path.join("Data", "raw", raw_filename)

            # Download Reddit content and save it to a unique raw file
            post_title = download_reddit_content(url, output_file_raw)

            # Extract comments from the raw file and save them to a processed file
            sanitized_title = sanitize_filename(post_title)
            output_file_processed = os.path.join("Data", "processed", f"{sanitized_title}_comments.txt")
            extract_comments(output_file_raw, output_file_processed)

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python RedditScrape1.py <input_urls_file.txt>")
    else:
        input_file = sys.argv[1]
        process_urls_from_file(input_file)

if __name__ == "__main__":
    main()


