import re
import sys

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_program_name.py input_file.txt")
    else:
        input_file = sys.argv[1]
        output_file = "comments.txt"
        extract_comments(input_file, output_file)
