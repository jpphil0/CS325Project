import os
import pandas as pd
import matplotlib.pyplot as plt

def read_sentiment_file(sentiment_file):
    with open(sentiment_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sentiments = []
    current_sentiment = None

    for line in lines:
        if 'Sentiment:' in line:
            current_sentiment = line.split("Sentiment:")[1].strip()
        elif 'Comment:' in line and current_sentiment:
            sentiments.append(current_sentiment)
            current_sentiment = None

    if current_sentiment:
        sentiments.append(current_sentiment)

    df = pd.DataFrame({'Sentiment': sentiments})
    return df



def plotGraph(pos, neg, neu, title, output_plot_path):
    categories = ['Positive', 'Negative', 'Neutral']
    values = [pos, neg, neu]

    # Create figure and axes
    fig, ax = plt.subplots()

    # Plotting the bar graph using ax.bar
    ax.bar(categories, values, color=['green', 'red', 'yellow'], label=categories)

    # Adding labels and title
    ax.set_xlabel('Sentiments of Comments')
    ax.set_ylabel('Sentiment Count')
    ax.set_title(title)

    # Add legend with predefined labels
    ax.legend()

    # Display the plot
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
        if sentiment_file.endswith(".txt"):
            sentiment_file_path = os.path.join(sentiment_files_folder, sentiment_file)
            df = read_sentiment_file(sentiment_file_path)

            # Extract title from the filename
            title_parts = os.path.splitext(sentiment_file)[0].replace("_comments", "").replace("_", " ").split()
            title = " ".join(title_parts[1:])

            sanitized_title = title.replace(" ", "_").replace("'", "").lower()
            output_plot_path = os.path.join(output_plots_folder, f"{sanitized_title}_plot.png")

            negative=0
            positive=0
            neutral=0


            for i in range(len(df)):
                value_at_position_0_0 = df.iloc[i, 0]

                if( "negative" in str(value_at_position_0_0)):
                    negative=negative+1

                elif( "positive" in str(value_at_position_0_0)):
                    positive=positive+1    

                else:
                    neutral=neutral+1   
                     
            # print(positive," ",negative," ",neutral)
            plotGraph(positive,negative,neutral,title,output_plot_path)

if __name__ == "__main__":
    main()
