import pandas as pd
import random

# Load the dataset from the CSV file
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df

# Data Sampling - Randomly sample a subset of the dataset
def data_sampling(dataset, num_samples):
    return dataset.sample(n=num_samples, random_state=42)

# Preprocess the data and return separate lists for code snippets, descriptions, and programming languages
def preprocess_data(df):
    code_snippets = df["code"].tolist()
    descriptions = df["description"].tolist()
    programming_languages = df["language"].tolist()
    return code_snippets, descriptions, programming_languages

def main():
    # Load the dataset
    dataset_path = "github_code_snippets.csv"
    dataset = load_dataset(dataset_path)

    # Data Sampling - Sample a subset of the dataset
    num_samples = 10000
    sampled_dataset = data_sampling(dataset, num_samples)

    # Preprocess the sampled data
    code_snippets, descriptions, programming_languages = preprocess_data(sampled_dataset)

    # Display the first few samples as a demonstration
    num_display_samples = 5
    for i in range(num_display_samples):
        print("Description:", descriptions[i])
        print("Code Snippet:", code_snippets[i])
        print("Programming Language:", programming_languages[i])
        print("=" * 40)

if __name__ == "__main__":
    main()
