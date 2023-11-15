# This module (RedditScrape2.py) contains the download_reddit_content function.
# It expects two parameters:
#   - url (str): URL of the Reddit post to download.
#   - output_file (str): The name of the file to save the Reddit post content.
# The function interacts with the Reddit API to fetch post details and comments and saves them to the specified output file.

import praw

def download_reddit_content(url, output_file):
    try:
        # Initialize a PRAW Reddit client
        reddit = praw.Reddit(client_id='sMczX1S6WJHX5OiNJNl3xg',
                             client_secret='9JROcxfqSQMBY445SWAjm3ZYR7ZSQg',
                             user_agent='CS325Project1/1.0 by /u/omega-xxxvi')

  # Fetch the Reddit post using the API
        submission = reddit.submission(url=url)

        # Extract the title, user, and content
        post_title = submission.title
        post_user = submission.author.name
        post_content = submission.selftext
        upvote_ratio = submission.upvote_ratio
        score = submission.score

        comments = []
        for comment in submission.comments.list():
            comments.append(comment.body)
        comments_text = "\n".join(comments)

        # Save the text content, title, and user to a text file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Title: {post_title}\n")
            file.write(f"User: {post_user}\n\n")
            file.write(f"Upvote Ratio: {upvote_ratio}\n")
            file.write(f"Score: {score}\n\n")
            file.write(f"Content: \n{post_content}\n\n")
            file.write(f"Comments:\n{comments_text}")

        print(f"Content saved to '{output_file}'")

        # Return the post title for further use
        return post_title

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
