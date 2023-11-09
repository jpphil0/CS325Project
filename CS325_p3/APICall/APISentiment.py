import os
from bardapi import Bard
import re

# Bard API key
os.environ['_BARD_API_KEY'] = "xxxxxx"

def generate_text(comment):
    try:
        prompt = f"What is the sentiment of this sentence?\nComment: {comment}\nSentiment:"

        generated_text = Bard().get_answer(prompt)['content']
        return generated_text

    except Exception as e:
        print(f"An error occurred while generating text: {e}")
        return None

def classify_comment(comment, output_file):
    generated_response = generate_text(comment)

    # Test line to see if comments are being extracted properly
    # print(f"Comment: '{comment}'")  #print sentiments in the temrinal

    if generated_response:
        # print(f"Generated Response: '{generated_response}'")
        # Write comment and sentiment to the output file
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(f"Comment: '{comment}'\nSentiment: '{generated_response}'\n\n")
        print("Sentiment appended to the file.\n")
    else:
        print("Failed to generate response for the comment.\n")

# Function to extract comments from the input file
def extract_comments(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Use regular expression to extract individual comments
        comments = re.findall(r'(.+)', content)
        return comments

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    input_file = os.path.join("Data", "Processed", "comments.txt")
    output_file = os.path.join("Data", "Sentiments", "sentiments.txt")  # Name of the file to store sentiments

    comments = extract_comments(input_file)

    if not comments:
        print("No comments found in the input file.")
    else:
        for comment in comments:
            classify_comment(comment, output_file)


if __name__ == "__main__":
    main()