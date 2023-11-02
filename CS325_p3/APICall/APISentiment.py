import os
from bardapi import Bard
import re

# Bard API key
os.environ['_BARD_API_KEY']="cQhVmYRyqpWI_cnOwmRLvIX33n3tnSjI7_ItSJpGjTydKWk4Tbe7Z74gcgeyrtizugoVHA."

def generate_text(prompt):
    try:
        prompt=f"What is the sentiment of this sentence?\nComment: {comment}\nSentiment:",

        generated_text = Bard().get_answer(str(prompt))['content']
        return generated_text

    except Exception as e:
        print(f"An error occurred while generating text: {e}")
        return None

def classify_comment(comment):
    generated_response = generate_text(comment)
    # Test line to see if comments are being extracted properly
    print(f"Comment: '{comment}'")
    if generated_response:
        print(f"Generated Response: '{generated_response}'")
        print("\n")
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

if __name__ == "__main__":
    input_file = "comments.txt"
    comments = extract_comments(input_file)

    if not comments:
        print("No comments found in the input file.")
    else:
        for comment in comments:
            classify_comment(comment)

