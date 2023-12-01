import os
import pandas as pd
import matplotlib.pyplot as plt

def read_sentiment_file(sentiment_file):
    # Read sentiment file into a pandas dataframe
    with open(sentiment_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Assuming sentiments are one per line in the file
    df = pd.DataFrame({'Sentiment': lines})

    return df

def plot_sentiments(df, output_plot_path, title):
    # Extract sentiments and counts
    sentiments = df['Sentiment'].str.strip()  # Remove leading/trailing whitespaces
    counts = sentiments.value_counts()

    # Plot the graph
    plt.bar(counts.index, counts, color=['green', 'yellow', 'red'])  # Customize colors as needed
    plt.title(title)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')

    # Add legend
    plt.legend(['Positive', 'Neutral', 'Negative'])  # Customize labels as needed

    # Save the plot
    plt.savefig(output_plot_path)
    plt.close()

def main():
    # Path to the folder containing sentiment files
    sentiment_files_folder = os.path.join("Data", "Sentiments")

    # Path to the folder to store plots
    output_plots_folder = os.path.join("Data", "Plots")

    # Create the output plots folder if it doesn't exist
    os.makedirs(output_plots_folder, exist_ok=True)

    # Iterate through sentiment files
    for sentiment_file in os.listdir(sentiment_files_folder):
        if sentiment_file.endswith("_comments.txt"):  # Assuming the sentiment files have a specific naming pattern
            sentiment_file_path = os.path.join(sentiment_files_folder, sentiment_file)

            # Read sentiment file
            df = read_sentiment_file(sentiment_file_path)

            # Extract title from the filename or URL (customize as needed)
            title_parts = os.path.splitext(sentiment_file)[0].replace("_comments", "").replace("_", " ").split()
            title = " ".join(title_parts[1:])

            # Create a sanitized title for the plot filename
            sanitized_title = title.replace(" ", "_").replace("'", "").lower()  # Customize as needed

            # Path to store the output plot
            output_plot_path = os.path.join(output_plots_folder, f"{sanitized_title}_plot.png")

            # Plot sentiments and save the plot
            plot_sentiments(df, output_plot_path, title)

if __name__ == "__main__":
    main()
