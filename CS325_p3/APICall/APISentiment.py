import openai
import re

# OpenAI API key
openai.api_key = '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'

def generate_text(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the ChatGPT 3.5 engine
            prompt=f"What is the sentiment of this sentence?\nComment: {comment}\nSentiment:",
            max_tokens=150  # Set the maximum length of the generated text
        )

        generated_text = response.choices[0].text.strip()
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

