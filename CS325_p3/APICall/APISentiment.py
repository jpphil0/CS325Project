import os
from bardapi import Bard
import re
import time

MAX_RETRIES = 3
# Bard API key
os.environ['_BARD_API_KEY'] = "xxxxxx"

# Initialize Bard outside the loop
bard_instance = Bard()

def generate_text(comment):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            prompt = f"What is the sentiment of this sentence (use the word Positive, Negative, or Neutral)?\nComment: {comment}\nSentiment:"
            generated_text = bard_instance.get_answer(prompt)['content']
            return generated_text
        except Exception as e:
            print(f"An error occurred while generating text: {e}")
            if "429" in str(e):  # Check if the error contains a 429 status code
                retries += 1
                print(f"Retrying in 5 seconds (Retry {retries}/{MAX_RETRIES})...")
                time.sleep(5)
            else:
                return None
    print("Max retries reached. Unable to generate text.")
    return None

def classify_comment(comment, output_file):
    generated_response = generate_text(comment)
    # print(f"Comment: '{comment}'")  # print sentiments in the terminal

    if generated_response:
        if "Response Error" not in generated_response:
            with open(output_file, 'a', encoding='utf-8') as file:
                file.write(f"Comment: '{comment}'\nSentiment: '{generated_response}'\n\n")
            print(f"Sentiment appended to the file: {output_file}\n")
        else:
            print("Excluded response with 'Response Error' from being written.\n")
    else:
        print("Failed to generate response for the comment.\n")
        # with open(output_file, 'a', encoding='utf-8') as file:
            # file.write(f"Comment: '{comment}'\n\n")

def extract_comments_from_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        comments = re.findall(r'(.+)', content)
        return comments

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def process_files(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, f"sentiments_{filename}")

            comments = extract_comments_from_file(input_file)

            if not comments:
                print(f"No comments found in {input_file}.")
            else:
                for i, comment in enumerate(comments):
                    classify_comment(comment, output_file)

def main():
    input_folder = os.path.join("Data", "Processed")
    output_folder = os.path.join("Data", "Sentiments")

    process_files(input_folder, output_folder)

if __name__ == "__main__":
    main()
