# Import necessary modules
import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from openai import ChatCompletion
import openai

# Ensure the environment variable for AI Proxy token is set
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable not set.")
    sys.exit(1)

# Initialize OpenAI client with the provided API key
openai.api_key = AIPROXY_TOKEN

def analyze_dataset(file_path):
    """
    Load and analyze the dataset from the given file path.
    Returns the DataFrame and a dictionary containing analysis details.
    """
    # Load the dataset and handle potential file loading errors
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

    # Perform basic analysis: columns, data types, summary stats, missing values
    analysis = {
        "columns": list(df.columns),
        "dtypes": df.dtypes.apply(str).to_dict(),
        "summary_stats": df.describe(include='all').to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }
    return df, analysis

def generate_visualizations(df, output_dir):
    """
    Generate visualizations like correlation heatmap and distribution plots.
    Saves the visualizations in the specified output directory.
    """
    # Select numeric columns for correlation analysis
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 1:
        corr = df[numeric_columns].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
        plt.close()

    # Create a distribution plot for the first numeric column
    if len(numeric_columns) > 0:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[numeric_columns[0]], kde=True)
        plt.title(f"Distribution of {numeric_columns[0]}")
        plt.savefig(os.path.join(output_dir, f"{numeric_columns[0]}_distribution.png"))
        plt.close()

def narrate_story(analysis, output_dir):
    """
    Use OpenAI's API to generate a narrative about the dataset analysis.
    Saves the narrative in a README.md file in the output directory.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data scientist narrating the story of a dataset."},
                {"role": "user", "content": f"Here's the analysis of the dataset: {analysis}"}
            ]
        )
        story = response['choices'][0]['message']['content']
    except Exception as e:
        story = f"Error generating narrative: {e}"
    
    # Write the narrative to a README file
    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write(story)

def analyze_and_generate_output(file_path):
    """
    Perform dataset analysis, generate visualizations, and narrate a story.
    Returns the path to the output directory.
    """
    # Create an output directory based on the dataset's file name
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(".", base_name)
    os.makedirs(output_dir, exist_ok=True)

    # Analyze dataset and generate visualizations and narrative
    df, analysis = analyze_dataset(file_path)
    generate_visualizations(df, output_dir)
    narrate_story(analysis, output_dir)

    return output_dir

def main():
    """
    Main function to process command-line arguments and run the analysis.
    """
    if len(sys.argv) < 2:
        print("Usage: python autolysis.py dataset1.csv dataset2.csv ...")
        sys.exit(1)

    file_paths = sys.argv[1:]
    output_dirs = []

    # Iterate over each dataset file and process it
    for file_path in file_paths:
        if os.path.exists(file_path):
            output_dir = analyze_and_generate_output(file_path)
            output_dirs.append(output_dir)
        else:
            print(f"File {file_path} not found!")

    # Print the summary of where results are saved
    print(f"Analysis completed. Results saved in directories: {', '.join(output_dirs)}")

if __name__ == "__main__":
    main()